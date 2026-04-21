# Pendientes del Proyecto

Documento de trabajo para rastrear capítulos sin escribir, mecánicas prometidas y preguntas de diseño abiertas. Actualizar aquí cuando se resuelva o avance un ítem.

---

## Capítulos sin escribir (stubs conocidos)

Estos capítulos existen como carpetas vacías en el repo de publicaciones. El corebook no es utilizable hasta que estén escritos.

| Capítulo | Título | Notas |
| --- | --- | --- |
| 06 | Species | Requerido para creación de personaje — Ch05 asume que el lector ya conoce su especie |
| 07 | Backgrounds and Origins | Requerido para creación de personaje — Ch05 asume que el lector ya conoce su trasfondo |
| 09 | Techniques | Catálogo de Técnicas desbloqueables por competencia — contenido principal del capítulo |
| 10 | Equipment and Resources | — |
| 11 | Cosmic Horror and Corruption | — |
| 12 | GM Toolkit | Destino natural de reglas de escalado con NR/NRg |
| 13 | Adversaries and Bestiary | — |
| 14 | Setting and Factions | — |
| 15 | Scenarios and Adventures | — |
| 16 | Appendices | — |
| 17 | Reference Index | — |

---

## Mecánicas prometidas, no escritas

Estas mecánicas están referenciadas en el texto existente pero no tienen reglas definidas todavía. El corebook las menciona sin describirlas.

### Catálogo de Técnicas

- **Referenciado en:** `03-core-rules`, `08-conflict-and-combat/acciones.md`
- **Descripción:** Lista completa de Técnicas desbloqueables por competencia, con su tipo (Acción Activa / Reacción), costo de ritmo, Desgaste y efecto mecánico directo
- **Destino sugerido:** Cap. 09 (Techniques) o cap. dedicado dentro de Ch08

### Condiciones y presión ambiental

- **Estado:** Escrito — `03-core-rules/es/environmental-conditions.md` y `en/environmental-conditions.md`
- **Nota:** Modelo reducido a dos herramientas del Narrador (Limitar / Acelerar); Entorpecer eliminado — el NR del umbral lo reemplaza. Ver D-08 para el caso extranatural.

### Sistema de Aflicciones

- **Referenciado en:** `rolling-system-and-competencies.md` (T.R. de Aflicciones), `desgaste-aguante-fatiga.md`
- **Descripción:** Qué son las Aflicciones, cómo se aplican, cómo progresan, cómo se resuelven
- **Destino sugerido:** Cap. 11 (Cosmic Horror and Corruption) o sección dentro de Ch10

### Sistema de Maldiciones

- **Referenciado en:** `rolling-system-and-competencies.md` (T.R. de Maldiciones y Aflicciones)
- **Descripción:** Distinción entre Aflicciones y Maldiciones; mecánicas propias
- **Nota:** Puede diseñarse junto con el sistema de Aflicciones

### Lista de Rasgos de Personalidad

- **Referenciado en:** `05-character-creation` (sección de rasgos)
- **Descripción:** Lista completa de rasgos sugeridos con sus Factores e Intensidades
- **Destino sugerido:** Cap. 04 (Character Creation) o apéndice dedicado

### Penalizaciones de Fatiga 1 / 2 / 3

- **Referenciado en:** `08-conflict-and-combat/desgaste-aguante-fatiga.md` — los umbrales están definidos, los efectos no
- **Descripción:** Qué penalizaciones concretas aplica cada nivel de Fatiga asentada
- **Nota:** Pregunta de diseño abierta — ver sección siguiente

### Regla de Herramientas

- **Referenciado en:** `01-general-rules.md` — eliminado del capítulo hasta que Ch09 exista
- **Descripción:** Actividades de fabricación, reparación y refinamiento requieren herramientas específicas; uso de herramientas alternativas aumenta la dificultad de la prueba
- **Destino sugerido:** Cap. 10 (Equipment and Resources)

### Condiciones de Correr

- **Referenciado en:** `acciones.md` — tabla de terreno muestra "Velocidad al doble" sin condiciones
- **Descripción:** Restricciones o consecuencias adicionales al correr (¿no se puede atacar?, ¿T.E. requerida en terreno difícil?, ¿Desgaste adicional?)

---

## Preguntas de diseño abiertas

Decisiones que no han sido tomadas todavía. El sistema no puede estar completo hasta que estas se resuelvan.

| # | Pregunta | Contexto |
| --- | --- | --- |
| D-01 | ¿Qué efectos concretos aplica cada nivel de Fatiga? | El sistema puede escalar a 5 niveles en lugar de 3; los umbrales están definidos pero los efectos no — requiere vocabulario mecánico más amplio (condiciones, restricciones, modificadores) antes de cerrarse |
| D-02 | ¿Los ataques apuntados (aimed) se quedan dentro de las familias de arma o se vuelven una categoría de ritmo separada? | Ver open question en `combat-atb-rhythm-costs.md` |
| D-03 | ¿En qué punto el movimiento se divide en movimiento controlado vs. forzado o desesperado? | Ver open question en `combat-atb-rhythm-costs.md` |
| D-04 | ¿Los escudos se convierten en su propia familia de acción base? | Ver open question en `combat-atb-rhythm-costs.md` |
| D-05 | ¿Ciertos usos de especialización de alta demanda (fabricación compleja en combate) merecen banda Pesada en lugar de Estándar? | Ver open question en `combat-atb-rhythm-costs.md` |
| D-06 | ¿Qué restricciones tiene la acción Correr? | Referenciado en `acciones.md` sin definir |
| D-07 | ¿Cómo funcionan los combates en movimiento (pursuits, combate en desplazamiento sostenido)? | Marcha aparece como reactiva secundaria en esos escenarios; Equitación, Acrobacias y Equilibrio también son candidatas; la mecánica no existe todavía |
| D-08 | ¿Aclimatación y otras especializaciones naturales aplican igual a condiciones extranaturales? | Una tormenta elemental no es solo frío extremo — puede requerir Instinto, Resonancia o Taumaturgia; no puede cerrarse sin el sistema del Vacío — ver `data/system/environmental-conditions.yaml` |
| D-09 | ¿Cómo interactúa el uso de Tauma con las tres manifestaciones del Limbo? | ¿Necesita el practicante un flujo o vínculo, o la energía es interna? — ver `data/system/limbo-manifestations.yaml` |
| D-10 | ¿Cuál es la tasa de disipación de vestigios? | ¿Depende del material del objeto, del tiempo, de la intensidad original, de la proximidad a un vínculo? — ver `data/system/limbo-manifestations.yaml` |
| D-11 | ¿Los vínculos tienen NR? ¿Ese NR afecta los umbrales de condiciones extranaturales del área? | Parámetro del vínculo vs. parámetro del entorno — ver `data/system/limbo-manifestations.yaml` |
| E-02 | ¿Cómo se agrupan los slots internos de las criaturas por gran familia anatómica? | La lógica de zonas existe; falta taxonomía por anatomía para bestiario |
| E-06 | ¿Cómo se integra Cordura con el peto cuando el sistema de cosmic horror/corruption esté definido? | Dependencia futura del capítulo 11 |

---

## Resuelto recientemente

Para referencia — ítems que estaban abiertos y ya se cerraron.

| Fecha | Ítem | Resolución |
| --- | --- | --- |
| 2026-04 | "Basic read / understand" como acción base | Renombrado a Especialización; costo 5/1 aplicado a todo uso de especialización en escena hostil |
| 2026-04 | Desgaste de arma a dos manos y dos armas | Cambiado de 2 a 1; el ritmo 7 ya genera desventaja de cadencia suficiente |
| 2026-04 | Nombre canónico para habilidades de competencia | Adoptado: **Técnicas (ES) / Techniques (EN)** |
| 2026-04 | "Nivel de Resonancia" en fórmula T.C. | Corregido a **Nivel de Referencia (NR)**; sección NR añadida al cap. 03 |
| 2026-04 | Conflicto de costo de Movimiento | `atb-linea-de-tiempo.md` corregido — costo siempre 5, terreno no altera ritmo |
| 2026-04 | Reacciones definidas dos veces | Sección en ATB reducida a referencia; definición canónica en `acciones.md` |
| 2026-04 | Características usadas antes de definirse | Nota de forward-reference añadida al inicio de "Tipos de Tirada" en cap. 03 |
| 2026-04 | Modelo de T.D. para armadura por piezas | Cerrado como modelo híbrido: Evasión + Agilidad según zona resuelta + bloqueo por zona si el golpe conecta |
| 2026-04 | Progresión de armadura | Cerrada por tipo de armadura en `T.D` fallida con Ventaja de Aprendizaje, cuando la armadura de la zona realmente absorbe impacto |
| 2026-04 | Rol sistémico del escudo | Cerrado: el escudo aporta un bono general a `T.D.` por equipo; su competencia progresa por Técnicas y maniobras específicas |
| 2026-04 | Naturaleza de los bonos de slot | Cerrado: todos los bonos de slot son pasivos |
| 2026-04 | Fórmula base de Cordura | Cerrado provisionalmente: `Cordura = Compostura × 2` |
