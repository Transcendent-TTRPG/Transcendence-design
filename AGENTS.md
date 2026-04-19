# AGENTS — Transcendence Design

This file instructs AI agents working in the design repository on how to approach mechanical definition tasks and keep all files in sync.

## Before every task

1. Read `CLAUDE.md` — priorities and constraints for this repo.
2. Read `docs/system/index.md` — locate the relevant reference file before touching anything.
3. Check `docs/adr/` for any existing decision that affects the area you are working on.
4. Follow the `mechanic-registrar` skill from `../pipeline/SKILLS.md` for every change.

## The registration rule

**Every mechanical definition must be registered in at least three places:**

| Place | What goes there |
| --- | --- |
| `data/system/*.yaml` | The authoritative numeric or structural definition |
| `docs/system/<file>.md` | The human-readable reference |
| `Transcendence-publications/canon/glossary.md` | The term in ES + EN with translation flag |

If any of these three is missing, the definition is incomplete.

Additionally, check:

| Condition | Also update |
| --- | --- |
| Concept is an ability surface | `docs/system/mechanics-overview.md` §Ability design surfaces |
| Concept changes a key number | `docs/system/index.md` §Key Numbers |
| Concept required a design decision | `docs/adr/<topic>.md` |
| Term is used frequently in prose | `Transcendence-publications/CLAUDE.md` cheat sheet |

## File authority map

When values conflict between files, the authority order is:

1. `data/system/*.yaml` — numeric truth (formulas, costs, thresholds)
2. `docs/adr/*.md` — structural decisions (what is allowed, what is excluded)
3. `docs/system/*.md` — human-readable reference (derived from the above)
4. Corebook files — downstream; must be updated to match, not used to override

## Checklist before closing any design task

- [ ] Does the new concept have a YAML definition in `data/system/`?
- [ ] Does the relevant `docs/system/*.md` file reflect the change?
- [ ] Is the term in `canon/glossary.md` with correct ES + EN mapping?
- [ ] Is `docs/system/mechanics-overview.md` up to date with any new ability surfaces?
- [ ] Does `docs/system/index.md` §Key Numbers need updating?
- [ ] If a design decision was made, is there an ADR entry?
- [ ] Are there corebook files that state values now outdated by this change?

## Hard rules

- Do not invent values. If a number is not in `data/system/`, it does not exist yet — create it there first.
- Do not create a new term in any prose file before adding it to `canon/glossary.md`.
- Do not modify `data/system/*.yaml` without also updating the corresponding `docs/system/*.md`.
- ADRs are append-only. Do not delete or rewrite existing decisions — add a new decision that supersedes them and note the supersession.
