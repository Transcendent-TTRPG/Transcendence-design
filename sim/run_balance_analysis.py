"""Balance analysis: intra-set rhythm/attrition consistency for Naghii techniques.

Basic actions are NOT used as baseline — they are intentionally less efficient by design.
Techniques are compared against each other using median rhythm efficiency as the reference point.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from experiments.technique_consistency import format_consistency_report, run_consistency_analysis
from experiments.technique_value import _cached_technique_cost_runtime, run_technique_cost_experiment, run_technique_cost_iteration

COST_QUESTIONS = [
    "naghii_cerrar_la_linea_cost",
    "naghii_clavar_el_paso_cost",
    "naghii_recuperar_la_distancia_cost",
    "naghii_anudar_el_paso_cost",
    "naghii_robar_el_angulo_cost",
    "naghii_marcar_la_lectura_cost",
    "naghii_nublar_la_senal_cost",
    "naghii_doblar_el_tiro_cost",
    "naghii_clavar_la_cadencia_cost",
    "naghii_tocar_y_ceder_cost",
    "naghii_pesar_el_umbral_cost",
    "naghii_trabar_el_gesto_cost",
]

# Info-only techniques with no scorable sim output — resolution_rate is the primary metric
DATA_ONLY_QUESTIONS = [
    "naghii_leer_el_calor_del_paso_cost",
]

DERIVED_QUESTIONS = [
    "naghii_doblar_el_tiro_effectiveness",
    "naghii_marcar_la_lectura_effectiveness",
    "naghii_nublar_la_senal_effectiveness",
    "naghii_recuperar_la_distancia_reposition_value",
    "naghii_robar_el_angulo_effectiveness",
]

ITERATIONS = 2000
BATCH_SIZE = 200
OUTPUT_FILE = Path(__file__).parent / "reports" / "balance_analysis_naghii.txt"


def log(out, msg: str) -> None:
    print(msg, flush=True)
    out.write(msg + "\n")
    out.flush()


def run_derived_with_progress(qid: str, *, out) -> None:
    runtime = _cached_technique_cost_runtime(qid)
    name = qid.replace("naghii_", "").replace("_", " ").title()
    log(out, f"\n  [{name}]  n={ITERATIONS}")

    accumulator: dict[str, float] = {}
    counts: dict[str, int] = {}

    for i in range(ITERATIONS):
        result = run_technique_cost_iteration(question_id=qid, seed=i + 1, runtime=runtime)
        for k, v in result.metrics.items():
            accumulator[k] = accumulator.get(k, 0.0) + v
            counts[k] = counts.get(k, 0) + 1
        if (i + 1) % BATCH_SIZE == 0 or (i + 1) == ITERATIONS:
            status = "DONE" if (i + 1) == ITERATIONS else "..."
            log(out, f"    iter {i+1:>5}  {status}")

    finals = {k: v / counts[k] for k, v in accumulator.items()}
    requested = runtime.metric_ids
    for mid in requested:
        if mid in finals:
            log(out, f"    {mid:<45} {finals[mid]:.3f}")


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w") as out:
        log(out, "=" * 80)
        log(out, "BALANCE ANALYSIS — NAGHII: CONSISTENCIA INTERNA DE COSTOS")
        log(out, f"n={ITERATIONS} por técnica  |  batch={BATCH_SIZE}  |  sin baseline de acción básica")
        log(out, f"Precisión estimada (CI 95%): ±{1.96 * 0.5 / (ITERATIONS ** 0.5):.1%} en métricas binarias")
        log(out, "=" * 80)

        n_cost = len(COST_QUESTIONS)
        log(out, f"\n── ANÁLISIS DE CONSISTENCIA ({n_cost} técnicas de costo) ─────────────────────\n")

        report = run_consistency_analysis(
            COST_QUESTIONS,
            iterations=ITERATIONS,
            batch_size=BATCH_SIZE,
            log_fn=lambda msg: log(out, msg),
        )

        log(out, "\n\n" + format_consistency_report(report))

        log(out, "\n── PREGUNTAS DERIVADAS (efectividad de superficie secundaria) ──────────")
        for qid in DERIVED_QUESTIONS:
            run_derived_with_progress(qid, out=out)

        log(out, "\n── TÉCNICAS DATA-ONLY (sin output medible — resolution_rate es la métrica) ─")
        log(out, "  Nota: technique_value=0 porque el output es Narrador-lado, no estado sim")
        for qid in DATA_ONLY_QUESTIONS:
            run_derived_with_progress(qid, out=out)

        log(out, "\n" + "=" * 80)
        log(out, "FIN DEL ANÁLISIS")
        log(out, f"Resultados en: {OUTPUT_FILE}")
        log(out, "=" * 80)


if __name__ == "__main__":
    main()
