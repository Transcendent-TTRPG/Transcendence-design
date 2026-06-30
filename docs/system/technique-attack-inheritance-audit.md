---
title: "Technique Attack Inheritance Audit"
type: design-audit
status: draft
purpose: >
  Audit table for chapter-09 techniques that may inherit inherent effects from
  manufactured or natural weapons. Used to normalize wording, classify
  resolution category, and identify high-risk stacking cases.
related:
  - Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/01-Como-leer-una-tecnica.md
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/docs/system/weapon-technique-profiles.md
  - Transcendence-design/docs/system/natural-attack-forms.md
---

# Technique Attack Inheritance Audit

This file is a working audit artifact, not publication-facing prose.

Its job is to answer, technique by technique:

- whether the technique resolves through a **normal attack**
- whether it instead uses a **modified normal attack**
- or whether it uses a **self-contained resolution** that should not inherit a weapon's inherent effect automatically

The publication-side rule now lives in:

- `09-techniques/es/01-Como-leer-una-tecnica.md`

---

## Categories

### `1` — Normal attack allowed

The technique enables a normal attack and leaves its resolution structurally intact.

Expected inheritance:

- inherent weapon effect **applies**

### `2` — Modified normal attack

The technique still resolves a normal attack, but adds follow-up structure:

- repositioning
- a second attack
- extra save
- movement spoil
- forced placement
- or another consequence layered on top of the normal hit

Expected inheritance:

- inherent weapon effect **applies**

### `3` — Own resolution / replacement

The technique uses a weapon, profile, or attack surface, but does **not** deliver a normal inherited attack resolution.

Expected inheritance:

- inherent weapon effect **does not apply automatically**
- if inheritance is intended, the technique should say so explicitly

---

## Scope

Included here:

- techniques in chapter 9 that perform `T.A.`
- techniques that create a counterattack
- techniques that use an attack profile or attack surface in a way that could be mistaken for inherited weapon resolution

Excluded for now:

- pure detection / posture / setup techniques that only happen to mention weapon reach
- non-offensive utility techniques that do not open the inheritance ambiguity

---

## Audit Table

| File | Técnica | Tipo | Señal de lectura actual | Propuesta inicial | ¿Hereda efecto inherente? | Prioridad | Nota |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `02-cerrar-la-linea.md` | Cerrar la Línea | Reacción - Ataque | `resuelves T.I. normalmente` + detiene movimiento | `2` | Sí | Alta | Ataque reactivo de interrupción con consecuencia extra. |
| `03-recuperar-la-distancia.md` | Recuperar la Distancia | Activo - Ataque | `resuelves T.I. normalmente` + reposicionamiento | `2` | Sí | Media | Buen candidato para wording explícito de herencia. |
| `04-clavar-el-paso.md` | Clavar el Paso | Activo - Ataque | avanza y luego `T.A.` + `resuelves T.I. normalmente` | `2` | Sí | Media | Ataque normal con reposicionamiento previo. |
| `05-anudar-el-paso.md` | Anudar el Paso | Reacción - Ataque | `resuelve la T.I. con normalidad` + fija posición | `2` | Sí | Alta | Muy clara como ataque normal modificado. |
| `06-robar-el-angulo.md` | Robar el Ángulo | Activo - Ataque | `T.A.` + desplazamiento angular; no declara `T.I. normalmente` | `3` | No automático | Alta | Ambigua; parece resolución propia montada sobre ataque. |
| `07-marcar-la-lectura.md` | Marcar la Lectura | Activo - Utilidad | `T.A.` para aplicar marca, sin `T.I.` | `3` | No automático | Media | Usa ataque como entrega, no como daño normal. |
| `08-nublar-la-senal.md` | Nublar la Señal | Activo - Utilidad | `T.A.` para fijar residuo, sin `T.I.` | `3` | No automático | Media | Resolución propia de residuo. |
| `09-doblar-el-tiro.md` | Doblar el Tiro | Activo - Ataque | `resuelves T.I. normalmente` por línea indirecta | `2` | Sí | Media | Ataque normal con geometría modificada. |
| `10-clavar-la-cadencia.md` | Clavar la Cadencia | Reacción - Ataque | `resuelves T.I. normalmente` + reducción de movimiento | `2` | Sí | Alta | Buen ejemplo de ataque normal modificado. |
| `11-tocar-y-ceder.md` | Tocar y Ceder | Activo - Ataque | `resuelves T.I. normalmente` + reposicionamiento | `2` | Sí | Media | Similar a `Recuperar la Distancia`. |
| `12-trabar-el-gesto.md` | Trabar el Gesto | Reacción - Ataque | contraataque con `T.I. normalmente` + T.R. extra | `2` | Sí | Alta | Reacción defensiva-ofensiva con stacking posible. |
| `30-cerrar-el-juicio.md` | Cerrar el Juicio | Activo - Ataque | `resuelve el daño normalmente` + objetivo de ruptura declarado | `2` | Sí | Alta | Revisar si el punto de ruptura añade demasiado encima del arma. |
| `31-barrer-la-orilla.md` | Barrer la Orilla | Activo - Ataque | `resuelve el daño normalmente` + `Desequilibrado` | `2` | Sí | Media | Ataque normal modificado bastante claro. |
| `33-cerrar-el-flanco.md` | Cerrar el Flanco | Reactivo - Ataque | reemplaza defensa + `resuelves tu daño normalmente` | `2` | Sí | Alta | Muy sensible por protección + contraataque. |
| `34-abrir-la-vasija.md` | Abrir la Vasija | Activo - Ataque | `resuelve el daño normalmente` + `Lacerado` | `2` | Sí | Media | Ver stacking con armas naturales de desgarro. |
| `35-la-corriente-no-retrocede.md` | La Corriente No Retrocede | Activo - Ataque | `resuelve el daño normalmente` + desplazamiento forzado | `2` | Sí | Media | Ataque normal modificado. |
| `36-sellar-la-presa.md` | Sellar la Presa | Activo - Ataque | `resuelve el daño normalmente` + `Derribado` | `2` | Sí | Media | Ataque normal modificado. |
| `37-devolver-al-cauce.md` | Devolver al Cauce | Reactivo - Utilidad | `T.A.` reactiva, pero no usa daño normal | `3` | No automático | Media | Usa superficie ofensiva para una resolución de control. |
| `52-ensuciar-la-herida.md` | Ensuciar la Herida | Activo - Ataque | `T.A.` exitosa aplica estado de herida ensuciada; no `T.I.` normal | `3` | No automático | Alta | Clarísimo caso de resolución propia. |
| `53-reir-en-la-brecha.md` | Reír en la Brecha | Activo - Ataque | `T.A.` exitosa aplica penalización; no `T.I.` normal | `3` | No automático | Alta | Debe quedar explícito que no hereda por defecto. |
| `54-abrir-la-costura.md` | Abrir la Costura | Activo - Ataque | `resuelve la T.I.` ignorando Bloqueo | `3` | No automático | Alta | Modifica la propia resolución del impacto. |
| `55-atajar-el-brote.md` | Atajar el Brote | Activo - Ataque | `realiza una T.I.` ignorando Bloqueo | `3` | No automático | Alta | Otro caso claro de resolución propia. |
| `56-robar-la-orilla.md` | Robar la Orilla | Activo - Ataque | `resuelve la T.I.` + reposicionamiento | `2` | Sí | Alta | Conviene normalizar a `resuelve T.I. normalmente`. |
| `59-cortar-la-mano-tarde.md` | Cortar la Mano Tarde | Reactivo - Ataque | `resuelve la T.I. con normalidad` + anula acción enemiga | `2` | Sí | Alta | Ataque reactivo muy sensible a stacking. |
| `60-encontrar-la-parte-blanda.md` | Encontrar la Parte Blanda | Activo - Ataque | `realiza una T.I.` con umbral crítico reducido | `3` | No automático | Alta | Resolución propia de letalidad. |
| `61-hacer-ceder-el-resguardo.md` | Hacer Ceder el Resguardo | Activo - Ataque | `T.A.` a estructura declarada; no `T.I. normalmente` | `3` | No automático | Alta | Mejor tratarla como ruptura propia. |
| `62-darle-a-la-pieza-util.md` | Darle a la Pieza Útil | Activo - Ataque | `T.A.` a parte del cuerpo declarada; no `T.I. normalmente` | `3` | No automático | Alta | Precisión funcional, no ataque heredado normal. |
| `71-cortar-el-paso-dos-veces.md` | Cortar el Paso Dos Veces | Reactivo - Ataque | dos ataques; `por cada ataque que impacte, resuelve T.I. normalmente` | `2` | Sí | Muy alta | Multiimpacto; revisar con prioridad. |
| `72-cerrar-la-salida.md` | Cerrar la Salida | Activo - Ataque | primer ataque `T.I. normalmente` + segunda `T.A.` + estado | `2` | Sí | Muy alta | Riesgo alto de stacking por doble ataque. |
| `73-cobrar-con-la-otra.md` | Cobrar con la Otra | Activo - Ataque | primer ataque `T.I. normalmente` + segunda `T.A.` + estado | `2` | Sí | Muy alta | Igual que `72`, pero con perfil impredecible. |
| `74-cierre-en-el-umbral.md` | Cierre en el Umbral | Reactivo - Ataque | reemplaza `T.D.`; luego contraataque / cierre | `2` | Sí | Muy alta | Contraataque reactivo; revisar wording exacto. |
| `75-el-peso-que-gira.md` | El Peso Que Gira | Activo - Ataque | `resuelve la T.I. normalmente` + reposicionamiento | `2` | Sí | Media | Ataque normal modificado. |
| `76-la-masa-continua.md` | La Masa Continúa | Activo - Ataque | `resuelve la T.I. normalmente` + `Derribado` | `2` | Sí | Media | Ataque normal modificado. |
| `77-el-cierre-que-no-se-negocia.md` | El Cierre Que No Se Negocia | Activo - Ataque | `resuelve la T.I.` ignorando Bloqueo | `3` | No automático | Alta | Resolución propia de imparable. |
| `78-el-angulo-que-falla.md` | El Ángulo Que Falla | Reactivo - Ataque | reemplaza `T.D.` + `T.I. normalmente` + segunda `T.A.` con otra arma natural | `2` | Sí | Muy alta | Uno de los casos más explosivos; revisar primero. |
| `79-la-vuelta-que-suelta.md` | La Vuelta Que Suelta | Activo - Utilidad | `T.A.` exitosa aplica `Desarmado`; sin `T.I.` normal | `3` | No automático | Media | Control puro por ataque. |
| `80-la-base-que-falta.md` | La Base Que Falta | Reactivo - Ataque | reemplaza `T.D.` + `T.I. normalmente` + `Desequilibrado` | `2` | Sí | Alta | Reacción defensiva-ofensiva con extra alteración. |
| `81-el-transito-que-no-llega.md` | El Tránsito Que No Llega | Reactivo - Utilidad | `T.A.` contra reposicionamiento; no `T.I.` normal | `3` | No automático | Media | Usa perfil ofensivo para control de tránsito. |
| `82-la-costura-que-cede.md` | La Costura Que Cede | Activo - Ataque | `resuelve tu T.I. normalmente` + falla estructural de armadura | `2` | Sí | Alta | Buen candidato para wording explícito. |
| `85-el-margen-que-se-mueve.md` | El Margen Que Se Mueve | Activo - Ataque | `T.A.` exitosa reposiciona; no `T.I.` normal | `3` | No automático | Media | Control de línea sin daño heredado normal. |
| `106-el-veredicto.md` | El Veredicto | Reactivo - Ataque | contacto automático del aguijón + `resolviendo T.I. normalmente` + Veneno | `2` | Sí | Muy alta | Natural weapon auto-contact; revisar con prioridad máxima. |
| `108-la-presa-del-oso.md` | La Presa del Oso | Activo - Ataque | `resuelve T.I. normalmente` + T.R. + `Atrapado` | `2` | Sí | Muy alta | Otro caso de especie con arma natural y efecto fuerte. |

---

## First Review Pass Targets

These should be reviewed first because they combine:

- reactive timing
- a normal inherited attack
- a second attack
- or a strong species / natural-weapon consequence

Priority set:

1. `71-cortar-el-paso-dos-veces.md`
2. `72-cerrar-la-salida.md`
3. `73-cobrar-con-la-otra.md`
4. `74-cierre-en-el-umbral.md`
5. `78-el-angulo-que-falla.md`
6. `106-el-veredicto.md`
7. `108-la-presa-del-oso.md`
8. `12-trabar-el-gesto.md`
9. `33-cerrar-el-flanco.md`
10. `59-cortar-la-mano-tarde.md`

---

## Recommended Next Step

For each row above, retroactively normalize the wording into one of these explicit formulas:

- **inherits normally**
  - `Si impacta, resuelve T.I. normalmente. Este ataque conserva los efectos inherentes del arma usada.`
- **inherits normally with extra structure**
  - `Si impacta, resuelve T.I. normalmente. Este ataque conserva los efectos inherentes del arma usada. Luego...`
- **does not inherit automatically**
  - `Esta técnica usa el perfil/superficie del arma, pero no cuenta como un ataque normal a efectos de los efectos inherentes del arma.`

