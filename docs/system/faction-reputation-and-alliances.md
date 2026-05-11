# Faction Reputation, Public Renown, Alliances, and Commerce

**Authority data:** `data/system/faction-reputation-and-alliances.yaml`

This document defines the social-world layer that sits between raw scene interaction and long-term political or economic consequence.

It exists to answer questions like:

- who trusts the group right now;
- what kind of public pattern the group is becoming known for;
- what formal support a faction is willing to provide;
- and what kinds of goods, services, or restricted access the group can credibly obtain in a settlement.

This is **not** a personality system.
It does not define morality, inner alignment, or psychological essence.
It defines how organized groups and public structures read the party over time.

---

## Core Rule

Use four related but distinct layers:

- `Faction Standing` tracks how one specific faction currently relates to the group.
- `Public Renown` tracks the pattern of actions a faction associates with the group.
- `Alliance Status` tracks whether the relationship has crossed from goodwill into organized mutual commitment.
- `Commerce & Availability` tracks what can be reached in a place, and how social position changes price, access, and priority.

Do not collapse all four into one number.

---

## Why This System Exists

The social layer of the world should not depend only on one conversation roll at a time.

`Negociación`, `Liderazgo`, `Intimidación`, `Engaño`, `Imitación`, and similar specializations still resolve the live scene:

- can you secure this agreement right now;
- can you pressure this target;
- can you get through this audience;
- can you frame this exchange successfully.

But those rolls should happen inside a world that already has memory.

This system provides that memory without turning social play into a personality grid.

---

## Faction Standing

`Faction Standing` is always tracked **per faction**.
There is no single universal reputation value for the whole world.

At the framework level, use a short six-step relationship ladder:

| Standing | Meaning |
| --- | --- |
| `Hostile` | The faction treats the group as a danger, enemy, or direct liability |
| `Unwelcome` | The faction does not trust the group and limits access or cooperation |
| `Neutral` | No special trust or hostility; ordinary baseline treatment |
| `Favored` | The faction is willing to help within normal bounds and deal in good faith |
| `Trusted` | The faction is willing to share better access, better terms, and internal opportunities |
| `Allied` | The faction recognizes the group as a reliable partner with active mutual commitment |

### Standing rule

Standing should change when the group:

- materially helps the faction;
- materially harms the faction;
- supports or obstructs the faction's declared interests;
- honors or breaks a commitment the faction considers meaningful;
- becomes publicly associated with actions the faction cannot ignore.

### Standing change procedure

`Faction Standing` should move slowly.
It is a trust-state, not a scene-by-scene mood tracker.

Use this default procedure:

1. decide whether the action materially matters to that faction
2. decide whether the effect is `minor`, `major`, or `decisive`
3. move `Standing` only if the action crosses a real trust threshold

#### Default Standing shift bands

| Impact band | Default Standing change |
| --- | --- |
| `minor` | no immediate standing shift by itself |
| `major` | `+1` or `-1` standing step |
| `decisive` | `+2` or `-2` standing steps when the fiction clearly justifies it |

#### Minor vs major vs decisive

`Minor` should cover things like:

- one helpful conversation;
- one fair trade;
- one routine success that helps the faction a little;
- one small insult, inconvenience, or breach with no lasting consequence.

`Major` should cover things like:

- completing or sabotaging a meaningful job;
- materially helping a faction project succeed;
- publicly embarrassing or undermining the faction;
- honoring or violating a promise that mattered.

`Decisive` should be rare and should cover things like:

- saving or destroying something the faction considers strategically or symbolically critical;
- exposing treason, corruption, or sacred breach;
- betraying an alliance;
- delivering a victory or disaster the faction cannot reinterpret away.

#### Standing stability rule

Do not move `Standing` more than once for the same faction from the same underlying event chain unless:

- the first change reflected the immediate event;
- and a later consequence creates a second, distinct political meaning.

This keeps Standing from becoming noisy.

### What Standing changes

Standing is the main gate for:

- hospitality and safe reception;
- whether officials, merchants, or agents will even deal with the group;
- mission quality and trust-sensitive work;
- access to restricted information, infrastructure, or inventory;
- price pressure, urgency, and willingness to extend risk.

Standing should not by itself replace a live social roll when a scene is contested.
It changes the starting position and what outcomes are even plausible.

---

## Public Renown

`Public Renown` tracks **what kind of pattern** a faction believes it sees in the group's actions.

This preserves the useful part of the old matrix without treating it as personality or universal moral truth.

### Renown points

When the group takes a significant action that a faction can observe, verify, or hear about credibly, assign `1 Renown` with that faction.

Good triggers include:

- missions completed or failed in visible ways;
- protection, sabotage, rescue, betrayal, or exploitation;
- commercial behavior that affects others materially;
- factional resource extraction or destruction;
- public interventions that clearly help, destabilize, or profit from a situation.

Use larger swings only when the fiction clearly justifies a major public event.

### Renown gain procedure

`Public Renown` should move more often than `Faction Standing`.
It tracks visibility and repeated pattern, not trust.

Use this default procedure:

1. ask whether the faction can credibly witness, verify, or hear about the action
2. tag the action on both Renown axes
3. assign Renown based on event scale

#### Default Renown gain bands

| Event scale | Default Renown gain |
| --- | --- |
| `minor but visible` | `+1` |
| `major public event` | `+2` |
| `defining public event` | `+3` |

#### Renown loss or reversal

Use negative Renown when the group:

- fails publicly in a way that damages its known image;
- is exposed as acting against the profile a faction thought it represented;
- or becomes publicly tied to scandal, cowardice, incompetence, or hypocrisy in a way the faction cares about.

Negative Renown should usually be assigned to the profile the faction now associates with the failure or reversal.

#### Renown memory rule

Renown should be sticky, but not immortal.

If the group spends significant time acting in a different public pattern, the dominant profile with that faction may shift even without deleting the older one.

The important question is:

- what pattern does this faction now believe best describes the group

not:

- what was the very first thing the group ever did

### Renown axes

Each Renown mark should be tagged on two axes:

- `Constructive / Neutral / Destructive`
- `Altruistic / Personal / Selfish`

This does **not** claim to know the group's soul.
It records how the faction is reading the act.

### Renown profile matrix

At the framework level, use these public profile names:

| Actions \\ Motivations | `Altruistic` | `Personal` | `Selfish` |
| --- | --- | --- | --- |
| `Constructive` | `Benefactors` | `Builders` | `Magnates` |
| `Neutral` | `Observers` | `Independents` | `Opportunists` |
| `Destructive` | `Revolutionaries` | `Mercenaries` | `Tyrants` |

### Renown threshold rule

Every `10` Renown with a faction should normally produce one stronger step of recognition inside the currently dominant profile.

That does **not** automatically move `Faction Standing`.
A faction may believe the group are competent `Mercenaries`, admired `Benefactors`, or feared `Tyrants` without liking them more.

### Renown-to-Standing guideline

`Public Renown` can influence `Faction Standing`, but should not do so automatically.

Use this guideline:

- repeated positive Renown in a profile the faction values may justify a later positive Standing shift
- repeated negative Renown in a profile the faction fears or hates may justify a later negative Standing shift
- but a faction can admire competence, fear power, or hate effectiveness without ever becoming friendlier

So the right order is usually:

1. Renown establishes pattern
2. the faction interprets that pattern through its own values
3. only then, if trust actually changes, `Standing` shifts

### What Renown changes

Public Renown should affect:

- what kinds of offers the faction thinks suit the group;
- whether rumor or expectation precedes the group;
- which doors open through fame, fear, admiration, or notoriety;
- and which kinds of social modifiers make sense when dealing with that faction's members.

It is the correct layer for:

- “they know what kind of people we are becoming”

It is **not** the correct layer for:

- “they trust us personally”

That remains `Faction Standing`.

---

## Alliances

An alliance is not just goodwill.
It is a recognized relationship with obligations.

### Alliance status

At the framework level, use:

| Status | Meaning |
| --- | --- |
| `None` | No alliance exists |
| `Informal` | Mutual support exists, but mostly through practice and expectation |
| `Recognized` | The relationship is acknowledged and carries recurring privileges |
| `Sworn` | The relationship carries explicit commitments, duties, and breach consequences |
| `Broken` | A former alliance has been abandoned, violated, or publicly dissolved |

### Alliance formation

An alliance usually requires:

- at least `Favored` or stronger `Faction Standing`;
- one or more meaningful acts that align with faction interests;
- explicit narrative recognition from the faction;
- and some form of mutual expectation, not one-sided admiration.

### Alliance maintenance

An alliance should be maintained through:

- continued support;
- honoring requests or shared obligations;
- not acting directly against alliance interests without explanation;
- and responding when the alliance is publicly tested.

### Alliance benefits

Alliance benefits should usually come from curated packages, not from arbitrary stacking.

Common categories include:

- access to restricted goods or faction-only services;
- use of infrastructure such as forges, archives, shrines, libraries, or transport;
- privileged information and early warnings;
- expert assistance for defined projects;
- diplomatic sponsorship;
- military or logistical support in bounded situations;
- reduced scrutiny inside faction-controlled territory.

### Alliance costs

Alliances should also create:

- obligations;
- expectation of response;
- enemies by association;
- pressure not to assist rivals;
- and real fallout if the group disappears when needed.

### Broken alliances

If an alliance is broken, do not only remove benefits.
Also check:

- `Faction Standing` drop;
- loss of credibility with related factions;
- targeted retaliation or embargo;
- and whether the old ally becomes a faction that actively warns others about the group.

---

## Commerce and Availability

Trade should feel like part of the world, not a universal vending machine.

### Currency

The baseline money unit for ordinary market play is the `Shekel`.

This system does not need to redefine all coinage details.
It only needs one stable transactional unit so that prices, discounts, markups, labor, and sourcing pressure can be compared across regions.

### Commerce categories

For sourcing, trade, and settlement logic, group things into broad categories:

- `Consumables`
- `Equipment`
- `Materials and Resources`
- `Services`
- `Luxury Goods`
- `Authored Documents`

#### Category guidance

`Consumables` includes routine travel goods, food, writing supplies, basic light, and similar daily-use items.

`Equipment` includes adventuring gear, combat gear, tools, kits, and other practical carried objects.

`Materials and Resources` includes raw materials, processed materials, reagents, creature parts, and other crafting-facing inputs.

`Services` includes lodging, transport, treatment, labor, repair, refining, commissioning, and professional assistance.

`Luxury Goods` includes status goods, ceremonial goods, fine adornment, and nonessential prestige items.

`Authored Documents` includes plans, formulas, trap diagrams, maps, and other know-how objects whose value comes partly from information rather than substance alone.

### Availability categories

Use the same five-step availability ladder already compatible with the rest of the system:

| Availability | Meaning |
| --- | --- |
| `Common` | Readily available in most settlements |
| `Moderate` | Usually available in towns and larger markets |
| `Specialized` | Usually available only in serious trade centers or through known experts |
| `Rare` | Difficult to obtain without large-city access, influence, or special contacts |
| `Exceptional` | Extraordinary or capital-grade access only |

### Settlement availability ceiling

At the framework level, settlement scale should set a normal maximum availability ceiling:

| Settlement tier | Population guidance | Normal ceiling |
| --- | --- | --- |
| `Small Village` | up to `500` | `Common` |
| `Town` | `500–2,000` | `Moderate` |
| `City` | `2,000–10,000` | `Specialized` |
| `Major City` | `10,000–50,000` | `Rare` |
| `Capital / Metropolis` | `50,000+` | `Exceptional` |

This ceiling is the normal market expectation, not an absolute cosmic law.

### Local market rule

When the group tries to buy, commission, or source something through ordinary channels:

1. identify the item's `Commerce Category`
2. identify its `Availability`
3. compare that Availability to the settlement's normal ceiling
4. check whether a faction, alliance, or narrative exception changes access
5. apply `Faction Standing` to price, speed, and willingness to sell

If the item's Availability is at or below the local ceiling, it is normally sourceable through the local market unless another fiction-level restriction blocks it.

If the item's Availability is above the local ceiling, it is **not** normally sourceable through ordinary channels and requires an exception route.

### What can exceed the local ceiling

The local ceiling may be bypassed or raised when:

- a faction with relevant stock or infrastructure is willing to sponsor access;
- `Faction Standing` is high enough to open private inventories;
- an active `Alliance` grants access to non-public channels;
- or the fiction supports a one-off exception such as a caravan, embassy, black market route, or recent war supply.

### Price and access modifiers

Use `Faction Standing` first, then `Alliance Status`, to judge:

- price changes;
- waiting time;
- whether rare goods are offered at all;
- and whether the group gets first refusal, normal treatment, or last priority.

Good default logic:

- `Hostile`: no ordinary trade, punitive pricing, confiscation risk, or forced intermediaries
- `Unwelcome`: restricted access, worse terms, and low trust
- `Neutral`: baseline local pricing and availability
- `Favored`: better goodwill, modest discounts, or easier sourcing
- `Trusted`: better-than-market priority, access to held stock, and better service terms
- `Allied`: faction channels, protected access, and special exceptions when the fiction supports them

### Price pressure bands

When the fiction does not call for a more specific rate, use these baseline market shifts:

| Standing | Default market effect |
| --- | --- |
| `Hostile` | no ordinary sale; if trade happens anyway, at least `+50%` and under risk |
| `Unwelcome` | `+20%` price and lower willingness to source edge-case goods |
| `Neutral` | no modifier |
| `Favored` | `-10%` price or one favorable sourcing concession |
| `Trusted` | `-20%` price or priority access to held stock |
| `Allied` | `-20%` plus faction-channel exceptions when justified |

These are default market-pressure bands, not sacred numbers.
Use them when you want consistency without building a bespoke economy scene.

### Service priority and wait pressure

Standing also changes how long the group waits for attention, labor, or special access.

Good default logic:

| Standing | Default service priority |
| --- | --- |
| `Hostile` | refused unless coerced or hidden |
| `Unwelcome` | last priority; only after known clients |
| `Neutral` | normal queue |
| `Favored` | moved forward when possible |
| `Trusted` | priority treatment for bounded requests |
| `Allied` | direct internal routing when the faction controls the service |

### Alliance trade exceptions

An alliance should not simply mean “everything is cheaper.”

Its strongest trade effects should usually be:

- access to non-public inventories;
- permission to use faction infrastructure instead of buying the result at full price;
- access to specialists who do not serve the open market;
- bypassing one step of the local availability ceiling when the allied faction controls the relevant supply;
- and protection from ordinary local scarcity when the faction chooses to spend its own logistics on the group.

### Market sourcing outcomes

When a good or service is not immediately available, use one of these outcomes instead of a flat “no” whenever the fiction supports it:

- delayed sourcing
- limited quantity
- commission only
- restricted buyer scrutiny
- faction referral
- black-market route
- caravan wait
- embassy or guild channel
- refusal

This keeps shopping connected to the living world instead of reducing it to binary access.

### Baseline market catalog

This first layer is intentionally small.
It is meant to make ordinary trade playable without forcing the system to author every object in the world at once.

Use it as the default open-market layer for mundane adventuring life.

#### Baseline object catalog

These entries are starting references, not a claim that every region prices every good identically forever.

| Item | Category | Price | Availability | Weight / unit note |
| --- | --- | --- | --- | --- |
| `Travel backpack` | `Equipment` | `30 Shekels` | `Common` | `1 kg` |
| `Bedroll` | `Consumables` | `25 Shekels` | `Common` | `2 kg` |
| `Waterskin / canteen` | `Consumables` | `12 Shekels` | `Common` | `1 kg empty` |
| `Rain poncho` | `Consumables` | `12 Shekels` | `Common` | `0.5 kg` |
| `Rope (10 m)` | `Equipment` | `120 Shekels` | `Common` | `1.5 kg` |
| `Travel rations (1 day)` | `Consumables` | `10 Shekels` | `Common` | `0.5 kg` |
| `Torch` | `Consumables` | `10 Shekels` | `Common` | `1 kg` |
| `Wax candles (10)` | `Consumables` | `5 Shekels` | `Common` | `0.2 kg` |
| `Writing kit` | `Consumables` | `10 Shekels` | `Common` | `0.2 kg` |
| `Blank journal` | `Consumables` | `20 Shekels` | `Common` | `0.5 kg` |
| `Whetstone` | `Equipment` | `15 Shekels` | `Common` | `0.5 kg` |
| `Basic repair box` | `Equipment` | `35 Shekels` | `Common` | `3 kg` |
| `Field cook set` | `Equipment` | `30 Shekels` | `Common` | `2 kg` |
| `Bandages (10)` | `Consumables` | `8 Shekels` | `Common` | `0.2 kg` |
| `Antiseptic bottle` | `Consumables` | `20 Shekels` | `Common` | `0.3 kg` |
| `Oil lamp` | `Equipment` | `20 Shekels` | `Moderate` | `1 kg` |
| `Local territory map` | `Authored Documents` | `60 Shekels` | `Moderate` | `0.1 kg` |
| `Camouflage cloth` | `Equipment` | `30 Shekels` | `Moderate` | `1 kg` |
| `Compass` | `Equipment` | `35 Shekels` | `Moderate` | `0.3 kg` |
| `Mortar and pestle` | `Equipment` | `30 Shekels` | `Moderate` | `1.5 kg` |
| `Test tubes (5)` | `Equipment` | `15 Shekels` | `Specialized` | `0.5 kg` |
| `Climbing hooks set` | `Equipment` | `30 Shekels` | `Specialized` | `0.8 kg` |

#### Baseline ammunition goods

If a table wants mundane ammunition available without opening the full weapon-production economy yet, use:

| Item | Category | Price | Availability | Weight / unit note |
| --- | --- | --- | --- | --- |
| `Steel arrows (20)` | `Equipment` | `20 Shekels` | `Common` | `1 kg` |
| `Darts (10)` | `Equipment` | `10 Shekels` | `Common` | `0.3 kg` |
| `Sling stones (10)` | `Equipment` | `15 Shekels` | `Common` | `2 kg` |

Specialty ammunition should usually begin at `Specialized` availability or higher unless the setting gives a strong reason otherwise.

#### Baseline service catalog

| Service | Category | Price guidance | Availability | Notes |
| --- | --- | --- | --- | --- |
| `Common lodging` | `Services` | `10–20 Shekels / night` | `Common` | Basic room or shared shelter equivalent |
| `Modest meal` | `Services` | `5–10 Shekels` | `Common` | One decent meal in a routine settlement |
| `Animal stabling / care` | `Services` | `8–15 Shekels / day` | `Common` | Ordinary housing and feed |
| `Local messenger` | `Services` | `10–25 Shekels` | `Common` | Within the same settlement or nearby route |
| `Short secure storage` | `Services` | `5–15 Shekels / day` | `Common` | Non-faction protected storage |
| `Local guide` | `Services` | `30–80 Shekels / day` | `Moderate` | Settlement, nearby roads, or known terrain only |
| `Map copy or update` | `Services` | `40–120 Shekels` | `Moderate` | Depends on scope and source quality |
| `Minor equipment repair` | `Services` | `20–80 Shekels` | `Moderate` | Not a full rebuild; uses local craft capacity |
| `Routine treatment` | `Services` | `20–100 Shekels` | `Moderate` | Stabilization, cleaning, ordinary medical handling |
| `Appraisal` | `Services` | `20–60 Shekels` | `Moderate` | Object, material, or trade-value judgment |
| `Passenger transport` | `Services` | `varies by route and danger` | `Moderate` | Use route length and security as main drivers |
| `Private specialist consultation` | `Services` | `100+ Shekels` | `Specialized` | Alchemist, scholar, engineer, jeweler, etc. |

#### Catalog use rule

Use this first layer when:

- the group wants ordinary market interaction;
- the object is not unique enough to deserve its own authored chapter;
- and the table needs a stable baseline faster than a bespoke negotiation scene.

If the fiction strongly cares about regional identity, scarcity, danger, or faction control, treat these prices as baseline references and let `Standing`, `Alliance`, and `Availability` do the real shaping.

### What Commerce is for

This layer should answer:

- can we buy it here;
- who is willing to sell it to us;
- how hard is it to source;
- and what social position changes the result.

It should not try to catalog every mundane object before the world needs it.

---

## Design Rule For Social Systems

Do not use one global moral alignment grid to determine:

- trust;
- prices;
- political access;
- alliance strength;
- or public identity.

Use:

- `Faction Standing` for trust and access;
- `Public Renown` for recognizable action pattern;
- `Alliance Status` for formal or semi-formal commitment;
- `Commerce & Availability` for market reality.

This keeps the world socially legible without pretending that all factions read the same act the same way.

---

## Ability Design Surfaces

When a Technique, feature, background, or other authored element touches this system, it should usually modify one or more of these surfaces:

- standing shift with a bounded faction set;
- renown gain, loss, or reinterpretation;
- alliance formation, maintenance, or strain;
- access gate to goods, information, or infrastructure;
- price modifier or priority of service;
- settlement availability exception;
- social starting position inside a faction-controlled scene.

Do not let abilities rewrite the whole social world globally unless the effect is truly exceptional and world-scale.

---

## Summary

1. Reputation is per faction.
2. Public Renown is a faction-facing pattern, not personality truth.
3. Alliances are living commitments, not just bonus flags.
4. Trade depends on settlement scale, faction trust, and alliance access.
5. Social specializations still resolve the live scene; this system determines what the world remembers and what it allows.
