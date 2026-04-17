# Desgaste, Aguante y Fatiga

**Status:** Adopted (structural model)
**Calibration status:** Initial numeric baseline adopted; further tuning open
**Related systems:** Combat, ATB, Vigor, Tenacity, Conditions, Environmental Pressure, Enemy Readability

---

## Propósito del sistema

El sistema de **Desgaste, Aguante y Fatiga** existe para modelar el costo real de sostener acciones significativas bajo presión. Su función no es reemplazar el daño ni duplicar el orden de activación del combate, sino representar algo distinto: la carga acumulada que un personaje soporta al actuar de forma eficaz en una situación hostil.

En Transcendence, el combate no está diseñado como una secuencia de intercambios triviales hasta vaciar una barra de vida. Los encuentros importantes buscan que los personajes observen, interpreten, reaccionen, neutralicen amenazas y tomen decisiones de prioridad. Por ello, el sistema necesitaba una forma de modelar no solo el castigo por recibir daño, sino también el costo de sostener rendimiento físico, mental y anímico a lo largo de una escena. Los playtests del Ice Wolf confirmaron precisamente esa necesidad: la Fatiga debía aparecer **después** de que la lógica principal del enemigo se volviera accionable, pero **antes** de que la amenaza ya estuviera completamente resuelta.

Este sistema se articula alrededor de tres conceptos:

- **Desgaste**, la carga acumulada durante la escena
- **Aguante**, la capacidad del personaje para soportar esa carga
- **Fatiga**, el deterioro progresivo que aparece cuando el Desgaste supera lo que el personaje puede sostener

---

## Relación con el combate y con el ATB

El sistema de Desgaste no sustituye al ATB ni cumple la misma función.

- El **ATB** determina **cuándo** puede actuar una criatura.
- El **Desgaste** determina **cuánto tiempo puede sostener** un rendimiento relevante antes de deteriorarse.
- La **Fatiga** expresa las consecuencias de exceder ese margen.

Esta separación es intencional. Un personaje puede actuar rápido y con frecuencia, pero no necesariamente sostener ese ritmo durante mucho tiempo. Del mismo modo, una acción mental o social en combate puede no mover el cuerpo tanto como una carga o una embestida, pero sí exigir foco, compostura y procesamiento bajo amenaza real. Por eso, el sistema no entiende el esfuerzo únicamente como cansancio muscular: entiende el combate como sobrecarga funcional.

---

## Desgaste

El **Desgaste** es la carga acumulada que un personaje soporta al ejecutar acciones significativas bajo presión.

No representa daño físico directo, ni un recurso mágico, ni un simple contador de cansancio. Representa el esfuerzo real de seguir operando con efectividad mientras el cuerpo, la mente y la compostura están siendo exigidos a la vez.

El Desgaste puede provenir de:

- acciones corporales exigentes
- lectura táctica bajo amenaza
- análisis o interpretación en medio del combate
- presión emocional o imposición social en una escena hostil
- respuesta a telegraphs, interrupciones o maniobras coordinadas
- condiciones persistentes y presión ambiental

En este sistema, lo que genera Desgaste no es el atributo involucrado por sí solo, sino la **relevancia funcional y la exigencia real** de la acción dentro de la escena.

### Qué acciones generan Desgaste

Generan Desgaste las acciones que:

- compiten tácticamente con atacar, defenderse, moverse o controlar
- alteran de forma real el estado del combate
- exigen atención, precisión, control o decisión bajo presión
- fuerzan al personaje a sostener rendimiento en un entorno hostil

Esto incluye tanto acciones físicas como mentales o sociales, siempre que sean significativas en la situación actual.

### Qué acciones normalmente no generan Desgaste

No deberían generar Desgaste, salvo regla especial, las acciones triviales o puramente narrativas que no imponen una exigencia real de escena. Por ejemplo:

- una observación obvia sin riesgo
- una frase breve sin peso táctico
- una interacción menor sin presión
- movimiento irrelevante en una pausa sin amenaza

---

## Aguante

El **Aguante** es el atributo derivado que representa cuánta carga acumulada puede absorber un personaje antes de comenzar a sufrir Fatiga.

No es una característica base independiente. Es el resultado de una **reserva mínima universal** más la resistencia corporal del personaje y su desarrollo en **Vigor**.

### Reserva Base de Aguante

Todo personaje posee una **Reserva Base de Aguante de 3**.

Esta reserva representa la capacidad mínima de seguir operando bajo presión en tres planos fundamentales del conflicto:

- **cuerpo**
- **mente**
- **compostura**

Estos tres planos justifican el valor base común del sistema:

- el **cuerpo** permite sostener esfuerzo, impacto y movimiento
- la **mente** permite mantener atención, lectura e interpretación en medio del caos
- la **compostura** permite conservar control, intención y presencia bajo tensión

La Reserva Base no pretende reflejar entrenamiento, sino la capacidad mínima de funcionamiento de cualquier personaje jugable que puede entrar en una escena de conflicto y seguir actuando.

### Relación con Tenacidad y Vigor

A la Reserva Base se suman dos fuentes propias del personaje:

- **Tenacidad**, que expresa su resistencia física real
- **Rango de Vigor**, que expresa su grado de entrenamiento para sostener esfuerzo continuado

Esto conserva el papel central de Vigor dentro del sistema. Vigor no solo mejora las pruebas ligadas al esfuerzo corporal, sino que además incrementa la capacidad total de soportar Desgaste. Esto es coherente con la creación de personaje ya adoptada: todo personaje comienza con **Vigor Nivel 1 / Rango 1**, y esa especialización inicial incrementa su Tenacidad mediante Sinapsis.

### Fórmula de Aguante

**Aguante = 3 + Tenacidad + Rango de Vigor**

### Interpretación práctica

Con esta fórmula:

- un personaje mínimo, con **Tenacidad 1** y **Vigor Rango 1**, comienza con **Aguante 5**
- una especie con bonificación adicional a Tenacidad eleva ese valor desde el inicio
- personajes que desarrollen más Vigor o Tenacidad aumentarán su capacidad de absorber Desgaste antes de entrar en Fatiga

Esto encaja con la hipótesis de trabajo ya respaldada por los playtests: la primera Fatiga en combates relevantes debe aparecer después de varias acciones significativas, no inmediatamente, y todavía con la amenaza activa.

---

## Vigor

**Vigor** es una especialización física asociada a **Tenacidad**. Representa entrenamiento del esfuerzo, resistencia prolongada, adaptación corporal y capacidad de sostener actividad exigente en condiciones adversas.

No es una simple medida abstracta de "stamina". Es una especialización real que se ejecuta y progresa dentro del sistema.

### Qué cubre Vigor

Vigor se usa en situaciones como:

- cargar o sostener peso
- resistir marcha o esfuerzo prolongado
- soportar ambientes hostiles
- mantener actividad física en condiciones adversas
- seguir operando cuando el cuerpo ya está siendo exigido de forma seria

### Rol doble de Vigor

Vigor cumple dos funciones estructurales:

1. mejora directamente las pruebas relacionadas con sostener esfuerzo físico
2. alimenta el eje de Aguante y Fatiga

Esto está alineado con la lógica general de Sinapsis: las características no suben de forma separada, sino a través de la práctica de especializaciones relevantes. Vigor es precisamente la especialización que permite que el personaje aumente su Tenacidad al exponerse una y otra vez a pruebas de esfuerzo significativo.

### Regla inicial universal

Todo personaje comienza con:

- **Vigor Nivel 1**
- **Vigor Rango 1**

Esto refleja que sobrevivir en el mundo de Transcendence exige una base mínima de resistencia física y adaptación al entorno. No es un rasgo racial particular, sino una condición estructural de cualquier personaje jugable.

---

## Fatiga

La **Fatiga** es el deterioro progresivo del rendimiento causado por haber acumulado más Desgaste del que el personaje puede sostener sin consecuencias.

La Fatiga no aparece por una sola acción aislada, sino por acumulación. Su función es marcar el momento en que la escena deja de ser simplemente exigente y empieza a alterar de forma estable la capacidad funcional del personaje.

En términos de ficción, la Fatiga no representa solo cansancio físico. Representa:

- saturación corporal
- sobrecarga cognitiva
- pérdida de compostura
- dificultad creciente para sostener precisión, control y decisión

Por eso encaja con un sistema donde el conflicto no es solamente golpear, sino también leer, responder, coordinar y actuar en varios planos a la vez.

### Regla estructural de timing

La regla estructural adoptada a partir de los playtests es esta:

> **La Fatiga 1 debe aparecer después de que la lógica principal del enemigo se haya vuelto accionable, pero antes de que esa lógica haya sido completamente explotada y la amenaza ya esté colapsada.**

Esta regla es más importante que cualquier cifra concreta aislada.

---

## Umbrales de Fatiga

La Fatiga se determina comparando el **Desgaste acumulado** con el **Aguante** del personaje.

### Umbrales

- **Fatiga 0:** Desgaste menor que el Aguante
- **Fatiga 1:** Desgaste igual o mayor al Aguante
- **Fatiga 2:** Desgaste igual o mayor a 2 × Aguante
- **Fatiga 3:** Desgaste igual o mayor a 3 × Aguante

### Ejemplo

Si un personaje tiene **Aguante 5**:

- Desgaste 0–4 → sin Fatiga
- Desgaste 5–9 → Fatiga 1
- Desgaste 10–14 → Fatiga 2
- Desgaste 15+ → Fatiga 3

Este esquema mantiene la Fatiga como algo escalonado, legible y fácil de rastrear.

---

## Costos de Desgaste

El sistema usa una escala corta de costos por acción. El objetivo no es que cada maniobra del juego tenga una fórmula propia, sino clasificar la exigencia real que impone la acción en contexto.

### Escala de costos

- **0 Desgaste:** acción no significativa o puramente narrativa
- **1 Desgaste:** acción significativa estándar
- **2 Desgaste:** acción de alta exigencia
- **3 Desgaste:** acción extrema o de sobreextensión

### 0 Desgaste

Acciones sin exigencia funcional real en la escena actual.

Ejemplos:
- observación trivial
- frase breve sin impacto táctico
- gesto menor sin presión
- transición narrativa sin costo real

### 1 Desgaste

Acciones significativas normales.

Ejemplos:
- ataque estándar
- defensa o respuesta sencilla
- desplazamiento importante bajo presión
- observación activa
- lectura básica del enemigo
- uso táctico moderado de una habilidad mental o social

### 2 Desgaste

Acciones de alta exigencia.

Ejemplos:
- interceptar una carga
- proteger a otro absorbiendo presión
- analizar profundamente al enemigo en medio del caos
- maniobra de control que cambia el ritmo del combate
- acción mental/social que quita una ventaja importante
- reacción especialmente demandante

### 3 Desgaste

Acciones extremas o de sobreextensión.

Ejemplos:
- empuje decisivo cuando el personaje ya está al límite
- intervención heroica claramente por encima del ritmo normal
- respuesta que fuerza al personaje a rendir más allá de su margen seguro
- maniobra límite que el sistema quiera marcar como un esfuerzo extraordinario

---

## Acciones físicas, mentales y sociales

El sistema no divide el Desgaste por atributo, sino por exigencia funcional.

Esto significa que una acción mental o social **sí puede generar Desgaste** si en combate:

- exige foco real bajo amenaza
- altera la situación táctica
- compite con acciones de daño, control o defensa
- obliga a sostener lectura o compostura en un entorno hostil

Esto evita dos errores:

1. tratar las acciones mentales/sociales como si fueran gratuitas
2. castigar de forma artificial cualquier pensamiento o interacción menor

### Principio adoptado

> No toda acción mental o social genera Desgaste.
> Sí lo generan aquellas que producen una ventaja táctica real, exigen interpretación bajo presión o modifican el estado del combate.

---

## Reacciones y Desgaste

Las reacciones no cuestan más por ser reacciones en sí mismas. Lo que suele volverlas más costosas es que normalmente se ejecutan en contextos de alta presión y con poco margen.

Por ello:

- una reacción simple puede costar **1 Desgaste**
- una reacción exigente puede costar **2**
- una reacción límite o salvadora puede costar **3**

### Principio adoptado

> Las reacciones tienden a ser más costosas no por su categoría, sino por el nivel de exigencia que suelen implicar.

---

## Condiciones y presión ambiental

Las condiciones y el entorno pueden acelerar la llegada de la Fatiga, pero no deben reemplazar el sistema de Desgaste ni duplicar su función.

### Principio general

- una condición leve debería entorpecer primero
- una condición severa puede empezar a encarecer acciones
- la presión ambiental debe sentirse como carga persistente, no solo como color narrativo

Esto es especialmente importante porque los hallazgos del Ice Wolf mostraron que el entorno frío no puede quedarse como simple ambientación; debe contribuir a la presión del encuentro de forma real.

### Ejemplo de criterio para condiciones escaladas

Un estado como **Cold** puede funcionar así:

- **Cold I:** penaliza ligeramente, pero no aumenta Desgaste
- **Cold II:** restringe y dificulta acciones físicas, pero todavía no aumenta Desgaste por sí solo
- **Cold III:** además de sus penalizadores, hace que cada acción física significativa cueste **+1 Desgaste**

Este tipo de progresión permite que la condición primero incomode, luego limite, y finalmente acelere el colapso si no se resuelve.

---

## Categoría del encuentro y presión

La categoría del encuentro **no cambia el Aguante del personaje**.

Un personaje no aguanta más o menos porque el enemigo sea común, campeón o élite. Lo que cambia entre categorías es la **presión del encuentro**, es decir:

- cuántas fuentes de exigencia aparecen
- cuántas acciones de alta exigencia exige la situación
- cuánta presión ambiental o táctica se acumula
- qué tan difícil es conseguir una fase clara de operación con conocimiento

### Principio adoptado

- **Aguante** es un atributo del personaje
- **Desgaste** es la moneda de la escena
- **Fatiga** es la consecuencia de exceder ese margen
- la **categoría del enemigo** cambia la forma y velocidad con la que entra presión, no el umbral del personaje

Este principio es coherente con los hallazgos ya adoptados para comunes: los grupos informados pueden retrasar la Fatiga, pero no eliminar la presión mínima del encuentro.

---

## Ejemplo de personaje inicial

Personaje recién creado:

- Tenacidad 1
- Vigor Rango 1

Entonces:

**Aguante = 3 + 1 + 1 = 5**

Interpretación:

- puede sostener varias acciones significativas antes de Fatiga 1
- no es un tanque, pero tampoco colapsa en dos decisiones
- el sistema deja espacio para leer, reaccionar y empezar a explotar la lógica del enemigo antes del deterioro

Esto conversa bien con la estructura de combate validada en los playtests, donde los encuentros importantes necesitan una fase de descubrimiento útil antes de que la Fatiga empiece a dominar la escena.

---

## Resumen operativo

### Desgaste
Carga acumulada por actuar significativamente bajo presión.

### Aguante
Capacidad total del personaje para absorber Desgaste antes de sufrir Fatiga.

### Fatiga
Deterioro progresivo del rendimiento cuando el Desgaste iguala o supera el Aguante.

### Vigor
Especialización universal inicial asociada a Tenacidad, que mejora la capacidad del personaje para sostener esfuerzo y amplía su Aguante.

### Fórmulas clave

**Aguante = 3 + Tenacidad + Rango de Vigor**

| Umbral | Condición |
| --- | --- |
| Fatiga 0 | Desgaste < Aguante |
| Fatiga 1 | Desgaste ≥ Aguante |
| Fatiga 2 | Desgaste ≥ 2 × Aguante |
| Fatiga 3 | Desgaste ≥ 3 × Aguante |

---

## Decisiones adoptadas

1. El Desgaste modela esfuerzo significativo bajo presión, no solo cansancio físico.
2. El Aguante se justifica por una Reserva Base de 3 ligada a cuerpo, mente y compostura.
3. Vigor es la especialización estructural del esfuerzo y alimenta el Aguante.
4. La Fatiga aparece por hitos de Desgaste respecto al Aguante.
5. Las acciones mentales y sociales significativas en combate también pueden generar Desgaste.
6. La categoría del encuentro modifica la presión, no el umbral del personaje.
7. La primera Fatiga debe llegar después del descubrimiento útil y antes del colapso completo de la amenaza.

---

## Cuestiones aún abiertas

1. Qué penalizadores exactos aplica cada nivel de Fatiga a las distintas clases de acción.
2. Qué condiciones concretas añaden Desgaste adicional y en qué nivel.
3. Qué distribución de costos conviene para encuentros comunes, campeones y élites en términos de acciones esperadas.
4. Cómo interactúan explícitamente las maniobras de coordinación con el Desgaste grupal.
5. Qué piso mínimo de presión debe mantenerse incluso para grupos muy informados o muy bien coordinados.
