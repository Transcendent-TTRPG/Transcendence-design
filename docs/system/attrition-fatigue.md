# Desgaste, Aguante y Fatiga

**Status:** Adopted (structural model)
**Calibration status:** Initial numeric baseline adopted; further tuning open
**Related systems:** Combat, ATB, Tenacity, Tenacity specializations, Conditions, Environmental Pressure, Enemy Readability

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

No es una característica base independiente. Es el resultado de una **base de tamaño** más la resistencia corporal real del personaje, expresada en **Tenacidad**.

### Base de tamaño

El Aguante parte de una base determinada por el tamaño de la criatura:

| Tamaño | Base de Aguante |
| --- | ---: |
| Pequeño | 2 |
| Mediano | 4 |
| Grande | 6 |

La mayoría de las especies jugables son Mediano (base `4`).

### Relación con Tenacidad

A la base de tamaño se suma **Tenacidad**, que expresa la resistencia física real del personaje.

La especialización inicial universal de Tenacidad sigue siendo importante, pero lo es a través de **Sinapsis**: como esa elección otorga +1 a Tenacidad desde la creación, el Aguante ya refleja indirectamente esa trayectoria sin depender de una sola especialización fija.

### Fórmula de Aguante

```text
Aguante = base de tamaño + (Tenacidad × 2)
```

### Interpretación práctica

Con esta fórmula:

- un personaje Mediano, tras recibir su Sinapsis inicial de Tenacidad (Tenacidad 2), comienza con **Aguante 8**
- una especie con bonificación adicional a Tenacidad eleva ese valor desde el inicio
- personajes que desarrollen más Tenacidad aumentarán su capacidad de absorber Desgaste antes de entrar en Fatiga

Esto encaja con la hipótesis de trabajo ya respaldada por los playtests: la primera Fatiga en combates relevantes debe aparecer después de varias acciones significativas, no inmediatamente, y todavía con la amenaza activa.

---

### Relación con la creación

Todo personaje comienza con una especialización inicial de **Tenacidad** en Nivel 1 / Rango 1:

- **Marcha**
- **Aclimatación**
- **Tolerancia**

Esto refleja que sobrevivir en el mundo de Transcendence exige alguna forma entrenada de resistencia, pero no una manifestación única e idéntica para todas las historias de personaje.

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

### Carga sostenida

La carga no usa Desgaste de escena si se está midiendo como esfuerzo prolongado de viaje, exploración o transporte. En ese caso genera Fatiga directamente por tiempo.

La capacidad de carga depende del tamaño de la criatura, Fuerza y Tenacidad.

Para evitar que un personaje con Fuerza `0` o Tenacidad `0` tenga capacidad `0`, usa valores efectivos mínimos:

```text
Fuerza efectiva = mínimo 1
Tenacidad efectiva = mínimo 1
Capacidad de carga = Fuerza efectiva × Tenacidad efectiva × multiplicador de tamaño
```

| Tamaño | Capacidad de carga |
| --- | --- |
| Diminuto | Fuerza efectiva × Tenacidad efectiva × 1 kg |
| Pequeño | Fuerza efectiva × Tenacidad efectiva × 15 kg |
| Mediano | Fuerza efectiva × Tenacidad efectiva × 35 kg |
| Grande | Fuerza efectiva × Tenacidad efectiva × 80 kg |
| Enorme | Fuerza efectiva × Tenacidad efectiva × 200 kg |
| Gigantesco | Fuerza efectiva × Tenacidad efectiva × 800 kg |

El tipo de carga se determina por el porcentaje usado de esa capacidad:

| Tipo de carga | Peso transportado |
| --- | --- |
| Ligera | Hasta 50% de la capacidad |
| Media | Más de 50% y hasta 75% |
| Pesada | Más de 75% y hasta 100% |

Fatiga por carga sostenida:

| Tipo de carga | Fatiga |
| --- | --- |
| Ligera | No genera Fatiga automática por carga. |
| Media | +1 nivel de Fatiga por cada 2 horas de carga sostenida. |
| Pesada | +1 nivel de Fatiga por cada 1 hora de carga sostenida. |

Esta Fatiga no chequea umbral de Desgaste. Es consecuencia directa de transportar carga significativa durante tiempo prolongado.

La escala normal no crea niveles por encima de Fatiga 5. Si una nueva aplicación de carga sostenida empujaría al personaje más allá de Fatiga 5, queda Inconsciente por agotamiento y debe descansar o recibir ayuda.

Esta regla mide carga sostenida durante viaje, exploración, marcha, transporte o trabajo físico prolongado. No se usa para cada asalto de combate. Una carga que supera el 100% de la capacidad no puede transportarse de forma funcional sin ayuda, equipo, Técnica, criatura de carga o una regla específica.

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
- **Fatiga 4:** Desgaste igual o mayor a 4 × Aguante
- **Fatiga 5:** Desgaste igual o mayor a 5 × Aguante

### Ejemplo

Si un personaje Mediano tiene Tenacidad 2 (**Aguante 8**):

- Desgaste 0–7 → sin Fatiga
- Desgaste 8–15 → Fatiga 1
- Desgaste 16–23 → Fatiga 2
- Desgaste 24–31 → Fatiga 3
- Desgaste 32–39 → Fatiga 4
- Desgaste 40+ → Fatiga 5

Este esquema mantiene la Fatiga como algo escalonado, legible y fácil de rastrear. Fatiga 5 es el último punto antes del colapso operativo: si una regla vuelve a añadir Fatiga cuando el personaje ya está en Fatiga 5, queda Inconsciente. No puede realizar Acciones Activas, Reacciones ni Técnicas hasta iniciar descanso, recibir ayuda o aplicar una regla específica que lo saque de ese estado.

---

## Efectos de Fatiga

Los efectos de Fatiga son **acumulativos**. Llegar a Fatiga 3 significa que el personaje carga simultáneamente con los efectos de Fatiga 1, 2 y 3. Cada nivel añade algo cualitativamente distinto; no repite más del mismo modificador.

| Nivel | Efecto |
| --- | --- |
| **Fatiga 1** | Las T.E. físicas requieren una T.R. de Tenacidad previa. Si falla, la T.E. se pierde. |
| **Fatiga 2** | Las acciones de ritmo 5 o mayor no están disponibles. |
| **Fatiga 3** | Todas las acciones no gratuitas cuestan +1 Desgaste adicional. |
| **Fatiga 4** | Las Reacciones no están disponibles. Solo se pueden usar Acciones Activas. |
| **Fatiga 5** | Las Técnicas solo resuelven su efecto primario (T.A., T.I. o efecto de utilidad base). El reposicionamiento gratuito, las Alteraciones aplicadas y el control de posición no se activan. |
| **Overflow** | **Inconsciente** — el cuerpo se apaga, el personaje pierde consciencia. Sin Acciones Activas, Reacciones ni Técnicas hasta descansar o recibir ayuda. |

### Por qué este diseño

Cada umbral cierra una capacidad concreta antes de añadir más del mismo costo. El objetivo es que cada nivel tenga su propio peso narrativo:

- **Fatiga 1** golpea primero la precisión de movimiento y ejecución especializada — lo más fino se va primero.
- **Fatiga 2** cierra el acceso a la mayoría de los ataques estándar — el personaje empieza a perder ofensiva real.
- **Fatiga 3** encarece todo — cada acción que queda disponible cuesta más.
- **Fatiga 4** elimina la capacidad reactiva — el personaje solo puede iniciar, no responder.
- **Fatiga 5** deja las Técnicas en mínimos — el gesto todavía sale, pero el cuerpo no tiene margen para el payload adicional.

---

## Costos de Desgaste

El sistema usa una escala corta de costos por acción. El objetivo no es que cada maniobra del juego tenga una fórmula propia, sino clasificar la exigencia real que impone la acción en contexto.

### Escala de costos

La escala va de 0 a 5. Los valores 4 y 5 están reservados para técnicas de rangos altos — no aparecen en técnicas Novato.

- **0 Desgaste:** acción no significativa o puramente narrativa
- **1 Desgaste:** acción significativa estándar
- **2 Desgaste:** acción de alta exigencia
- **3 Desgaste:** compromiso extremo concentrado en un solo momento
- **4 Desgaste:** más allá del margen operativo normal; técnicas de rangos Experto y Maestro
- **5 Desgaste:** límite absoluto del sistema; técnicas signature de la cúspide (Maestro y Trascendente)

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

Acciones que exigen compromiso físico, biológico o cognitivo extremo concentrado en un solo momento.

No se limitan a actos suicidas o desesperados. Desgaste 3 aplica a cualquier activación cuyo costo biológico real en ese instante es genuinamente extremo — independientemente de si el resultado es ofensivo, defensivo o metabólico.

Ejemplos:

- sobreextensión ofensiva cuando el personaje ya está al límite
- intervención heroica que ignora el margen de seguridad del cuerpo
- respuesta biológica de emergencia que fuerza al organismo a rebasar su propio estado (purga metabólica, supresión de un estado alterado)
- entrada en una configuración defensiva completa que exige máxima disposición física sostenida
- coste de activación único de una Técnica cuyo efecto continuado justifica la carga inicial extrema

### 4 Desgaste

Reservado para técnicas de rangos Experto y Maestro. Fuerza el cuerpo más allá del margen operativo que un personaje de bajo Aguante puede sostener sin consecuencias severas.

No es desesperación — es el precio físico de ejecutar maniobras que solo son sostenibles para quien ha desarrollado la resistencia necesaria. Un personaje con Aguante 8 que activa una técnica de Desgaste 4 alcanza Fatiga 1 en dos activaciones. Un personaje con Aguante 20 puede encadenar cinco antes de llegar ahí.

Ejemplos:

- técnica de alta complejidad que exige fuerza, velocidad y resistencia simultáneas durante toda su ejecución
- maniobra que altera drásticamente el estado de la escena y cuyo efecto sostenido exige el organismo esté entrenado para mantenerlo
- concentración táctica extrema bajo presión múltiple que desplaza casi toda la capacidad cognitiva disponible

### 5 Desgaste

Límite absoluto del sistema base. Reservado para técnicas signature de la cúspide — Maestro y Trascendente.

Una sola activación de Desgaste 5 consume más de la mitad del umbral de Fatiga 1 de un personaje con Aguante 8. Para un personaje con Aguante 28, equivale a menos de una quinta parte. Esta asimetría es intencional: las técnicas más extremas del sistema solo son estratégicamente viables para quienes han construido la reserva necesaria para usarlas.

Ejemplos:

- técnica definitoria que concentra el límite absoluto de una línea de competencia
- maniobra que reescribe el combate de forma total y deja al personaje sin margen para otra activación de igual peso
- intervención que solo es tácticamente sostenible si el Aguante lo permite — para quien no lo tiene, es una apuesta de una sola vez

---

## Desgaste y rango de técnica

El Desgaste de una técnica es fijo al rango de esa técnica, no al rango del personaje que la usa.

Una técnica Novato siempre cuesta Desgaste 1-2, independientemente de si la usa un Novato o un Trascendente. Una técnica de rango Maestro siempre cuesta Desgaste 4-5.

El crecimiento de Aguante vía Tenacidad — impulsado por Sinapsis al subir rangos en especializaciones de resistencia — es el mecanismo que hace que los personajes avanzados puedan sostener técnicas de alto Desgaste sin colapsar. No reduce el costo; amplía la reserva que absorbe ese costo.

Esto crea la elección táctica central del sistema: las técnicas de bajo rango son la opción eficiente cuando el personaje quiere preservar Aguante. Las de alto rango son la opción poderosa cuando la situación justifica el gasto. Ninguna familia se vuelve obsoleta — simplemente ocupan posiciones distintas en el presupuesto táctico del combate.

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

## Descanso y recuperación de Fatiga

La recuperación no es un reinicio: es el tiempo biológico que el cuerpo necesita para metabolizar el estrés extremo y recuperar margen operativo.

### Descanso Corto

Pausa breve dentro de la aventura. Solo el primer Descanso Corto después de una escena significativa reduce Fatiga asentada. Las pausas posteriores permiten tareas, pero no reducen Fatiga nuevamente hasta la próxima escena significativa.

| Duración | Recuperación de Fatiga | Ámbito | Condición |
| --- | --- | --- | --- |
| 15 minutos | −1 nivel | Un personaje | Solo si tiene Fatiga asentada 2 o inferior |
| 30 minutos | −1 nivel | Cada personaje que descanse | — |
| 60 minutos | −2 niveles | Cada personaje que descanse | — |

Con 60 minutos en condiciones favorables, el Narrador puede añadir uno de estos beneficios: −1 Fatiga adicional, 1 tarea adicional, o reducción del riesgo de evento inesperado.

### Descanso Completo

Requiere 8 horas o más en condiciones razonablemente adecuadas.

- **Fatiga asentada:** −3 niveles (−4 si las condiciones son especialmente favorables)
- **Desgaste remanente:** se reduce en `2 × Aguante`
- **Aflicciones:** −1 intensidad por Aflicción activa, por día de Descanso Completo
- **Heridas:** permite liberar 1 Ranura de Herida con T.E. Medicina exitosa (zona estabilizada)
- **Durabilidad:** hasta 5 puntos por pieza relevante con tirada de especialización exitosa

**Excepción en territorio de Primordial:** el flujo taumático organizado contrarresta la recuperación normal de Aflicciones. Ver `attrition-fatigue.yaml` → `rest_recovery.full_rest.primordial_territory_exception` para reglas exactas de Entidad/Soberano y Abismal.

### Riesgo del descanso

Descansar en zona insegura puede producir eventos inesperados. El Narrador lanza 1d100 en secreto cuando el contexto lo justifica — no como rutina.

Modificadores por duración: +0 (15 min) / +10 (30 min) / +20 (60 min) / +30 (Descanso Completo). Modificadores situacionales adicionales van de −20 (refugio seguro) a +20 (persecución activa / enemigos cercanos).

Tabla de eventos: 1–45 sin incidentes, 46–55 señal inquietante, 56–65 cambio ambiental, 66–75 incomodidad o desplazamiento, 76–85 pérdida de posición, 86–93 interrupción hostil, 94–100 evento nefasto.

---

## Ejemplo de personaje inicial

Personaje Mediano recién creado:

- Tenacidad final 2 tras aplicar la Sinapsis inicial de Tenacidad

Entonces:

```text
Aguante = 4 + (2 × 2) = 8
```

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

### Especialización inicial de Tenacidad
Toda hoja comienza con una especialización inicial de Tenacidad, elegida según la historia del personaje. Esa elección mejora la Sinapsis inicial de Tenacidad, pero no modifica la fórmula de Aguante de forma separada.

### Fórmulas clave

```text
Aguante = base de tamaño + (Tenacidad × 2)
```

| Tamaño | Base |
| --- | ---: |
| Pequeño | 2 |
| Mediano | 4 |
| Grande | 6 |

| Umbral | Condición |
| --- | --- |
| Fatiga 0 | Desgaste < Aguante |
| Fatiga 1 | Desgaste ≥ Aguante |
| Fatiga 2 | Desgaste ≥ 2 × Aguante |
| Fatiga 3 | Desgaste ≥ 3 × Aguante |
| Fatiga 4 | Desgaste ≥ 4 × Aguante |
| Fatiga 5 | Desgaste ≥ 5 × Aguante |

---

## Decisiones adoptadas

1. El Desgaste modela esfuerzo significativo bajo presión, no solo cansancio físico.
2. El Aguante se justifica por una Reserva Base de 3 ligada a cuerpo, mente y compostura.
3. La especialización inicial de Tenacidad justifica la Sinapsis temprana de Tenacidad, pero el Aguante deriva directamente de la característica resultante.
4. La Fatiga aparece por hitos de Desgaste respecto al Aguante.
5. Las acciones mentales y sociales significativas en combate también pueden generar Desgaste.
6. La categoría del encuentro modifica la presión, no el umbral del personaje.
7. La primera Fatiga debe llegar después del descubrimiento útil y antes del colapso completo de la amenaza.
8. Los efectos de Fatiga son acumulativos; cada nivel añade algo cualitativamente distinto, no más del mismo costo.

---

## Sistema psíquico: Eco, Cordura y Disonancia

El sistema físico tiene un paralelo estructural exacto para personajes humanoides con vínculos activos. Los dos tracks son independientes y se trackean por separado.

| | Físico | Psíquico |
| --- | --- | --- |
| **Acumulado** | Desgaste | Eco |
| **Reserva** | Aguante | Cordura |
| **Consecuencia asentada** | Fatiga | Disonancia |
| **Overflow** | Inconsciente | Inconsciente |

Los tracks acumulan de forma independiente — la Fatiga no afecta al Eco y la Disonancia no afecta al Desgaste. Pero el overflow en cualquiera de los dos deja al personaje **Inconsciente**: es un OR, no un AND.

---

### Eco

El **Eco** es la carga psíquica acumulada que deja en el personaje la activación de Aspectos a través de un vínculo. No representa daño: representa el residuo del vínculo presionando su realidad perceptual sobre la mente del personaje.

El costo de Eco por activación se define por cada entrada de Aspecto (paralelo al costo de Desgaste por acción). El Eco se proyecta durante la escena y se asienta cuando termina, igual que el Desgaste.

---

### Cordura

La **Cordura** representa cuánta carga psíquica acumulada puede absorber el personaje antes de empezar a sufrir Disonancia.

```text
Cordura = 3 + (Compostura × 2)
```

El valor mínimo es 3 (cuando Compostura es 0). El paralelo exacto con Aguante es intencional.

---

### Disonancia

La **Disonancia** es el deterioro progresivo de la coherencia perceptual que aparece cuando el Eco supera lo que el personaje puede sostener.

No surge por una sola activación aislada. Surge por acumulación. A medida que el Eco aumenta, la mente pierde precisión en el procesamiento de lo que percibe a través del vínculo — primero lo más fino, luego el acceso a profundidades mayores, finalmente la capacidad de integrar múltiples canales a la vez.

#### Umbrales de Disonancia

| Nivel | Condición |
| --- | --- |
| Disonancia 0 | Eco menor que la Cordura |
| Disonancia 1 | Eco igual o mayor a la Cordura |
| Disonancia 2 | Eco igual o mayor a 2 × Cordura |
| Disonancia 3 | Eco igual o mayor a 3 × Cordura |
| Disonancia 4 | Eco igual o mayor a 4 × Cordura |
| Disonancia 5 | Eco igual o mayor a 5 × Cordura |

#### Efectos de Disonancia

Los efectos son **acumulativos**, igual que los de Fatiga.

| Nivel | Efecto |
| --- | --- |
| **Disonancia 1** | Las T.E. de categoría mental y saberes requieren una T.R. de Compostura previa. Si falla, la T.E. se pierde. |
| **Disonancia 2** | Los Aspectos en etapa Grave no están disponibles, independientemente de la intensidad de Aflicción. |
| **Disonancia 3** | Todas las activaciones de Aspecto cuestan +1 Eco adicional. |
| **Disonancia 4** | Los vínculos con más de un camino quedan completamente inutilizables — ningún camino puede activarse. Los caminos inactivos de un vínculo multi-sentido siguen generando carga de Aflicción activamente; en este nivel esa carga doble no se puede sostener. Solo los vínculos de camino único siguen disponibles. |
| **Disonancia 5** | Los Aspectos solo resuelven su etapa Leve, independientemente de la intensidad de Aflicción. Los efectos de etapa Moderado y Grave no se activan. El vínculo sigue respondiendo, pero la mente no puede procesar la percepción profunda en acción. |
| **Overflow** | **Inconsciente** — el cerebro activa el corte automático para evitar daño permanente. El personaje pierde consciencia. Sin activaciones de Aspecto. Todos los vínculos suspendidos hasta descansar o recibir ayuda. Las Aflicciones registran el daño perceptual acumulado; la inconsciencia es el apagado total temporal. |

#### Lógica del diseño de Disonancia

El paralelo con Fatiga es intencional en estructura pero distinto en contenido:

- **Disonancia 1** golpea primero la precisión mental y el saber — lo más fino del procesamiento cognitivo se va primero.
- **Disonancia 2** cierra el acceso a la profundidad perceptual máxima del vínculo.
- **Disonancia 3** encarece todas las activaciones.
- **Disonancia 4** elimina la capacidad de sostener vínculos con carga dual — el personaje no puede mantener dos canales sensoriales abiertos.
- **Disonancia 5** deja los Aspectos en mínimos — el vínculo todavía responde, pero solo en su expresión más superficial.

---

## Cuestiones aún abiertas

1. Qué condiciones concretas añaden Desgaste adicional y en qué nivel.
2. Qué distribución de costos conviene para encuentros comunes, campeones y élites en términos de acciones esperadas.
3. Cómo interactúan explícitamente las maniobras de coordinación con el Desgaste grupal.
4. Qué piso mínimo de presión debe mantenerse incluso para grupos muy informados o muy bien coordinados.
5. Costo de Eco por activación de Aspecto — definir la escala (¿paralela a Desgaste 0/1/2/3 según etapa Leve/Moderado/Grave?) — ver E-05 en `limbo-entities.yaml`.
