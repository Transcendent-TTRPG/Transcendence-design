# Ciclos Autónomos

**Parent doc:** `docs/system/creatures.md`
**Related docs:** `docs/system/techniques.md`, `docs/system/ailments.yaml`
**Authority data:** pending — no YAML entry yet

---

## Definición

Un **ciclo autónomo** es una entrada adicional en el ATB, separada del turno principal de una criatura o del ambiente, que representa una habilidad recurrente, un efecto ambiental activo, o una fase de criatura que opera con su propio Ritmo independiente.

El ciclo autónomo no es una acción del Narrador en su turno de criatura. Es una pieza propia en la línea del ATB con su propio costo de Ritmo, su propio momento de activación, y su propio efecto al dispararse.

---

## Cuándo aparece

Los ciclos autónomos están disponibles para todas las categorías de criatura. El tipo varía por categoría:

- **Criaturas Comunes** — ciclos biológicos únicamente: fisiología propia, carga elemental, postura defensiva, regeneración pasiva.
- **Campeones** — ciclos biológicos y ciclos de coordinación: habilidades que modifican el comportamiento de criaturas cercanas en paralelo al turno principal.
- **Criaturas Elite** — ciclos biológicos y ciclos ambientales: procesos que modifican el campo de batalla (visibilidad, terreno, condiciones elementales).

Los ciclos ambientales generados por el encuentro — clima activo, terreno inestable, anomalías — también pueden aparecer como entradas independientes en el ATB, sin estar atados a la criatura que los originó.

---

## Mecánica en el ATB

- El Narrador declara la existencia de un ciclo autónomo cuando este entra por primera vez en el ATB
- El ciclo autónomo ocupa su propia posición en la línea del ATB, visible para todos los jugadores
- Su **costo de Ritmo para la próxima activación no se declara por defecto** — es información oculta hasta que el ciclo se activa o hasta que una técnica la revela
- Cuando el ciclo llega a su posición en el ATB, su efecto se ejecuta; luego inicia el siguiente paso del ciclo con un nuevo costo de Ritmo (que puede ser igual o distinto al anterior, según la criatura o efecto)
- Los jugadores pueden ver que el ciclo existe y que está en el ATB, pero no saben cuándo exactamente se activará la próxima vez

---

## Vínculo a zonas

Los ciclos biológicos están anclados a la **zona** que los impulsa. Cuando esa zona colapsa:

- El ciclo autónomo se interrumpe y se retira del ATB
- Los efectos activos que generó pueden persistir según lo especificado en la criatura

Los ciclos ambientales de criaturas Elite no están vinculados a ninguna zona específica — son una propiedad de la presencia de la criatura en el espacio. Persisten a través de las fases de Metamorfosis salvo que el diseño especifique lo contrario, y terminan con la derrota de la criatura.

---

## Diseño de ciclos para el Narrador

Al diseñar un ciclo autónomo para una criatura o encuentro, el Narrador debe definir:

- **Ritmo de cada paso** — cuánto Ritmo cuesta cada activación (puede ser constante o variable entre fases)
- **Efecto al activarse** — qué ocurre cuando el ciclo dispara
- **Condición de interrupción** — qué destruye o detiene el ciclo (normalmente el colapso de una zona)
- **Visibilidad inicial** — si los jugadores pueden identificar el ciclo al inicio o solo cuando se manifiesta por primera vez

---

## Dificultad de lectura

La dificultad de identificar y aislar el Ritmo de un ciclo autónomo específico no depende de la categoría de la criatura — depende de cuántos ciclos autónomos están activos simultáneamente en el ATB en ese momento.

Cuando muchos ciclos corren en paralelo, separar el patrón de uno del ruido de los demás se vuelve progresivamente más difícil. Una criatura común con muchos sistemas activos puede ser tan difícil de leer como una criatura Elite con pocos.

| Ciclos autónomos activos | Dificultad |
| --- | --- |
| 1 | Fundamental |
| 2–3 | Desafiante |
| 4–5 | Rigurosa |
| 6–7 | Exigente |
| 8+ | Extrema |

Esta escala aplica como umbral para la T.E. que intenta leer un ciclo. El Narrador no tira — la dificultad es fija en el momento del intento.

## Relación con Técnicas

La Técnica **Medir el Ciclo** (Astronomía — Novato) permite a un usuario determinar el costo de Ritmo de las próximas N activaciones de un ciclo autónomo visible, donde N es el rango actual de Astronomía del usuario. La dificultad de la tirada se establece por la tabla anterior.
