# CLAUDE.md

## Role
You are working in the Transcendence design repository, which is the source of truth for canon and system design.

## Priorities
1. Preserve canon consistency
2. Preserve mechanical consistency
3. Use existing templates and frameworks
4. Avoid inventing contradictory lore
5. Document major decisions clearly

## Rules
- Check `docs/vision/` before proposing major content
- Check `docs/canon/` before writing lore
- Check `docs/system/` before designing mechanics
- Check `docs/frameworks/` before creating structured content
- Check `docs/qa/` before finalizing

## Technique Authoring Rules

- Before authoring ANY technique, read `data/system/techniques.yaml` (taxonomy, cost model, authoring_questions)
- Before authoring a SPECIALIZATION technique, also read the relevant domain entry in `docs/system/specialization-technique-domains.md`
- Before authoring a technique that applies a condition, read `data/system/ailments.yaml`
- If a technique needs a condition/Alteration that does not exist, evaluate and define a generic Ailment first instead of forcing the closest existing condition; avoid species-flavored names for generic states
- When a technique applies an Ailment through an R.R., default severity scaling should usually be rank 1-2 Minor, rank 3-4 Moderate, rank 5-6 Severe
- Before authoring a technique for a species, read that species' file in `docs/canon/species/`

## Avoid
- Do not redefine canon casually
- Do not create implementation-specific assumptions unless documented
- Do not write publication prose here unless explicitly requested
