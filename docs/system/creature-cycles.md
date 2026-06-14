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

Los ciclos autónomos aparecen principalmente en:

- **Criaturas Elite** durante sus fases de Metamorfosis — habilidades recurrentes vinculadas a un Punto Vital que se activan en paralelo al turno principal de la criatura
- **Efectos ambientales activos** generados por un encuentro — clima, terreno inestable, anomalías, o condiciones ambientales que tienen efectos propios en el campo de batalla
- **Habilidades de criatura con activación independiente** — ataques, dones, o presiones que no se ejecutan en el turno principal sino en su propia ventana de Ritmo

---

## Mecánica en el ATB

- El Narrador declara la existencia de un ciclo autónomo cuando este entra por primera vez en el ATB
- El ciclo autónomo ocupa su propia posición en la línea del ATB, visible para todos los jugadores
- Su **costo de Ritmo para la próxima activación no se declara por defecto** — es información oculta hasta que el ciclo se activa o hasta que una técnica la revela
- Cuando el ciclo llega a su posición en el ATB, su efecto se ejecuta; luego inicia el siguiente paso del ciclo con un nuevo costo de Ritmo (que puede ser igual o distinto al anterior, según la criatura o efecto)
- Los jugadores pueden ver que el ciclo existe y que está en el ATB, pero no saben cuándo exactamente se activará la próxima vez

---

## Vínculo a Puntos Vitales

Los ciclos autónomos de criaturas Elite suelen estar **vinculados a un Punto Vital** (Parte Vinculada). Si ese Punto Vital es destruido:

- El ciclo autónomo se interrumpe y se retira del ATB
- Los efectos activos que generó pueden persistir según lo especificado en la criatura

---

## Diseño de ciclos para el Narrador

Al diseñar un ciclo autónomo para una criatura o encuentro, el Narrador debe definir:

- **Ritmo de cada paso** — cuánto Ritmo cuesta cada activación (puede ser constante o variable entre fases)
- **Efecto al activarse** — qué ocurre cuando el ciclo dispara
- **Condición de interrupción** — qué destruye o detiene el ciclo (normalmente un Punto Vital)
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
