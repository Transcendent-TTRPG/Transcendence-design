# Panin Adaptability: partial transfer without lost competencies

- Status: creator-approved rule; empirical balance pending.
- Date: 2026-11-02.
- Scope: innate Technique #107, species summary, cards and narrative access.
- Supersedes: the former #107 specialization swap and its rest-based expiry.

## Decision

Keep the character's actual competencies. Select a trained source specialization
and a different target specialization with the same associated characteristic,
using a concrete transferable principle validated by the Narrator. For an eligible
target S.R., use `max(target_level + target_rank, source_rank)` as the competency
contribution. Apply die, target characteristic and other modifiers normally once.
Only actual training supplies either value; do not stack or chain transfers.

Maintain 1 source/target pair at NR 1–4, 2 at NR 5–8 and 3 at NR 9+.
One active use during the character's own activation adds or replaces one pair,
preserving the others. Cost is Rhythm 3 / Attrition 1 under pressure, with no
activation roll. Ordinary unpressured exploration follows general Attrition rules.
Pairs remain until replaced, without upkeep, per-roll payment or rest expiry.
Use current actual source rank and target training, updating without reactivation.

No granted levels, ranks, Synapsis, Techniques, prerequisites, unknown information,
Major Affinity changes, weapon competencies or Resistances. Practicing the actual
target can progress it under ordinary learning rules using its real level/rank;
selection itself grants no progress and does not duplicate progress in the source.
Actual training and Synapsis remain after replacing the adaptation.

## Fiction and amnesia

Mechanical selection need not be a consciously planned or named activation in
fiction. A Panin can make the association spontaneously. This is not a passive
bonus to every roll and does not remove costs, timing or capacity limits.

The creator approved Seku's spontaneous associative access at awakening using
only currently accessible experience. No competency menu, private history,
blocked Technique, language, initial selected pair or first-use scene is granted.
The actor chooses actions; GM adjudication must not choose those actions for him.

## Implementation and remaining checks

Structured definition: `data/system/techniques.yaml`, ID 107.
Reference: `docs/system/technique-adaptabilidad.md`.
No simulator implementation is claimed. Test change frequency under pressure,
preparation outside conflict, beginner/high-rank value and cross-Technique bonuses
before declaring the 3/1 cost or whole rule empirically balanced.
EN publication pairs and visual print validation are separate follow-up checks.
