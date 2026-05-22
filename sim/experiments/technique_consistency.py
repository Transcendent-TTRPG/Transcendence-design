"""Intra-set technique consistency analysis.

Compares techniques against each other — not against basic actions.
Basic actions are intentionally less efficient by design; they are not a valid baseline.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass

from experiments.technique_value import _cached_technique_cost_runtime, run_technique_cost_iteration


@dataclass
class TechniqueEntry:
    """Aggregated result for one technique in the consistency analysis."""

    question_id: str
    technique_id: str
    rhythm: int
    attrition: int
    as_reaction: bool
    has_weapon_damage: bool
    value_avg: float
    hit_rate: float
    rhythm_efficiency: float       # value_avg / rhythm
    attrition_efficiency: float    # value_avg / max(1, attrition)
    secondary_metrics: dict[str, float]

    @property
    def is_utility(self) -> bool:
        """Utility techniques: no weapon damage exchange — value comes entirely from state/effect application."""
        return not self.has_weapon_damage


@dataclass
class ConsistencyCurve:
    """Efficiency curve for one technique family (damage or utility)."""

    family: str                    # "damage" or "utility"
    entries: list[TechniqueEntry]
    median_rhythm_efficiency: float
    median_attrition_efficiency: float
    low_bound: float
    high_bound: float
    outlier_threshold: float = 0.25

    def verdict(self, entry: TechniqueEntry) -> str:
        r = entry.rhythm_efficiency
        if r < self.low_bound:
            return "SOBRECOSTO"
        if r > self.high_bound:
            return "SUBCOSTO"
        return "OK"

    def fair_rhythm(self, entry: TechniqueEntry) -> float:
        if self.median_rhythm_efficiency <= 0:
            return float(entry.rhythm)
        return entry.value_avg / self.median_rhythm_efficiency

    def fair_attrition(self, entry: TechniqueEntry) -> float:
        if self.median_attrition_efficiency <= 0:
            return float(max(1, entry.attrition))
        return entry.value_avg / self.median_attrition_efficiency


@dataclass
class ConsistencyReport:
    """Full intra-set consistency report split by technique family."""

    entries: list[TechniqueEntry]
    damage_curve: ConsistencyCurve | None
    utility_curve: ConsistencyCurve | None


def run_consistency_analysis(
    question_ids: list[str],
    *,
    iterations: int = 2000,
    base_seed: int = 1,
    batch_size: int = 200,
    log_fn=None,
) -> ConsistencyReport:
    """Run all technique questions and analyze intra-set rhythm/attrition consistency.

    Each technique is measured independently. No basic action comparison is performed.
    Outliers are detected relative to the median of the full set.
    """
    log = log_fn or (lambda msg: None)
    entries: list[TechniqueEntry] = []

    for qid in question_ids:
        runtime = _cached_technique_cost_runtime(qid)
        name = qid.replace("naghii_", "").replace("_cost", "").replace("_", " ").title()
        log(f"\n  [{name}]  R={runtime.rhythm}  D={runtime.attrition}  reaction={runtime.as_reaction}  n={iterations}")

        accumulator: dict[str, float] = {}
        counts: dict[str, int] = {}

        for i in range(iterations):
            result = run_technique_cost_iteration(question_id=qid, seed=base_seed + i, runtime=runtime)
            for k, v in result.metrics.items():
                accumulator[k] = accumulator.get(k, 0.0) + v
                counts[k] = counts.get(k, 0) + 1

            if (i + 1) % batch_size == 0 or (i + 1) == iterations:
                current_val = accumulator.get("technique_value", 0.0) / counts.get("technique_value", 1)
                current_r_eff = accumulator.get("rhythm_efficiency", 0.0) / counts.get("rhythm_efficiency", 1)
                current_hit = accumulator.get("hit_rate", 0.0) / counts.get("hit_rate", 1)
                status = "DONE" if (i + 1) == iterations else "..."
                log(f"    iter {i+1:>5}  val={current_val:.3f}  ηR={current_r_eff:.3f}  hit={current_hit:.1%}  {status}")

        finals = {k: v / counts[k] for k, v in accumulator.items()}
        value_avg = finals.get("technique_value", 0.0)
        r_eff = finals.get("rhythm_efficiency", 0.0)
        d_eff = finals.get("attrition_efficiency", 0.0)
        hit = finals.get("hit_rate", 0.0)

        secondary = {
            k: v for k, v in finals.items()
            if k not in ("technique_value", "rhythm_efficiency", "attrition_efficiency", "hit_rate")
        }

        entries.append(TechniqueEntry(
            question_id=qid,
            technique_id=runtime.technique_id,
            rhythm=runtime.rhythm,
            attrition=runtime.attrition,
            as_reaction=runtime.as_reaction,
            has_weapon_damage=runtime.has_weapon_damage,
            value_avg=value_avg,
            hit_rate=hit,
            rhythm_efficiency=r_eff,
            attrition_efficiency=d_eff,
            secondary_metrics=secondary,
        ))

    threshold = 0.25

    def _build_curve(family: str, subset: list[TechniqueEntry]) -> ConsistencyCurve | None:
        if not subset:
            return None
        r_effs = [e.rhythm_efficiency for e in subset]
        d_effs = [e.attrition_efficiency for e in subset]
        med_r = statistics.median(r_effs)
        med_d = statistics.median(d_effs)
        return ConsistencyCurve(
            family=family,
            entries=subset,
            median_rhythm_efficiency=med_r,
            median_attrition_efficiency=med_d,
            low_bound=med_r * (1 - threshold),
            high_bound=med_r * (1 + threshold),
            outlier_threshold=threshold,
        )

    damage_entries = [e for e in entries if not e.is_utility]
    utility_entries = [e for e in entries if e.is_utility]

    return ConsistencyReport(
        entries=entries,
        damage_curve=_build_curve("damage", damage_entries),
        utility_curve=_build_curve("utility", utility_entries),
    )


def _format_curve(curve: ConsistencyCurve, title: str) -> list[str]:
    lines: list[str] = []
    lines.append(f"\n── {title} ──────────────────────────────────────────────────────")
    lines.append(f"   Mediana ηR: {curve.median_rhythm_efficiency:.3f}  "
                 f"Rango normal: [{curve.low_bound:.3f}, {curve.high_bound:.3f}]  (±{curve.outlier_threshold:.0%})")
    lines.append(f"   Mediana ηD: {curve.median_attrition_efficiency:.3f}")
    lines.append(f"\n   {'Técnica':<28} {'R':>3} {'D':>3} {'reac':>5}  "
                 f"{'val':>6} {'hit%':>6} {'ηR':>7} {'ηD':>7}  {'R-justo':>8} {'D-justo':>8}  Estado")
    lines.append("   " + "-" * 95)
    for entry in sorted(curve.entries, key=lambda e: e.rhythm_efficiency, reverse=True):
        name = entry.technique_id.replace("_", " ").title()
        verdict = curve.verdict(entry)
        fair_r = curve.fair_rhythm(entry)
        fair_d = curve.fair_attrition(entry)
        react_str = "sí" if entry.as_reaction else "no"
        lines.append(
            f"   {name:<28} {entry.rhythm:>3} {entry.attrition:>3} {react_str:>5}  "
            f"{entry.value_avg:>6.3f} {entry.hit_rate:>5.1%} {entry.rhythm_efficiency:>7.3f} {entry.attrition_efficiency:>7.3f}  "
            f"{fair_r:>8.2f} {fair_d:>8.2f}  {verdict}"
        )
    return lines


def format_consistency_report(report: ConsistencyReport) -> str:
    """Format a ConsistencyReport as two readable tables: damage curve and utility curve."""
    lines: list[str] = []
    lines.append("=" * 80)
    lines.append("CONSISTENCIA INTERNA — TÉCNICAS NAGHII")
    lines.append("Curvas separadas: daño (weapon_exchange) vs utilidad (check sin daño)")
    lines.append("=" * 80)

    if report.damage_curve:
        lines.extend(_format_curve(report.damage_curve, "CURVA DE DAÑO"))
    if report.utility_curve:
        lines.extend(_format_curve(report.utility_curve, "CURVA DE UTILIDAD"))

    lines.append("")
    lines.append("val = daño_efectivo + efectos_secundarios (pos, control, estados)")
    lines.append("val (utilidad) = tasa_aplicación + persistencia×0.5 + carga_forzada")
    lines.append("R-justo / D-justo = costo que pondría la técnica en la mediana de su curva")
    lines.append("SOBRECOSTO: ηR < mediana−25%  |  SUBCOSTO: ηR > mediana+25%")
    return "\n".join(lines)
