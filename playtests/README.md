# Playtests

This folder stores filled-in playtest records for Transcendence encounters and mechanics.
Each file is a completed instance of a template from `../templates/`.

## Structure

```
playtests/
├── combat/        ← combat encounter playtests
├── exploration/   ← exploration and environment playtests
└── social/        ← social encounter and negotiation playtests
```

## Naming Convention

```
[category]-[enemy-or-encounter-slug]-[YYYY-MM-DD].md
```

Examples:
- `combat/combat-raknor-stalker-2026-04-15.md`
- `exploration/exploration-sunken-archive-2026-05-01.md`
- `social/social-merchant-guild-negotiation-2026-05-10.md`

## Workflow

1. Copy the relevant template from `../templates/`
2. Rename it following the convention above
3. Place it in the corresponding subfolder
4. Fill in all sections before and during the session
5. Complete section 16 (Playtest Log) after the session
6. Record adjustments in section 17 and flag any system changes needed

## What to Do With Findings

- Mechanic calibration issues → open a discussion or note in `docs/adr/`
- Rulebook text that needs updating → update `docs/system/` and flag in `transcendence-publications`
- Enemy design issues → update enemy entry in `docs/canon/` or relevant bestiary draft
- Recurring patterns across multiple playtests → consider a design framework entry in `docs/frameworks/`

## Templates

| Encounter type | Template |
|---|---|
| Combat | `../templates/combat-playtest.md` |
