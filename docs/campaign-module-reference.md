# Campaign Module Reference

Documentos que cargar cuando se trabaja en módulos de campaña.
Organizado por tipo de tarea. No es necesario leer todo — carga lo que aplique al trabajo del momento.

**Skill:** Para cualquier trabajo de módulo, usar la skill `skills/module-development/SKILL.md`.

---

## Antes de cualquier trabajo de módulo

Leer los axiomas de diseño primero. Toda decisión de módulo se valida contra estos 7 principios.

| Documento | Qué da |
| --- | --- |
| `docs/modules/module-design-axioms.md` | Los 7 axiomas: presencia orgánica de sistemas, cadencia arrítmica, horror como textura, exposición progresiva, cohesión de setting, estructura anti-cliché, arco largo no exhaustivo |

---

## Siempre cargar primero

Estos dos documentos son la base de cualquier trabajo de módulo. Sin ellos, cualquier diseño de locación, criatura o encuentro puede contradecir la física del mundo o producir dinámicas inter-especie que no tienen sentido.

| Documento | Qué da |
| --- | --- |
| `docs/canon/world-foundations.md` | Fundamentos base. (Nota: Para reglas específicas de Vestigos y Entidades, ver la sección de Horror Cósmico abajo). |
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

**Regla rápida de Tauma en locaciones:**
- Zonas volcánicas, fallas tectónicas, cuencas sísmicas → alta concentración ambiental
- Ruinas humanas → propiedades de material desconocido, NO concentración activa de Tauma per se
- Vestigos presentes → donde haya creencia colectiva sostenida, sin importar la geología

---

### Diseño de encuentros de combate y *Ailments*

Para la estructuración de la dificultad, daño y los estados alterados físicos que los jugadores pueden sufrir en combate o exploración. Los ADRs proveen las matemáticas del encuentro, pero la estructura final usa el *Corebook*.

| Documento | Qué da |
| --- | --- |
| `docs/adr/combat-atb-timeline.md` | Cómo funciona la línea de tiempo ATB en un encuentro real |
| `docs/adr/combat-atb-rhythm-costs.md` | Costos de Ritmo y cómo afectan el ritmo del combate |
| `docs/system/atb-reference.md` | Referencia rápida del sistema ATB — fichas, Ritmo, orden de activación |
| `docs/system/wounds-and-damage.md` | Daño, heridas y consecuencias — calibrar lethality del encuentro |
| `.../core-books/transcendence-corebook/14-adversaries-and-bestiary/es/05-construccion-encuentros.md` | **Reglas oficiales** de presupuestos de encuentro y letalidad. |
| `.../core-books/transcendence-corebook/11-ailments/es/01-agravios.md` | **Ailments (Mecánica Core):** Escala de intensidad para estados alterados. |
| `.../core-books/transcendence-corebook/11-ailments/es/02-alteraciones.md` | **Ailments (Combate):** Estados alterados cinéticos y de trauma. |
| `.../core-books/transcendence-corebook/11-ailments/es/04-venenos.md` | **Ailments (Combate/Exploración):** Toxinas y venenos ambientales o de criaturas. |
| `.../core-books/transcendence-corebook/11-ailments/es/05-infecciones.md` | **Ailments (Exploración/Combate):** Enfermedades biológicas no vinculadas al Limbo. |

---

### Diseño de criaturas y adversarios (Bestiario Oficial)

Para diseñar monstruos, criaturas y antagonistas, **usar exclusivamente el Capítulo 14 del Corebook** en lugar de los documentos de diseño antiguos, ya que contienen la narrativa pulida y los ciclos autónomos oficiales. Además, apóyate en los datos crudos `.yaml` para matemáticas base.

| Documento | Qué da |
| --- | --- |
| `.../core-books/transcendence-corebook/14-adversaries-and-bestiary/es/01-doctrina.md` | Filosofía de diseño de criaturas en Transcendence. |
| `.../core-books/transcendence-corebook/14-adversaries-and-bestiary/es/02-zonas.md` | Arquitectura del adversario por partes/zonas atacables. |
| `.../core-books/transcendence-corebook/14-adversaries-and-bestiary/es/03-rasgos.md` | Habilidades estáticas y pasivas de las criaturas. |
| `.../core-books/transcendence-corebook/14-adversaries-and-bestiary/es/04-ciclos-autonomos.md` | Patrones de comportamiento en combate según el estrés/daño. |
| `data/system/natural-attack-forms.yaml` | Datos crudos de armas naturales disponibles para criaturas. |
| `data/system/weapon-technique-profiles.yaml` | Perfiles de técnica por arma — si la criatura tiene técnicas propias. |

---

### Contenido Tauma, Vestigos y lo Sobrenatural (Horror Cósmico)

Para módulos donde la corrupción, el Limbo o los objetos cargados son centrales, **usar exclusivamente los capítulos 11 y 12 del Corebook**. Estos archivos contienen el canon definitivo (NR, agotamiento, T.R. de Aflicción, etc.).

| Documento (en `Transcendence-publications/...`) | Qué da |
| --- | --- |
| `.../core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/01-el-limbo.md` | Reglas y lore de cómo opera la dimensión. |
| `.../core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/02-el-descubrimiento.md` | Proceso de asimilación perceptual. |
| `.../core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/03-vestigos.md` | **Reglas Definitivas:** Fatiga del patrón, NR, Categorías (Primordial, Fragmentario). |
| `.../core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/04-vinculos-y-aspectos.md` | Mutaciones físicas de los personajes. |
| `.../core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/05-entidades.md` | Comportamiento y lógica de los seres del Limbo. |
| `.../core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md` | **Ailments (Limbo):** Los peajes mentales y perceptuales del Horror Cósmico. |

**Reglas rápidas de Vestigos para módulos:**
- Los vestigos se forman donde hay creencia colectiva sostenida operando a través del Tauma base.
- Su duración y letalidad inversa: un Vestigo Primordial es devastador pero se agota rapidísimo, un Vestigo Fragmentario es débil pero dura mucho.
- Los Primordiales biológicos requieren dos condiciones simultáneas: alta concentración geológica de Tauma + conciencia colectiva sostenida.

---

### PNJs por especie (Lookup Table de Canon)

Para diseñar PNJs con coherencia interna. Usa la siguiente tabla de enrutamiento para apuntar al archivo exacto de la especie en el **Corebook** (que incluye stats, biología y herencia auditada). 

Ruta base: `Transcendence-publications/core-books/transcendence-corebook/06-species/es/`

| Especie | Archivo Exacto | Especie | Archivo Exacto |
| :--- | :--- | :--- | :--- |
| **Naghii** | `01-naghii.md` | **Ursari** | `11-ursari.md` |
| **Sauri** | `02-sauri.md` | **Luphran** | `12-luphran.md` |
| **Zarnag** | `03-zarnag.md` | **Arakhel** | `13-arakhel.md` |
| **Drakkai** | `04-drakkai.md` | **Bufoni** | `14-bufoni.md` |
| **Rokhart** | `05-rokhart.md` | **Vesper** | `15-vesper.md` |
| **Formix** | `06-formix.md` | **Lapinni** | `16-lapinni.md` |
| **Loxod** | `07-loxod.md` | **Kesh** | `17-kesh.md` |
| **Ceratox** | `08-ceratox.md` | **Talpan** | `18-talpan.md` |
| **Chelicer** | `09-chelicer.md` | **Soricin** | `19-soricin.md` |
| **Panin** | `10-panin.md` | **Yacani** | `20-yacani.md` |

Además, consultar el `Eje` correspondiente en `docs/canon/species-relations.md`:
- Antagonista territorial → Eje 1 y 5
- Guía o aliado → Eje 2
- Obstáculo ideológico → Eje 3
- Fanático del Limbo → Eje 7

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

Estos documentos son relevantes para trabajo de diseño del sistema (Reglamento Core y Expansiones), no para trabajo narrativo de módulo:

- `docs/system/technique-*.md` / `data/system/techniques.yaml` — solo si diseñas técnicas nuevas (las criaturas deberían usar habilidades simples, no técnicas complejas de jugador a menos que sean campeones).
- `docs/canon/species/*/technique-seeds.md` — trabajo obsoleto o semilla, usar el *Corebook*.
- Archivos `.md` de `docs/system/` que han sido superados por el *Corebook* (ej: `limbo-entities.md`, `creatures.md`, `ailments.md`).
- `docs/adr/system-*.md` — decisiones de arquitectura del sistema.
- `docs/knowledge/` — gobernanza interna del repo.
