# Pendientes de Diseño del Sistema

**Status:** Working backlog
**Related docs:** `docs/system/wounds-and-damage.md`, `docs/system/equipment-overview.md`, `docs/system/cover-visibility-concealment.md`, `docs/system/techniques.md`

---

## Propósito

Este archivo conserva preguntas de diseño que todavía necesitan calibración, pruebas de mesa o integración con otros sistemas.

Una pregunta pendiente no significa que el sistema no tenga una regla provisional. Significa que todavía no está cerrada como regla final de publicación.

---

## Heridas y Daño

Falta decidir o calibrar:

- Plantillas concretas para enemigos con HP, zonas, partes rompibles, Durabilidad, Potencia y habilidades vinculadas.

Notas actuales:

- `wounds-and-damage.md` ya define `Funcional`, `Saturada`, `Colapsada` y Desbordamiento.
- `wounds-and-damage.md` ya define penalizadores por zona con escala basada en ranuras ocupadas.
- `wounds-and-damage.md` ya define que una Herida Crítica no fuerza `R.R.` por defecto; solo lo hace por Colapso vital, ataque/Técnica, Agravio o circunstancia extrema.
- `wounds-and-damage.md` define dos pasos de recuperación: Estabilizar (detiene deterioro, no libera ranuras) y Tratar (Descanso Completo con T.E. Medicina — libera 1 ranura estabilizada en caso de éxito). Curar ya no existe como paso separado.
- `wounds-and-damage.md` ya define ruptura de equipo: si Potencia Crítica es igual o superior a Durabilidad, rompe; si es menor, reduce `1` Durabilidad.
- `wounds-and-damage.md` ya define partes de criatura como soportes de Bloqueo, HP, Durabilidad, Potencia y habilidades vinculadas.
- La extracción de recursos de criaturas queda para su propia sección.
- Esa regla debe probarse antes de considerarse final.

---

## Impacto Crítico y Romper Partes

Falta definir:

- Qué es exactamente Potencia base en cada arma o material.
- Qué valores típicos de Durabilidad tienen partes, armaduras y equipo.
- Qué consecuencias estándar tiene romper brazo, pierna, ala, mandíbula, arma, escudo, armadura, etc.
- Cómo se preservan o destruyen recursos extraíbles de criaturas.
- Qué Técnicas pueden ampliar el rango crítico, aumentar Potencia, ignorar Durabilidad o declarar partes no obvias.

Notas actuales:

- La frecuencia crítica se valida con un dado crítico designado antes de tirar.
- La probabilidad crítica no aumenta automáticamente por tirar más dados de Impacto.
- La Potencia Crítica ya tiene multiplicadores provisionales por tipo de arma.

---

## Armaduras, Escudos y Bloqueo

La capa estructural actual de equipo ya funciona, pero hay varias tensiones de balance entre `D.R.`, `Bloqueo`, materiales y escudos que conviene revisar antes de cerrar publicación.

Nota de estado:

- `equipment-overview.md` ahora ya refleja una versión candidata de rebalanceo para esta capa.
- Lo que sigue pendiente aquí ya no es definir desde cero, sino validar si la versión candidata se sostiene en mesa o si necesita otro ajuste.

### Riesgos detectados

- `Armadura intermedia` parece demasiado eficiente respecto a `Armadura pesada`, porque conserva parte de `Evasión` y `Agilidad` mientras la diferencia de `Bloqueo base` es relativamente pequeña.
- Materiales de alta `Durabilidad` empujan demasiado el `BM`, lo que permite que piezas ligeras o intermedias de materiales muy buenos se acerquen demasiado al `Bloqueo` de categorías superiores sin pagar su costo de movilidad.
- `Escudo intermedio` parece el punto dulce más rentable porque combina bono a `D.R.`, `Cobertura Ligera` y una penalización de movimiento que puede volverse nula con competencia suficiente.
- Algunos bonos de ranura no diferencian bien entre `Intermedia` y `Pesada`, especialmente en brazales.

### Propuesta de rebalanceo pendiente

#### 1. Reforzar la identidad de `Armadura pesada`

Propuesta:

- `Ligera`: mantiene `Evasión` completa y `Agilidad` completa.
- `Intermedia`: mantiene `Agilidad` a la mitad, pero deja de conservar `Evasión` a la mitad.
- `Pesada`: recupera una porción mínima de `Evasión`, pero sigue sin usar `Agilidad`.

Versión concreta a probar:

| Armadura en la zona | Evasión aplicable | Agilidad aplicable |
| --- | --- | --- |
| sin armadura | completa | completa |
| ligera | completa | completa |
| intermedia | completa | mitad, redondeando hacia arriba, mínimo 1 |
| pesada | mitad, redondeando hacia arriba, mínimo 1 | 0 |

Objetivo:

- `Intermedia` sigue siendo la opción flexible.
- `Pesada` deja de sentirse como "peor que intermedia salvo por +2 Bloqueo base".
- `Pesada` aguanta mejor sin convertirse en evasiva.

#### 2. Bajar el peso del material en `Bloqueo`

Regla actual:

```text
BM = floor(durability / 5)
```

Problema:

- la `Durabilidad` del material está escalando demasiado cerca del corazón del `Bloqueo`, no solo en supervivencia del equipo.

Propuesta conservadora:

```text
BM = floor(durability / 10)
```

Alternativa más granular:

- `Ligera`: `BM = floor(durability / 10)`
- `Intermedia`: `BM = floor(durability / 8)`
- `Pesada`: `BM = floor(durability / 6)`

Objetivo:

- el material sigue importando
- pero la categoría de armadura vuelve a importar más
- y `Pesada` capitaliza mejor los materiales excelentes

#### 3. Recalibrar escudos

Problema principal:

- `Escudo intermedio` ofrece demasiada eficiencia acumulada si mantiene simultáneamente `D.R.`, `Cobertura Ligera` y una penalización muy fácil de anular.

Propuesta de prueba:

| Tipo de escudo | Bono a `D.R.` | Cobertura | Penalización de movimiento |
| --- | --- | --- | --- |
| ligero | `grade` | ninguna | ninguna |
| intermedio | `grade` | `Cobertura Ligera` | `grade` |
| pesado | `grade + 1` | `Cobertura Media` | `grade × 2` |

Nota:

- esta versión deja a `Pesado` como inversión real en protección
- y evita que `Intermedio` sea el mejor punto de costo-beneficio casi siempre

#### 4. Diferenciar mejor bonos por ranura

Problema:

- `Brazales intermedios` y `Brazales pesados` hoy entregan el mismo tipo de bono ofensivo.

Propuesta:

| Ranura | Ligera | Intermedia | Pesada |
| --- | --- | --- | --- |
| Brazales | bono a `S.R.` cuando forman parte de la Técnica | bono a `A.R.` en Técnicas activas | bono a `I.R.` o bono a `Bloqueo` en reacciones defensivas con brazos |

Objetivo:

- `Intermedia` = precisión ofensiva y control activo
- `Pesada` = castigo o respuesta de choque

### Orden sugerido de pruebas

1. Probar solo el cambio de `Evasión/Agilidad` por categoría.
2. Si `Pesada` sigue débil, probar el ajuste de `BM`.
3. Luego revisar escudos.
4. Por último recalibrar bonos de ranura.

### Preguntas abiertas

- ¿`Armadura intermedia` debería conservar `Evasión` completa o media?
- ¿`Pesada` se siente mejor con `media Evasión` o con más `Bloqueo base`?
- ¿el `BM` del material debe ser universal o variar según categoría?
- ¿`Escudo pesado` debería dar `Cobertura Media` y `D.R.` alto, o una de las dos?
- ¿`Brazales pesados` deben premiar `I.R.` o `Bloqueo` reactivo?

---

## Cobertura

Notas actuales:

- `cover-visibility-concealment.md` ya define que la cobertura física puede destruirse con Potencia contra Durabilidad.
- La cobertura aplica contra cuerpo a cuerpo, distancia y proyectiles si interrumpe materialmente la línea de ataque.
- Los escudos son cobertura portátil principalmente para la celda del portador.
- Cubrir a otra criatura normalmente requiere Técnica, reacción o regla específica.
- Los ataques de área pueden recibir cobertura completa, media cobertura o ninguna según geometría y ficción del efecto.

Pendiente de prueba:

- Calibrar tamaños de escudo, tamaños de criatura y cobertura resultante en mesa.

---

## Visibilidad

Notas actuales:

- `cover-visibility-concealment.md` ya define `1 metro = 1 casilla`.
- El juego permite medición flexible, pero recomienda grid cuando hay combate táctico.
- Percepción cubre todos los sentidos relevantes, no solo visión.
- Los sentidos especiales usan Percepción con bonos o excepciones propias.
- La distinción base queda en localizado / no localizado para evitar debates finos de "ver borroso".
- La oscuridad extranatural bloquea luz ordinaria y requiere luz extranatural, artefacto, Técnica o regla compatible.

Pendiente de contenido:

- Definir sentidos especiales concretos por especie y criatura.

---

## Ocultación

Este sistema necesita especial cuidado porque afecta sigilo, combate, percepción y posición táctica.

Notas actuales:

- `cover-visibility-concealment.md` ya define la acción base `Ocultarse`: Ritmo 5, Desgaste 1, con `T.E.` apropiada.
- Ocultarse requiere no estar claramente localizado por un sentido aplicable, o crear primero una oportunidad real para ocultarse.
- No existe una acción universal separada de Buscar; se usa `Percepción`, Técnica o acción específica de escena.
- Atacar desde ocultación puede dar `+3` a `T.A.` si el objetivo no detecta la acción a tiempo.
- Comprometer ocultación no revela automáticamente posición exacta.
- La detección cercana usa rango base de 10 metros, salvo sentidos especiales, Técnicas o circunstancias.
- Posición aproximada puede resolverse con `1d8` en secreto para que el jugador no sepa si la posición marcada es real o falsa.
- Habilidades y criaturas pueden declarar que ignoran ocultación bajo condiciones específicas.

Pendiente:

- Decidir si `Sigilo` existe como especialización final o si se reemplaza por otro nombre/categoría.
- Definir Técnicas que permitan atacar sin comprometer o revelar ocultación.
