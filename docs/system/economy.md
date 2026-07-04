# Economy

**Authority data:** `data/system/economy.yaml` (pending)
**Related docs:** `docs/system/mundane-equipment-and-objects.md`, `docs/system/materials-and-fabrication.md`, `docs/canon/world-foundations.md`

---

## Purpose

This document defines the economic layer of the system: currency, cost of living, wage rates, income methods, equipment maintenance costs, and inter-settlement pricing. It is the design authority for questions about what things cost, what characters can earn, and how the economy of a post-apocalyptic fragmented world behaves mechanically.

Item prices for mundane objects are defined in `docs/system/mundane-equipment-and-objects.md`. This document defines the economic context those prices exist within.

---

## The Shekel

The Shekel is the universal currency of the world. Its value is not guaranteed by any state or central institution — it is guaranteed by the accumulated consensus of all who trade. In a fragmented and hostile world, that consensus is more durable than any government.

A Shekel is a unit of weight in standardized metal. Its form varies between settlements and regions, but its weight and composition are recognizable to any experienced trader. Accepting Shekels does not imply trust in the individual offering them — it implies trust that whoever receives them tomorrow will also accept them.

---

## Cost of Living

Infrastructure within a settlement — common stores, shared defenses, access to local artisans — reduces the cost of subsistence. Outside the walls, every ration, resource, and drop of purified water carries the price of the risk and effort it took to bring it there.

### Inside a settlement

| Level | Daily cost | Covers |
| --- | --- | --- |
| `subsistence` | 12 S/day | Basic food from common stores, shared lodging, water access |
| `comfortable` | 35 S/day | Good food, private room, basic equipment maintenance |
| `prosperous` | 80 S/day | Varied and abundant food, quality private lodging, well-maintained equipment and some extras |

### On route between settlements

| Level | Estimated daily cost | Notes |
| --- | --- | --- |
| `subsistence` | 20–25 S/day | Field rations, purified or stored water, no fixed shelter |
| `comfortable` | 55–70 S/day | Quality supplies, survival tools, inns at intermediate stops if available |

Every resource on the road carries the price of having been brought through hostile terrain.

---

## Wages

Specialized knowledge is scarce. An expert artisan who dies at sixty instead of their possible one hundred and twenty is knowledge that is not easily replaced. That scarcity has a price.

| Activity | Daily wage |
| --- | --- |
| Unskilled labor (hauling, cleaning, basic guard duty) | 12–18 S/day |
| Rank 1–2 specialization (functional skilled work) | 40–70 S/day |
| Rank 3–4 specialization (advanced work, low local competition) | 100–160 S/day |
| Rank 5+ specialization (recognized master, probably unique in the region) | 200 S/day or more |

These values apply inside a settlement. A specialist working on the road or in the field may charge a risk surcharge on top of their base wage.

---

## Income Methods

### Narrator contracts

The primary income source for adventuring groups. A contract has a client — a settlement, a faction leader, a merchant, a specialist — and pays for concrete results: a creature neutralized, a route mapped, an object recovered, a person rescued.

Orientation rates by duration and risk:

| Contract profile | Pay per character |
| --- | --- |
| Short task, low risk (1–2 days, known zone) | 100–250 S |
| Medium task, moderate risk (3–5 days, unknown terrain) | 300–700 S |
| Extended mission, real risk (1–2 weeks, defined threat) | 800–1,800 S |
| Critical mission, severe danger (variable duration, high death risk) | 2,000 S or more |

These are orientation values. A poor settlement may not have Shekels available and pay in materials, equipment, or service debts. A wealthy client may pay more when urgency justifies it.

### Material sales

Materials extracted from creatures, ruins, or deposits have sale value. Price is determined by local demand and material grade. Exceptional-grade or threshold-origin materials are rare and valuable, especially for alchemists and specialized artisans.

The price of a material depends on the settlement receiving it and how locally available it is.

### Specialization services

A character with a specialization may offer their skills directly to others. A blacksmith can forge commissions; an alchemist can produce compounds on request; a physician can treat third-party injured.

The price of a service has two components:

- **Material cost** — what is consumed during the work, paid by the client
- **Labor fee** — the specialist's wage based on time invested and their rank

The fee is negotiable, but a high-rank specialist who accepts less than the value of their time is effectively subsidizing the client.

### Exploration of dangerous zones

Some income sources are not formal contracts but a direct consequence of going where others do not. High taumatic concentration zones — Primordial territories, high-intensity anomalies, documented extranatural environments — contain materials not found under normal conditions. Among these are threshold materials: natural matter that the taumatic gradient has structurally altered over time.

Extracting threshold materials from these zones is possible but extremely dangerous. The risk is not only the creatures in the environment — it is the extranatural concentration itself, which can produce severe Afflictions through sustained exposure. The price of threshold materials reflects that mortality rate.

Human ruins are not a source of materials or any other resource. Nothing inside is usable — not construction materials, not objects, not residual technology. Ruins are sites of worship, interpretation, and death, in that order.

---

## Equipment Maintenance

Equipment with living components — materials in the living state as defined in the material taxonomy — requires active maintenance. Without it, the biological component fails, reducing or canceling the properties that made it valuable.

The maintenance cost of an object with a living component is a periodic fraction of its fabrication value. The Narrator sets the frequency based on the organism involved (may be daily, weekly, or monthly) and the cost based on the accessibility of the required inputs.

Pure inert equipment — only metal, wood, fiber, or leather without active biological components — requires no maintenance beyond normal use. A forged iron sword may rust if neglected, but it does not die. An object with living plates or a reactive grip that does not receive its maintenance will eventually rot, wither, or compromise the rest of the user's equipment.

---

## Inter-Settlement Surcharge

A material, tool, or compound produced in another settlement implicitly carries the cost of the journey that brought it there. As orientation, goods originating from another settlement cost between 50% and 100% more than their local fabrication price.

The exact surcharge depends on:

- distance;
- route danger;
- whether the trader brought it exclusively or as part of a caravan.

---

## Quick Price Reference

For item prices, see `docs/system/mundane-equipment-and-objects.md`.

Key calibration values:

| Object | Price | Approximate equivalence |
| --- | --- | --- |
| Field rations (1 day) | 10 S | ~60–80% of minimum daily wage |
| Bandages (10) | 8 S | ~50–65% of minimum daily wage |
| Rope (10 m) | 120 S | ~7–10 days of minimum wage |
| Compass | 35 S | ~2 days of minimum wage |
| Travel backpack | 30 S | ~2 days of minimum wage |
| Field rations (1 week) | 70 S | ~4–6 days of minimum wage |
