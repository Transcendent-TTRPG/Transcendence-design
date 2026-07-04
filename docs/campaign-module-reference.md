# Campaign Module Reference

Documentos que cargar cuando se trabaja en módulos de campaña.
Organizado por tipo de tarea. No es necesario leer todo — carga lo que aplique al trabajo del momento.

---

## Siempre cargar primero

Estos dos documentos son la base de cualquier trabajo de módulo. Sin ellos, cualquier diseño de locación, criatura o encuentro puede contradecir la física del mundo o producir dinámicas inter-especie que no tienen sentido.

| Documento | Qué da |
| --- | --- |
| `docs/canon/world-foundations.md` | Qué es el Tauma, qué son los vestigos, qué son los Primordiales, qué son las ruinas humanas. La física del mundo. |
| `docs/canon/species-relations.md` | Cómo se relacionan las especies entre sí en 7 ejes + su posición frente al horror cósmico. Indispensable para cualquier PNJ o facción. |

---

## Por tipo de tarea

### Diseño de locación y entorno

La locación es el espacio donde ocurre el módulo: qué es el lugar, qué historia tiene, qué reglas físicas aplican ahí.

| Documento | Qué da |
| --- | --- |
| `docs/system/environmental-conditions.md` | Condiciones ambientales y su efecto mecánico (calor, frío, oscuridad, presión, etc.) |
| `data/system/environmental-conditions.yaml` | Datos estructurados de condiciones — usar para asignar severidades |
| `docs/system/cover-visibility-concealment.md` | Cobertura, visibilidad y ocultamiento — cómo el entorno afecta el combate |
| `docs/system/difficulty-thresholds.md` | Cómo calibrar dificultad de tiradas según el entorno |
| `docs/canon/vestigos/species-cultural-mapping.md` | Qué tipo de vestigos produce cada especie — útil si la locación tiene historia de ocupación |
| `docs/system/tauma-cosmology.md` | Mecánicas de concentración de Tauma por zona geológica — para locaciones con actividad primordial |

**Regla rápida de Tauma en locaciones:**
- Zonas volcánicas, fallas tectónicas, cuencas sísmicas → alta concentración ambiental
- Ruinas humanas → propiedades de material desconocido, NO concentración activa de Tauma per se
- Vestigos presentes → donde haya creencia colectiva sostenida, sin importar la geología

---

### Diseño de encuentros de combate

Los ADRs de combate son los documentos más importantes para diseño de encuentros. Todos están en `docs/adr/`.

| Documento | Qué da |
| --- | --- |
| `docs/adr/combat-encounter-architecture.md` | Estructura general de un encuentro — cuántos enemigos, roles, escalada |
| `docs/adr/combat-atb-timeline.md` | Cómo funciona la línea de tiempo ATB en un encuentro real |
| `docs/adr/combat-atb-rhythm-costs.md` | Costos de Ritmo y cómo afectan el ritmo del combate |
| `docs/adr/combat-champion-encounter.md` | Diseño de encuentros con campeón/jefe — cuándo y cómo |
| `docs/adr/combat-enemy-readability.md` | Cómo hacer que los enemigos sean legibles para los jugadores |
| `docs/system/atb-reference.md` | Referencia rápida del sistema ATB — fichas, Ritmo, orden de activación |
| `docs/system/wounds-and-damage.md` | Daño, heridas y consecuencias — calibrar lethality del encuentro |
| `docs/system/ailments.md` | Catálogo de Alteraciones — herramientas de presión táctica en encuentros |
| `data/system/ailments.yaml` | Datos de Alteraciones (nombres canónicos, efectos, duración) |

---

### Diseño de criaturas

Criaturas hostiles (no humanoides, no armadas) son el tipo de enemigo más frecuente en este proyecto.

| Documento | Qué da |
| --- | --- |
| `docs/system/creatures.md` | Cómo construir una criatura: estadísticas, herencias, comportamiento en combate |
| `docs/system/creature-cycles.md` | Ciclos de criatura — comportamientos por fase del encuentro |
| `docs/system/natural-attack-forms.md` | Formas de ataque natural — perfiles disponibles para criaturas |
| `data/system/natural-attack-forms.yaml` | Datos de formas de ataque natural |
| `data/system/weapon-technique-profiles.yaml` | Perfiles de técnica por arma — si la criatura tiene técnicas propias |
| `data/system/techniques.yaml` | Base de técnicas existentes — consultar antes de crear técnicas de criatura para evitar duplicados |

---

### Contenido Tauma, vestigos y lo sobrenatural

Para módulos donde los vestigos, la concentración de Tauma o los Primordiales son parte del contenido (exploración de ruinas, zonas primordiales, objetos cargados).

| Documento | Qué da |
| --- | --- |
| `docs/canon/world-foundations.md` | Mecanismo canónico de vestigos y Primordiales (si no se cargó ya) |
| `docs/system/tauma-cosmology.md` | Profundidad en cosmología del Tauma — cómo se concentra, qué produce |
| `docs/canon/vestigos/species-cultural-mapping.md` | Qué produce cada especie como vestigos, cómo los usan |
| `docs/canon/species-relations.md` — Eje 6 | Relación de cada especie con vestigos y ruinas (sección directamente aplicable) |

**Reglas rápidas de vestigos para módulos:**
- Los vestigos se forman donde hay creencia colectiva sostenida operando a través del Tauma base
- Un vestigo en una ruina interacciona con el campo de impronta previo de esa ruina — efectos posiblemente no documentados
- Los Primordiales requieren dos condiciones simultáneas: alta concentración geológica de Tauma + conciencia colectiva sostenida

---

### Entidades del Limbo

Para módulos con presencia de entidades extranormales (no Primordiales, no criaturas ordinarias).

| Documento | Qué da |
| --- | --- |
| `docs/system/limbo-entities.md` | Qué son las entidades del Limbo, cómo se forman, cómo se comportan |
| `docs/system/limbo-manifestations.md` | Tipos de manifestación — cómo se presentan en el mundo físico |
| `data/system/limbo-entities.yaml` | Catálogo de entidades |
| `data/system/limbo-manifestations.yaml` | Catálogo de manifestaciones |

---

### PNJs por especie

Para diseñar PNJs con coherencia interna de especie: motivaciones, comportamiento bajo presión, relación con otras especies.

| Documento | Qué da |
| --- | --- |
| `docs/canon/species-relations.md` — Ejes 1–5 | Dinámicas territoriales, económicas, conflictos civilizacionales, alianzas, reputaciones |
| `docs/canon/species-relations.md` — Eje 7 | Cómo cada especie se relaciona con el horror cósmico — informa motivaciones profundas |
| `docs/canon/species/<especie>.md` | Canon de especie: identidad, biología, civilización |
| `Transcendence-publications/core-books/transcendence-corebook/06-species/es/<especie>.md` | Stats, herencia, legados — lo que el PNJ puede hacer mecánicamente |

**Eje de especies más útil para PNJs en combate/exploración:**

| Si el PNJ es... | Leer en species-relations.md |
| --- | --- |
| Antagonista territorial | Eje 1 (nichos ecológicos) + Eje 5 (reputación como amenaza) |
| Guía o aliado económico | Eje 2 (interdependencia económica) |
| Obstáculo ideológico | Eje 3 (conflictos civilizacionales) |
| Aliado natural | Eje 4 (convergencias naturales) |
| Fanático o perturbado | Eje 7 (relación con horror cósmico) |

---

### Equipo y recompensas

Para diseñar loot, objetos encontrados, materiales extraíbles de la locación.

| Documento | Qué da |
| --- | --- |
| `docs/system/equipment-overview.md` | Categorías de equipo y su función en el sistema |
| `docs/system/combat-equipment-catalog.md` | Armadura y armas de combate — qué existe, rangos de stats |
| `docs/system/mundane-equipment-and-objects.md` | Objetos no combativos — herramientas, provisiones, equipo de exploración |
| `docs/system/materials-and-fabrication.md` | Materiales y su jerarquía — para loot de materias primas o items craftados |
| `data/system/combat-equipment-catalog.yaml` | Datos estructurados de equipo de combate |
| `data/system/equipment.yaml` | Datos generales de equipo |

---

### Facciones (secundario)

Solo necesario cuando el módulo incluye política de facción activa o consecuencias de reputación.

| Documento | Qué da |
| --- | --- |
| `docs/system/faction-reputation-and-alliances.md` | Sistema de reputación y alianzas — cómo rastrear relaciones con facciones |
| `data/system/faction-reputation-and-alliances.yaml` | Datos de facciones existentes |
| `docs/canon/species-relations.md` — Ejes 1–3 | Base de por qué las facciones existen y qué quieren |

---

## Qué NO cargar para módulos

Estos documentos son relevantes para trabajo de diseño del sistema, no para trabajo de módulo:

- `docs/system/technique-*.md` / `data/system/techniques.yaml` — solo si diseñas técnicas de criatura
- `docs/canon/species/*/technique-seeds.md` — solo si diseñas técnicas de especie
- `docs/adr/system-*.md` — decisiones de arquitectura del sistema, no de módulo
- `docs/knowledge/` — gobernanza interna del repo
