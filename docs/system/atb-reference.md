# ATB Reference Sheet

**Purpose:** Quick reference for running combat with the ATB timeline.
**Use for:** Table play, encounter prep, GM reference, system reminders
**Related document:** `docs/adr/combat-atb-timeline.md`

---

## 1. Qué es el ATB

El combate en Transcendence no se divide en rondas.

En su lugar, cada criatura, sistema o elemento importante del encuentro ocupa una posición en un **track circular continuo**. Hay un **marcador de flujo** que representa el presente absoluto del combate. La entidad cuya ficha esté más próxima al marcador es la siguiente en actuar.

Cuando una entidad actúa, su ficha se aleja del marcador según el costo de ritmo de la acción elegida. El marcador avanza inexorablemente hasta la siguiente ficha más próxima, que se activa a continuación.

> **Regla de posición:** La ficha más próxima al marcador de flujo actúa primero. Actuar aleja la ficha del marcador.

---

## 2. Posición inicial en el track

Al comienzo del combate, el Narrador establece la posición inicial de cada entidad en tres pasos.

### Paso 1 — Valor de Apertura

Cada participante calcula su puntuación individual:

Valor de Apertura = **Preparación** + modificadores de situación

### Paso 2 — Punto de Referencia

El Narrador identifica el Valor de Apertura más alto entre todos los participantes. Ese es el **Punto de Referencia** del encuentro.

### Paso 3 — Posición inicial

Posición inicial = Punto de Referencia − Valor de Apertura

El participante con el Valor de Apertura más alto queda en la posición **0** — el extremo izquierdo del track — y actúa primero. Los demás quedan a la derecha, a una distancia igual a la diferencia entre el Punto de Referencia y su propio Valor de Apertura.

### Modificadores de situación

El Narrador asigna estos modificadores según la ficción de la escena. Los valores de la tabla son sugeridos — no son fijos.

| Situación | Modificador sugerido |
| --- | --- |
| Emboscando | +2 |
| Arma lista / postura preparada | +1 |
| Cobertura o posición dominante | +1 |
| Objetivo expuesto o distraído | +1 |
| Sorprendido | −2 |
| Desenfundando o reorganizándose | −1 |
| Terreno inmediato malo | −1 |
| Dormido, herido, desorientado o mal posicionado | −1 a −3 según el caso |

#### Ejemplo

Un lobo con Preparación 5 embosca (+2). Valor de Apertura = 7. Tres jugadores tienen Preparación 4, 3 y 2 sin modificadores. Punto de Referencia = 7.

| Participante | Preparación | Modificadores | Valor de Apertura | Posición inicial |
| --- | ---: | ---: | ---: | ---: |
| Lobo | 5 | +2 | 7 | 7 − 7 = **0** |
| Jugador C | 4 | 0 | 4 | 7 − 4 = **3** |
| Jugador A | 3 | 0 | 3 | 7 − 3 = **4** |
| Jugador B | 2 | 0 | 2 | 7 − 2 = **5** |

El lobo actúa primero. Tras una acción estándar (costo 5), su ficha se mueve a 5. El Jugador C en posición 3 actúa a continuación.

> **Posición inicial:** No es un sistema aparte del track — es el estado de partida. Los costos de ritmo se acumulan sobre ella desde la primera activación.

---

## 3. Qué representa una ficha

Una ficha en el track representa el momento en que una entidad estará lista para volver a actuar.

Puede representar:

- un personaje
- una criatura
- un campeón
- un boss
- un subsistema del encuentro
- una amenaza ambiental importante

---

## 4. Cómo se resuelve una activación

Cuando una ficha es la más a la izquierda:

1. esa entidad actúa
2. resuelve su acción
3. mueve su ficha a la derecha según el costo de ritmo
4. se vuelve a revisar cuál es ahora la ficha más a la izquierda

---

## 5. Desempates

Si dos o más fichas quedan en la misma posición — al inicio o durante el combate —:

- actúa primero quien tenga mayor **Preparación**

Si también empatan en Preparación bruta:

- **PNJ contra PJ:** el Narrador decide quién actúa primero.
- **PJ contra PJ:** los jugadores deciden el orden entre sí.

---

## 6. Costos de ritmo

Cada acción significativa tiene un **costo de ritmo**.

Ese costo representa cuánto retrasa la siguiente oportunidad de actuar.

### Bandas de ritmo

| Banda | Costo | Efecto en el tempo |
| --- | ---: | --- |
| Acción libre | 0 | No mueve la ficha |
| Acción rápida | 3 | La ficha vuelve pronto |
| Acción estándar | 5 | Retraso normal |
| Acción pesada | 7 | Otros actúan antes de tu recuperación |
| Acción extrema | 9 | Reservada para habilidades mayores — no se usa en el nivel base |

Los valores intermedios también son válidos cuando una acción o Técnica cae entre
dos anclas de sensación real, por ejemplo `6` entre estándar y pesada.

### Acciones base universales

| Acción | Costo de ritmo | Desgaste |
| --- | ---: | ---: |
| Acción libre (soltar, hablar) | 0 | 0 |
| Interactuar | 3 | 1 * |
| Moverse | 5 | 1 |
| Ocultarse | 6 | 1 |
| Usar Especialización | 4 | 1 |
| Atacar con arma natural | 6 | 1 |
| Atacar con arma a una mano | 6 | 1 |
| Atacar con arma a dos manos | 7 | 1 |
| Atacar con dos armas a una mano | 8 | 1 |

\* Solo cuando la interacción es significativa y ocurre bajo presión real.

> **Regla estructural de Desgaste:** las acciones base bajo presión suelen partir de `1` Desgaste, pero el costo de ritmo y el Desgaste no escalan de forma automática ni idéntica. Las Técnicas pueden subir, bajar o redistribuir esa relación cuando su identidad lo justifique.

---

## 7. Ritmo y Desgaste

Toda acción importante puede tener dos costos distintos:

### Costo de ritmo

Cuánto se mueve tu ficha en el track.

### Costo de Desgaste

Cuánta carga acumulada genera la acción.

Una acción puede ser:

- rápida pero muy exigente
- lenta pero poco agotadora
- rápida y eficiente si el personaje la domina bien

> **Ritmo y desgaste:** La exigencia de una acción afecta tanto el ritmo como el Desgaste, pero no siempre en la misma medida.

---

## 8. Reacciones

Las reacciones existen dentro del ATB, pero no son gratis.

Una reacción es una acción que se permite por una condición o disparador, aunque no sea tu próxima activación natural.

Una reacción sigue teniendo costo de ritmo, puede generar Desgaste y no es gratuita solo por ser reactiva.

> **Reacciones dentro del sistema:** Una reacción se permite por su disparador, no porque esté fuera del sistema de ritmo.

---

## 9. Amenazas importantes: telegraph → ventana → resolución

Las amenazas grandes deberían funcionar, cuando sea posible, en tres momentos:

### 1. Telegraph

La amenaza se vuelve visible.

Ejemplos:

- la garganta se llena de escarcha
- el campeón se prepara para rugir
- el suelo empieza a resquebrajarse

### 2. Ventana de respuesta

Los jugadores pueden:

- moverse
- cubrirse
- analizar
- interrumpir
- presionar un punto vital
- preparar una defensa

### 3. Resolución de la amenaza

La amenaza ocurre.

Esta estructura hace que el combate sea interactivo y legible.

---

## 10. Cuándo algo merece su propio track

No todo debe tener una ficha propia.

Un sistema o función del encuentro merece un track secundario si:

- genera presión real por sí mismo
- su timing importa
- los jugadores pueden interactuar con él
- sería poco claro resolverlo solo como "parte del cuerpo principal"

Ejemplos de buenos tracks secundarios:

- ciclo de aliento
- barrido de cola
- pulso de mando del campeón
- cuenta regresiva ritual
- colapso ambiental

---

## 11. Puntos vitales y ATB

Un punto vital no solo debería cambiar daño. También puede cambiar **el ritmo del encuentro**.

Un punto vital puede:

- retrasar una amenaza
- aumentar el costo de ritmo de una criatura
- debilitar una resolución
- cancelar una función
- forzar un cambio de fase
- simplificar la presión del encuentro

> **Puntos vitales y ritmo:** Si un punto vital importa, debería cambiar cómo se comporta el encuentro en el tiempo, no solo cuánto daño recibe.

---

## 12. Categorías de encuentro y capas recomendadas

### Común — capas

- **1 track principal**
- **0 a 1 tracks secundarios**
- **1 a 2 puntos vitales importantes**

### Campeón — capas

- **1 track principal**
- **1 track táctico o de liderazgo**
- **0 a 1 sistemas de apoyo**
- **1 a 3 aliados relevantes**

### Élite / Boss — capas

- **1 track principal**
- **2 a 3 tracks secundarios**
- **0 a 1 capa ambiental fuerte**
- **3 a 5 puntos vitales o sistemas importantes**

> El boss no debería sobrevivir solo por HP; debería sobrevivir porque el encuentro existe en varias capas temporales a la vez.

---

## 13. Qué hace diferente a cada categoría

### Común — identidad

Presión simple pero táctica. Debe poder leerse dentro del combate.

### Campeón — identidad

Presión distribuida. No solo es más fuerte: coordina, habilita tácticas o vuelve más peligrosos a otros.

### Élite / Boss — identidad

Presión multifrontal. El grupo pelea contra un cuerpo, sus funciones, su espacio y sus fases.

---

## 14. Competencia y ritmo

La competencia puede reducir la fricción de ciertas acciones.

Eso significa que una acción puede volverse:

- más rápida
- menos desgastante
- más estable
- o una mezcla de lo anterior

Ejemplos:

- un usuario experto de armas cortas puede atacar rápido con menor costo de ritmo
- un analista experto puede reducir el Desgaste de una lectura en combate
- un protector entrenado puede interceptar con menos castigo que otro personaje

> **Competencia y fricción:** La competencia no solo mejora tiradas; también puede volver ciertas acciones más limpias, rápidas o sostenibles.

---

## 15. Movimiento

Moverse no es gratis por defecto.

El movimiento forma parte del ritmo del combate y tiene costo según:

- distancia
- terreno
- urgencia
- condiciones
- tipo de desplazamiento

Moverse importa especialmente en un sistema donde el entorno presiona, los telegraphs importan y los puntos vitales requieren ángulos o ventanas.

---

## 16. Lectura rápida del combate en mesa

Cuando mires el track, pregúntate:

### 1. ¿Quién actúa ahora?

La ficha más a la izquierda.

### 2. ¿Qué amenaza se está preparando?

Cualquier track secundario cercano a resolverse.

### 3. ¿Qué ventana existe?

Qué pueden hacer los jugadores antes de que esa amenaza se resuelva.

### 4. ¿Qué parte del encuentro importa más?

Qué sistema, punto vital o capa de presión debería priorizarse.

### 5. ¿Qué costo tendrá actuar así?

Tanto en ritmo como en Desgaste.

---

## 17. Mini ejemplo de track

### Estado inicial del track

| Ficha | Posición |
| --- | ---: |
| Shade | 1 |
| Bastion | 2 |
| Frost Maw | 4 |
| Mira | 5 |
| Breath Cycle | 8 |

### Qué significa este estado

- Shade actúa primero
- Frost Maw tiene una acción central en 4
- el aliento no ocurre todavía, pero ya está en el track como amenaza futura

### Secuencia de ejemplo

- Shade usa acción rápida → se mueve a 3
- Bastion usa acción estándar → se mueve a 5
- Frost Maw prepara aliento → se mueve a 6
- Mira analiza la garganta → se mueve a 7
- Bastion golpea la garganta y retrasa el Breath Cycle
- el aliento sigue existiendo, pero llega más tarde o más débil

### Por qué importa este ejemplo

El boss no necesita más monstruos de relleno para sentirse activo. Su cuerpo y su sistema de aliento ya generan dos capas de presión.

---

## 18. Preguntas rápidas al diseñar un encuentro

### 1. ¿Cuál es el track principal?

[ ]

### 2. ¿Hay un sistema secundario que merezca track?

[ ]

### 3. ¿Qué punto vital altera el ritmo del encuentro?

[ ]

### 4. ¿Qué amenaza se telegraphía antes de resolverse?

[ ]

### 5. ¿Qué pasa si los jugadores la ignoran?

[ ]

### 6. ¿Qué pasa si la leen bien e interactúan correctamente?

[ ]

---

## 19. Reglas resumidas

- La ficha más a la izquierda actúa primero.
- Actuar mueve la ficha a la derecha.
- Valor de Apertura = Preparación + modificadores de situación.
- Punto de Referencia = Valor de Apertura más alto entre todos los participantes.
- Posición inicial = Punto de Referencia − Valor de Apertura.
- Mayor Valor de Apertura → posición 0 → actúa primero.
- Los costos de ritmo se acumulan sobre la posición inicial.
- No hay rondas fijas.
- Preparación bruta desempata en caso de empate. PNJ contra PJ: el Narrador decide. PJ contra PJ: los jugadores deciden.
- Reacciones también cuestan ritmo.
- Ritmo y Desgaste no son lo mismo.
- Los subsistemas importantes pueden tener su propio track.
- Los puntos vitales deben cambiar el comportamiento temporal del encuentro.
- Los bosses sobreviven por capas de presión, no solo por números.
