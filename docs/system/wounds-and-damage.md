# Heridas y Daño

**Status:** Draft
**Authority data:** `data/system/wounds-and-damage.yaml`
**Related docs:** `docs/system/roll-types.md`, `docs/system/equipment-overview.md`, `docs/system/ailments.md`, `docs/system/attrition-fatigue.md`

---

## Propósito

Este sistema define qué ocurre después de que un ataque supera la defensa.

Transcendence separa dos superficies de daño:

- **Jugadores contra NPCs:** daño normal contra las reservas o zonas del enemigo.
- **NPCs contra jugadores:** heridas por zona, medidas por la relación entre Impacto y Bloqueo.

La intención es que los enemigos, criaturas y monstruos puedan tener estructuras propias de HP, zonas, fases, defensas y puntos vitales, mientras que los personajes jugadores registran heridas localizadas en el cuerpo. Esto evita que los jugadores dependan de una barra abstracta de vida y hace que cada golpe recibido tenga una lectura física clara.

---

## Flujo de Ataque

El flujo base de un ataque físico es:

1. El atacante declara el ataque.
2. Se resuelve la `T.A.` contra la `T.D.` del objetivo.
3. Si la `T.A.` no supera la `T.D.`, el ataque no conecta de forma efectiva.
4. Si la `T.A.` supera la `T.D.`, el atacante tira Impacto.
5. Se determina el Bloqueo aplicable.
6. El resultado se convierte en daño, herida o efecto según el tipo de objetivo.

---

## Tirada de Impacto

Cuando un ataque conecta, el atacante tira su valor de Impacto.

```text
Impacto = Rango de Competencia × Daño del arma + Característica asociada × Grado del arma
```

El Impacto representa la presión real que el golpe transmite después de haber encontrado una entrada. No es solo daño bruto: incluye masa, ángulo, técnica, grado del arma, punto de contacto y capacidad del atacante para convertir una apertura en consecuencia.

---

## Dados adicionales de Impacto

Algunas Técnicas, efectos o rasgos añaden dados adicionales a la Tirada de Impacto. Estos dados:

- Suman al Impacto total de forma normal.
- No modifican el dado crítico designado.
- No aumentan la probabilidad de Impacto Crítico.

La probabilidad crítica depende exclusivamente del dado crítico designado, que el atacante fija antes de tirar. Añadir dados adicionales aumenta el Impacto promedio sin alterar la chance de Impacto Crítico.

El tipo y cantidad de dados adicionales los define la Técnica o efecto que los otorga. Expresiones habituales: `+Xd2`, `+Xd4`, o un valor fijo equivalente. Estos dados se tiran junto con la Tirada de Impacto normal.

---

## Impacto Crítico

Un Impacto Crítico ocurre cuando el dado crítico designado de la tirada de Impacto muestra su valor máximo.

Cuando una tirada de Impacto usa varios dados, el atacante debe identificar antes de tirar cuál de ellos es el dado crítico. En mesa, lo más simple es usar un dado de color distinto. En digital, el dado puede marcarse como `crítico`, `crit`, `main` o cualquier etiqueta equivalente.

Solo ese dado valida el Impacto Crítico. Los demás dados suman Impacto normalmente, pero no pueden activar crítico por sí solos.

El valor crítico depende del dado usado por el arma:

| Dado de Impacto | Resultado crítico |
| --- | --- |
| d4 | 4 |
| d6 | 6 |
| d8 | 8 |
| d10 | 10 |
| d12 | 12 |

Esto hace que las armas con dados pequeños generen críticos con más frecuencia, mientras que las armas con dados grandes produzcan críticos menos frecuentes pero normalmente más pesados. Como solo un dado valida crítico, subir de rango aumenta el Impacto total, pero no aumenta automáticamente la probabilidad crítica.

Un Impacto Crítico representa un golpe que encontró una entrada especialmente buena: un ángulo limpio, un punto débil, una mala recuperación del objetivo, una fractura de postura, una apertura en la armadura o un contacto inesperadamente preciso.

### Qué permite un Impacto Crítico

Cuando un ataque produce un Impacto Crítico, el atacante puede acceder a efectos críticos definidos por el arma, la Técnica o el objetivo.

Por defecto, un Impacto Crítico puede permitir:

- aplicar daño crítico contra un NPC;
- intentar romper una parte, pieza de equipo o protección;
- activar una Técnica que requiera Impacto Crítico;
- aplicar una consecuencia física si el objetivo la tiene definida.

Un Impacto Crítico no debe convertirse automáticamente en una lista universal de efectos. El objetivo, el arma y la Técnica deben definir qué opciones son válidas.

---

## Potencia Crítica

La Potencia Crítica mide la capacidad del arma para romper, deformar, abrir o inutilizar una parte resistente durante un Impacto Crítico.

```text
Potencia Crítica = Potencia base × Multiplicador de Potencia del arma
```

La Potencia base proviene del material, construcción o perfil del arma. El multiplicador depende del tipo de arma y expresa cómo esa arma transmite fuerza en un crítico.

### Multiplicadores de Potencia

| Tipo de arma | Multiplicador | Uso ideal |
| --- | ---: | --- |
| Lanzas | 80% | Perforar puntos pequeños, atravesar protecciones ligeras, castigar entradas. |
| Hachas | 120% | Abrir material, partir superficies rígidas, comprometer armaduras medianas. |
| Mazas | 150% | Romper armaduras pesadas, aplastar estructuras, castigar partes resistentes. |
| Hojas largas | 100% | Cortes amplios y profundos contra superficies de resistencia media. |
| Dagas | 50% | Críticos frecuentes y precisos contra zonas vulnerables o desprotegidas. |
| Hojas cortas | 75% | Ataques rápidos con potencia moderada, útiles contra blancos blandos o expuestos. |
| Armas arrojadizas | 40% | Impactos precisos a distancia; baja capacidad de romper partes resistentes. |
| Armas a distancia | 60% | Perforación o impacto desde lejos; limitada contra estructuras duras. |
| Armas flexibles | 30% | Control, restricción y desbalance; baja capacidad de ruptura material directa. |

Estos multiplicadores no describen cuánto daño hace siempre un arma. Describen qué tan bien convierte un crítico en ruptura estructural.

---

## Romper Partes

Romper Partes es una opción estratégica disponible cuando un ataque logra un Impacto Crítico y el objetivo tiene una parte, pieza o estructura que pueda romperse.

El atacante debe declarar qué intenta romper. El objetivo debe ser algo que el ataque pueda alcanzar y afectar de forma creíble:

- arma;
- escudo;
- pieza de armadura;
- extremidad;
- mandíbula;
- cuerno;
- caparazón;
- cola;
- ala;
- articulación;
- punto vital;
- parte destructible definida por el encuentro.

### Validación de ruptura

Cuando se intenta romper una parte:

```text
Potencia Crítica >= Durabilidad del objetivo
```

Si la Potencia Crítica es igual o superior a la Durabilidad, la parte se rompe, se deshabilita o queda inutilizada según su naturaleza.

Si la Potencia Crítica es menor que la Durabilidad, la parte no se rompe, pero pierde `1` punto de Durabilidad.

Esta reducción solo ocurre cuando se está resolviendo una ruptura válida: por Impacto Crítico, por una Técnica que permita romper sin crítico, o por una regla específica del ataque. Los ataques normales no reducen Durabilidad por defecto.

| Comparación | Resultado |
| --- | --- |
| Potencia Crítica ≥ Durabilidad | La parte se rompe, se deshabilita o queda inutilizada. |
| Potencia Crítica < Durabilidad | La parte no se rompe y pierde `1` Durabilidad. |

### Equipo roto y Bloqueo

Si una pieza de equipo que aportaba Bloqueo se rompe, deja de aportar Bloqueo hasta ser reparada o reemplazada.

Cuando una zona queda sin una pieza funcional que contrarreste Impacto, el golpe se resuelve sin el Bloqueo de esa pieza. Esto puede llenar ranuras rápidamente, y es intencional: romper equipo o partes es una forma de abrir defensas que normalmente serían demasiado resistentes.

La pérdida de Durabilidad no reduce Bloqueo automáticamente salvo que otra regla lo diga. La pieza funciona hasta romperse, aunque pueda estar más cerca de fallar ante el siguiente intento de ruptura.

### Consecuencias posibles

Romper una parte puede producir una o más consecuencias, según el objetivo:

- deshabilitar una opción de ataque;
- reducir defensa o Bloqueo;
- destruir o inutilizar equipo;
- impedir una Técnica que dependía de esa parte;
- reducir movilidad;
- alterar un patrón de comportamiento;
- abrir un punto vulnerable;
- cambiar una fase del encuentro.

La ruptura también puede dañar recursos extraíbles. Si una parte se rompe de forma destructiva, puede perder valor como material, trofeo, componente o muestra.

### Límites

No todas las armas son buenas rompiendo todo.

Un arma ligera puede generar críticos con frecuencia, pero fallar contra durabilidades altas. Un arma contundente puede romper estructuras duras, pero no necesariamente producir la precisión fina de una daga. Las Técnicas pueden modificar estos límites si lo declaran explícitamente.

Un ataque no puede romper tejido blando como si fuera una estructura, salvo que la criatura tenga esa parte definida como punto vulnerable, parte destructible o estructura anatómica relevante.

---

## Partes de Criatura y Enemigos

Los enemigos no tienen que usar las mismas zonas anatómicas que un personaje jugador. Un enemigo usa las zonas que su anatomía y diseño de encuentro necesiten.

Por defecto, una criatura importante debería organizarse en **cinco lugares principales**, igual que los personajes jugadores tienen cinco zonas de equipo. Esos lugares no tienen que llamarse Cabeza, Torso, Brazos, Piernas y Pies. Pueden ser, por ejemplo:

- cráneo, mandíbula, torso, patas, cola;
- núcleo, placas dorsales, extremidades, alas, cola;
- máscara, brazos rituales, vientre, anclajes, apéndices;
- caparazón, pinzas, abdomen, patas, ojos.

Cada parte de criatura puede tener:

| Campo | Uso |
| --- | --- |
| `T.D.` | Dificultad o defensa para golpear esa parte. |
| `HP` | Reserva de daño normal de la parte. |
| `Bloqueo` | Reducción de Impacto mientras la parte esté funcional. |
| `Potencia` | Capacidad estructural ofensiva o de ruptura si esa parte se usa para atacar. |
| `Durabilidad` | Resistencia de la parte contra ruptura. |
| `habilidades vinculadas` | Ataques, Técnicas, rasgos o fases que dependen de esa parte. |

Romper una parte de criatura sirve para limitar opciones del enemigo. Esto es especialmente importante porque muchas criaturas son más fuertes que los personajes jugadores de forma directa. Los jugadores no solo reducen números: desarman patrones.

Ejemplo: si un lobo de hielo tiene una habilidad de Aliento Helado vinculada a su mandíbula, romper la mandíbula impide usar esa habilidad hasta que una regla del enemigo diga lo contrario.

Las consecuencias exactas de romper una parte dependen del bloque del enemigo. El sistema solo exige que cada habilidad importante indique qué parte la sostiene cuando esa relación sea relevante.

### Material, Potencia y Durabilidad

El daño de un arma no cambia necesariamente por su material. Un khopesh de hierro y un khopesh de adamantium pueden usar el mismo dado de daño.

La diferencia material aparece sobre todo en:

- **Potencia:** qué tan bien el objeto rompe, penetra, abre o transmite fuerza estructural.
- **Durabilidad:** qué tan difícil es romper, deformar o inutilizar ese objeto.

Por eso un arma de un material superior puede no hacer más daño base, pero sí romper mejor y resistir mucho más antes de quedar inutilizada.

Los valores concretos de Potencia y Durabilidad pertenecen al catálogo de materiales y equipo.

---

## Bloqueo

Cuando un golpe conecta contra una zona protegida, esa zona aporta Bloqueo.

```text
Bloqueo = BC + BM + CD + CO
```

Donde:

- `BC` = Bloqueo base por categoría de armadura.
- `BM` = Bono de material.
- `CD` = Competencia Defensiva con el tipo de armadura usado en la zona.
- `CO` = Calidad o grado de la pieza.

### Bloqueo base

| Armadura | BC |
| --- | ---: |
| Ligera | 2 |
| Intermedia | 4 |
| Pesada | 6 |

### Bono de material

```text
BM = floor(durabilidad / 10)
```

### Competencia Defensiva

`CD` equivale al nivel de competencia en la armadura que protege la zona golpeada:

- Armadura ligera
- Armadura intermedia
- Armadura pesada

Solo se usa si esa armadura participa realmente en absorber el impacto.

### Calidad de objeto

`CO` es el grado de la pieza, normalmente de 1 a 3.

---

## Jugadores contra NPCs

Cuando un jugador golpea a un NPC, criatura, monstruo o adversario, el ataque usa el modelo de daño del objetivo.

Por defecto:

```text
Daño efectivo = Impacto - Bloqueo del objetivo
```

Ese daño se aplica al HP, reserva, zona, punto vital, fase o subsistema que el enemigo tenga definido.

Los enemigos pueden tener:

- HP general
- HP por zona
- defensas por zona
- bloqueos específicos
- puntos vitales
- fases
- partes destructibles
- reglas especiales de vulnerabilidad

El sistema no exige que todos los enemigos usen la misma estructura. Un enemigo común puede tener HP simple; una criatura importante puede tener zonas con valores propios; un campeón puede usar puntos vitales y subsistemas de encuentro.

### Críticos contra NPCs

Cuando un jugador logra un Impacto Crítico contra un NPC, el crítico se resuelve contra el modelo del objetivo.

Un enemigo simple puede recibir daño adicional. Una criatura con zonas puede permitir romper una parte. Un campeón puede tener puntos vitales que cambian el ritmo del encuentro si se rompen o deshabilitan.

El Impacto Crítico no obliga a todos los enemigos a tener partes rompibles. Solo habilita esa opción cuando el objetivo o la escena la tienen definida.

---

## NPCs contra jugadores

Cuando un NPC golpea a un jugador, no se usa HP general. Se determina una herida en la zona impactada.

### Orden de resolución

1. Determinar zona golpeada.
2. Identificar la armadura de esa zona.
3. Resolver `T.D.` con la Agilidad aplicable a esa armadura.
4. Si el ataque conecta, tirar Impacto.
5. Calcular Bloqueo de la zona.
6. Comparar Impacto contra Bloqueo.
7. Registrar herida si corresponde.

### Críticos contra jugadores

Cuando un NPC logra un Impacto Crítico contra un jugador, no afecta por defecto ningún atributo mental ni sistema de horror. Sigue siendo una consecuencia física del golpe recibido.

El crítico se interpreta como presión física excepcional sobre la zona golpeada. Por defecto, el ataque sigue usando la relación Impacto / Bloqueo para determinar la herida. Si el NPC, la Técnica o el ataque tienen una regla crítica específica, esa regla puede:

- aumentar la severidad de la herida;
- aplicar un Agravio físico;
- dañar una pieza de equipo;
- forzar una `R.R.`;
- romper una postura o defensa activa.

Si ninguna regla específica existe, el crítico solo confirma que el golpe se resuelve con su Impacto normal y cualquier opción crítica definida para ese ataque.

Una Herida Crítica no fuerza una `R.R.` por defecto. Ya ocupa `3` ranuras y puede saturar o colapsar una zona por sí misma.

Una `R.R.` solo se fuerza si:

- la Herida Crítica causa Colapso en una zona vital, como Cabeza o Torso;
- el ataque, NPC o Técnica lo dice;
- el Agravio asociado exige una `R.R.`;
- el Narrador lo declara por una circunstancia extrema de la escena.

La `R.R.` usada por Colapso vital es una `R.R.` de Alteración, porque representa shock corporal, pérdida funcional, trauma interno o interrupción física del cuerpo.

### Relación Impacto / Bloqueo

La severidad de la herida depende de cuánto supera el Impacto al Bloqueo.

| Relación | Resultado |
| --- | --- |
| Impacto ≤ Bloqueo × 1 | Sin herida |
| Impacto > Bloqueo × 1 y < Bloqueo × 2 | Herida Leve |
| Impacto ≥ Bloqueo × 2 y < Bloqueo × 3 | Herida Grave |
| Impacto ≥ Bloqueo × 3 | Herida Crítica |

En mesa, esto se puede leer así:

- si el golpe no supera el Bloqueo, la protección absorbe la consecuencia seria;
- si lo supera una vez, deja una herida leve;
- si lo duplica, deja una herida grave;
- si lo triplica, deja una herida crítica.

---

## Ranuras de Herida

Cada zona del personaje tiene una cantidad de ranuras de herida.

| Zona | Ranuras |
| --- | ---: |
| Cabeza | 3 |
| Torso | 5 |
| Brazos | 4 |
| Piernas | 4 |
| Pies | 3 |

Cada herida ocupa ranuras según su severidad.

| Severidad | Ranuras |
| --- | ---: |
| Leve | 1 |
| Grave | 2 |
| Crítica | 3 |

Una herida siempre intenta ocupar sus ranuras completas en la zona golpeada.

Si la zona tiene suficientes ranuras libres, se marcan normalmente.

Si la zona no tiene suficientes ranuras libres, se marcan las ranuras restantes y el exceso produce **Desbordamiento**. El Desbordamiento no crea una barra de vida oculta: significa que esa zona ya no puede absorber más daño sin perder función.

En resumen:

```text
Funcional = todavía tiene al menos 1 ranura libre.
Saturada = llegó exactamente a su máximo de ranuras.
Colapsada = recibió daño que excede sus ranuras disponibles.
```

### Estados de Zona

Cada zona puede estar en uno de estos estados.

| Estado | Condición | Efecto |
| --- | --- | --- |
| Funcional | La zona tiene al menos una ranura libre. | No aplica penalizador de zona por sí misma. |
| Saturada | Todas las ranuras están llenas, pero no hubo Desbordamiento. | Aplica el penalizador de Saturación de esa zona. |
| Colapsada | Una herida no cupo completa o la zona saturada recibió otra herida. | Aplica el efecto de Colapso de esa zona y puede escalar el estado corporal. |

Las heridas individuales pueden seguir causando Agravios si una Técnica, arma, criatura o decisión del Narrador lo indica. Los Estados de Zona solo definen qué ocurre cuando el daño acumulado compromete la función de una parte del cuerpo.

Ejemplo: si el Torso tiene `4/5` ranuras ocupadas y recibe una Herida Grave, solo puede marcar `1` de las `2` ranuras nuevas. La ranura restante no cabe, produce Desbordamiento y el Torso queda Colapsado.

### Penalizador de Saturación

Cuando una zona está Saturada, su penalizador numérico base es igual a la cantidad de ranuras ocupadas en esa zona.

```text
Penalizador de Saturación = ranuras ocupadas en la zona
```

Esto hace que una zona pequeña saturada duela menos en números que una zona grande saturada, pero siga siendo seria por el tipo de función que compromete.

| Zona saturada | Ranuras ocupadas | Penalizador base |
| --- | ---: | ---: |
| Cabeza | 3 | `-3` |
| Torso | 5 | `-5` |
| Brazos | 4 | `-4` |
| Piernas | 4 | `-4` |
| Pies | 3 | `-3` |

Este penalizador solo se aplica a las tiradas y acciones que dependan claramente de esa zona. No es un penalizador universal a todo el personaje.

### Penalizadores por Zona

Los penalizadores de zona representan pérdida de función acumulada. Si un Agravio ya impone un efecto igual o más fuerte, se usa el efecto más fuerte en lugar de apilar copias idénticas.

| Zona | Saturada | Colapsada |
| --- | --- | --- |
| Cabeza | Penalizador de Saturación a `S.R.` mentales y de percepción visual/auditiva. Penalizador de Saturación a Preparación. | Aplica `Aturdido`. Además, debe superar una `R.R.` de Alteración contra la severidad de la herida que causó el Colapso o queda `Inconsciente`. |
| Torso | Penalizador de Saturación a `Tolerancia`, acciones físicas exigentes, defensas pesadas, mantener postura bajo impacto y Técnicas que comprometan el torso. | Queda `Incapacitado` hasta estabilizarse. Si la herida que causó el Colapso fue Crítica, también entra en `Agonía`. |
| Brazos | Penalizador de Saturación a `A.R.`, `I.R.` y `S.R.` físicas que dependan claramente de brazos, agarre, escudo, armas o manipulación. | Un brazo, agarre o línea de ejecución queda inutilizado. No puede usar armas a dos manos, escudo o Técnicas ligadas a esa extremidad si dependen de la parte colapsada. Puede aplicar `Impedido`. |
| Piernas | Movimiento reducido a la mitad. Penalizador de Saturación a `S.R.` físicas de Fuerza o Tenacidad que dependan de piernas: carrera sostenida, salto, carga, trepar con apoyo inferior, empujar, resistir empuje o levantarse. | No puede caminar de forma funcional sin apoyo o ayuda. No puede cargar, correr ni saltar. |
| Pies | No puede esprintar. Penalizador de Saturación a `S.R.` físicas de Agilidad que dependan de apoyo fino: equilibrio, sigilo de pisada, giros, frenado, terreno difícil, esquiva fina o cambios bruscos de dirección. | Puede moverse solo con apoyo, ayuda o una `T.E.` apropiada. Si intenta moverse bajo presión sin apoyo y falla, queda `Derribado`. |

La severidad de la `R.R.` por Colapso usa la herida que causó el Desbordamiento:

| Herida que causó Colapso | Dificultad sugerida |
| --- | --- |
| Leve | Desafiante |
| Grave | Rigurosa |
| Crítica | Exigente |

### Estados Corporales

Los Estados Corporales describen la condición general de una criatura cuando el daño ya no es solo local.

| Estado | Significado |
| --- | --- |
| Operativo | Puede actuar normalmente, con los penalizadores que tenga por zona, Agravio, Fatiga o Desgaste. |
| Incapacitado | No puede realizar acciones significativas. Puede hablar, arrastrarse, sostener algo o reaccionar débilmente solo si la ficción lo permite. |
| Inconsciente | No puede actuar ni percibir de forma útil. No puede defenderse de forma activa. |
| Agonía | Está en riesgo de morir si no recibe estabilización. No puede actuar de forma significativa. |
| Muerto | La criatura deja de ser recuperable por medios normales de escena. |

Por defecto, una zona de brazos o piernas colapsada no mata al personaje. Puede dejarlo inutilizado, derribado o incapaz de pelear, pero la muerte requiere que el daño comprometa funciones vitales, que una regla lo declare o que el Narrador y la mesa lo acepten como consecuencia directa de la ficción.

### Escalada por Desbordamiento Repetido

Si una zona ya Colapsada recibe otra herida, se resuelve así:

1. La herida se registra como presión adicional sobre la zona, aunque ya no haya ranuras libres.
2. Se aplica o refresca el efecto de Colapso de la zona.
3. Si la zona es Cabeza o Torso, el personaje debe superar una `R.R.` de Alteración contra la severidad de la nueva herida.
4. Si falla esa `R.R.`, Cabeza escala hacia `Inconsciente` y Torso escala hacia `Agonía`.
5. Si un personaje en `Agonía` recibe otra Herida Crítica en Cabeza o Torso, muere salvo que una regla específica, Técnica, intervención inmediata o decisión de mesa establezca otra salida.

Esta regla hace que las extremidades puedan perder función sin convertir cada golpe en muerte automática, mientras que Cabeza y Torso siguen siendo zonas vitales.

---

## Zonas y localización

Para ataques de NPCs contra jugadores, la localización se determina antes de resolver la defensa. Esto evita que el Narrador elija siempre la zona más castigada o más vulnerable.

La tabla actual de localización es:

| 1d100 | Zona |
| --- | --- |
| 01-04 | Cabeza |
| 05-10 | Pies |
| 11-45 | Torso |
| 46-65 | Brazos |
| 66-100 | Piernas |

Los ataques de jugadores contra NPCs no usan esta tabla por defecto. El jugador declara objetivo, intención, técnica o punto vulnerable según lo permita la escena y la información disponible.

---

## Estabilización de Heridas

Estabilizar una herida significa intervenir para que deje de producir deterioro inmediato, dolor incapacitante, pérdida de función o riesgo de empeorar durante la escena o el interludio.

Estabilizar no borra la herida. Una herida estabilizada sigue existiendo hasta que sane, reciba tratamiento prolongado o una regla específica la elimine.

Transcendence usa tres pasos distintos:

| Paso | Función | Libera ranuras |
| --- | --- | ---: |
| Estabilizar | Se aplica a una herida concreta para detener deterioro inmediato, shock activo, sangrado abierto o Colapso que sigue empeorando. | No |
| Tratar | Se aplica a una zona durante un descanso completo para atender las ranuras ocupadas que ya fueron estabilizadas. | No por sí mismo |
| Curar | Libera ranuras ocupadas como resultado de descanso completo con tratamiento exitoso. | Sí |

`Medicina` cubre estabilizar, tratar y curar daño corporal. Objetos, Técnicas o artefactos pueden modificar estas reglas desde sus propias secciones, pero no forman parte de la regla base de heridas.

Cuando una Técnica no vuelve la herida más severa pero sí la hace más difícil de
limpiar, leer o tratar, la respuesta inmediata suele resolverse con una acción
base ya existente:

- `Interactuar` cuando basta limpiar, retirar, soltar, raspar o despejar algo
  de forma práctica
- `Usar Especialización` cuando hace falta diagnóstico, tratamiento entrenado,
  contención o manejo técnico

Esto no sustituye `Estabilizar`, `Tratar` o `Curar`. Resuelve el paso previo que
devuelve la herida o la zona a un estado tratable.

### Acción requerida

Un personaje puede intentar estabilizar una criatura con una:

```text
T.E. de Medicina (Sabiduría)
```

### Dificultad

| Herida | Dificultad |
| --- | --- |
| Leve | Desafiante |
| Grave | Rigurosa |
| Crítica | Exigente |

### Herramientas necesarias

La estabilización requiere un kit médico adecuado para la severidad de la herida.

| Herida | Kit requerido |
| --- | --- |
| Leve | Básico |
| Grave | Avanzado |
| Crítica | Especializado |

Si el personaje no tiene el kit adecuado, el Narrador puede impedir la tirada, aumentar la dificultad o permitir una estabilización parcial si la ficción lo justifica.

### Tiempo requerido

| Herida | Tiempo |
| --- | --- |
| Leve | 30 minutos |
| Grave | 60 minutos |
| Crítica | 8 horas de reposo y tratamiento |

Una herida crítica no se estabiliza de forma fiable con una intervención rápida. Requiere condiciones equivalentes a un descanso completo: tiempo, seguridad relativa, herramientas apropiadas y atención sostenida.

### Resultado

En un éxito, la herida queda estabilizada. Sus efectos inmediatos dejan de empeorar y cualquier penalizador que dependa de sangrado abierto, shock activo, desgarro sin cerrar o pérdida de control puede aliviarse según la ficción.

En un fallo, la herida no queda estabilizada. El intento puede consumir tiempo, recursos o abrir una complicación si la escena sigue bajo presión.

---

## Tratamiento y Curación

Una herida puede estar en uno de estos estados de cuidado:

| Estado | Significado |
| --- | --- |
| Activa | No ha sido estabilizada. Puede seguir causando deterioro, Colapso activo, `Agonía`, sangrado, dolor incapacitante o Agravios asociados. |
| Estabilizada | Ya no empeora de forma inmediata, pero sigue ocupando ranuras y manteniendo sus consecuencias de zona. |
| Tratada | La zona que contiene esa herida fue atendida con Medicina durante un descanso completo. Puede liberar una ranura al final de ese descanso si el tratamiento fue exitoso. |
| Curada | La herida perdió una o más ranuras por recuperación. Si llega a `0` ranuras, desaparece. |

### Heridas, zonas y ranuras

Para evitar ambigüedad:

- **Herida** es el registro narrativo y mecánico de un golpe recibido.
- **Ranuras** son el daño físico ocupado por esa herida.
- **Zona** es la parte del cuerpo donde esas ranuras están marcadas.

Estabilizar se hace sobre una herida porque lo urgente es detener esa lesión concreta.

Tratar se hace sobre una zona durante descanso completo porque el cuerpo no recupera una lesión aislada en el vacío: recupera tejido, función, presión, movilidad y circulación de esa zona.

Curar es el resultado mecánico del tratamiento: se libera `1` ranura ocupada.

### Curación por ranuras

Leve, Grave y Crítica indican cuántas ranuras ocupa una herida cuando ocurre:

```text
Leve = 1 ranura
Grave = 2 ranuras
Crítica = 3 ranuras
```

La curación no depende de que la herida sea Leve, Grave o Crítica. Depende de cuántas ranuras ocupadas quedan en el cuerpo.

Por regla base:

```text
Un personaje recupera 1 ranura de herida por descanso completo con tratamiento exitoso.
```

Esa ranura se libera de una zona tratada. Debe pertenecer a una herida estabilizada. Si una herida queda con menos ranuras, su severidad efectiva baja:

| Ranuras restantes en la herida | Severidad efectiva |
| ---: | --- |
| 3 | Crítica |
| 2 | Grave |
| 1 | Leve |
| 0 | Curada |

Esto significa que una Herida Crítica no sana porque “pasó a Grave” por una regla especial. Sana porque perdió `1` ranura después de un descanso completo con tratamiento exitoso. Si tenía `3` ranuras, queda con `2`; por eso ahora se trata como Grave.

### Curación por descanso

Las heridas deben estar estabilizadas antes de poder recuperar ranuras. Una herida activa primero debe estabilizarse.

| Descanso | Puede estabilizar | Puede tratar | Puede liberar ranuras |
| --- | --- | --- | ---: |
| 30 minutos | Herida Leve | No | 0 |
| 60 minutos | Herida Grave | No | 0 |
| Descanso completo | Herida Crítica o cualquier herida estabilizada | Sí, con `Medicina` | 1 ranura por personaje tratado |

Los descansos de 30 y 60 minutos sirven para estabilizar, preparar traslado, reducir presión inmediata o mantener a una criatura funcional, pero no liberan ranuras. La recuperación real de ranuras requiere descanso completo y tratamiento.

### Tirada de tratamiento

Al tratar una zona durante un descanso completo, el personaje que atiende al paciente realiza una `T.E. de Medicina (Sabiduría)`.

La dificultad base y el kit dependen de la ranura más severa que todavía esté ocupada en esa zona:

| Ranura ocupada más severa en la zona | Dificultad | Kit requerido |
| --- | --- | --- |
| Leve | Desafiante | Básico |
| Grave | Rigurosa | Avanzado |
| Crítica | Exigente | Especializado |

Después, aumenta el `NR` según cuántas ranuras estén ocupadas en la misma zona al inicio del descanso completo.

| Ranuras ocupadas en la zona | Ajuste |
| ---: | --- |
| 1 | Sin ajuste |
| 2-3 | `+1 NR` |
| 4-5 | `+2 NR` |

Si la zona está `Colapsada`, añade otro `+1 NR`.

Esto significa que tratar una Herida Leve aislada en el torso no tiene la misma dificultad que liberar una ranura cuando el torso tiene cuatro ranuras ocupadas. La herida puede ser pequeña, pero el cuerpo está trabajando alrededor de una zona mucho más comprometida.

En un éxito, el paciente libera `1` ranura ocupada de esa zona. La ranura liberada debe pertenecer a una herida estabilizada.

En un fallo, la zona no libera ranuras. El tratamiento puede seguir contando como cuidado narrativo, pero no produce curación mecánica. Si la escena fue insegura, el Narrador puede además mantener Agravios, impedir traslado seguro o abrir una complicación.

### Elegir qué ranura se libera

Cuando hay varias heridas estabilizadas en la misma zona, el personaje que realiza el tratamiento debe declarar qué ranura intenta liberar antes de tirar.

Por defecto, solo se libera `1` ranura. Si esa era la última ranura de una herida, la herida desaparece. Si la herida conserva ranuras, su severidad efectiva baja según las ranuras restantes.

El Narrador puede exigir que primero se libere una ranura de la herida más severa si una lesión crítica está dominando la función de la zona, causando `Agonía`, manteniendo Colapso o haciendo imposible atender daño menor con seguridad.

### Ejemplos de progresión

Una Herida Leve ocupa `1` ranura. Si está estabilizada y recibe tratamiento exitoso durante un descanso completo, libera esa ranura y desaparece.

Una Herida Grave ocupa `2` ranuras. Después de un descanso completo con tratamiento exitoso, libera `1` ranura y queda como Herida Leve. Necesita otro descanso completo con tratamiento exitoso para desaparecer.

Una Herida Crítica ocupa `3` ranuras. Después de un descanso completo con tratamiento exitoso, libera `1` ranura y queda como Grave. Después de otro descanso completo con tratamiento exitoso, queda como Leve. Después de otro, desaparece.

### Efectos de tratar sin curar

Un tratamiento exitoso puede aliviar consecuencias aunque la herida no se cure todavía:

- suspender `Agonía` si la herida ya fue estabilizada;
- permitir que un personaje `Incapacitado` por shock, sangrado o dolor vuelva a estar operativo con los penalizadores de zona correspondientes;
- retirar o reducir un Agravio asociado si el Agravio permite recuperación por Medicina;
- preparar a la criatura para moverse, ser trasladada o completar un descanso sin empeorar.

El tratamiento no elimina Saturación ni Colapso por sí mismo. Esos estados cambian cuando se liberan suficientes ranuras o cuando una regla específica restaura función.

### Condiciones inseguras

Si el descanso ocurre bajo lluvia intensa, frío extremo, persecución, contaminación, falta de sueño real, movimiento forzado o amenaza constante, el Narrador puede impedir el tratamiento, aumentar dificultad o convertir el descanso en estabilización sin curación.

---

## Relación con Agravios

Las heridas son daño localizado. Los Agravios son estados perjudiciales que cambian cómo funciona una criatura.

Una herida puede causar o justificar un Agravio, pero no toda herida lo hace automáticamente.

Ejemplos:

- una herida cortante puede aplicar `Lacerado`;
- un golpe contundente a la cabeza puede justificar aturdimiento o desorientación;
- una perforación contaminada puede abrir riesgo de Infección;
- una fractura o aplastamiento puede justificar una Alteración física.

Las Técnicas deben declarar explícitamente cuándo una herida aplica un Agravio, aumenta severidad, ignora parte del Bloqueo o modifica ranuras.

---

## Preguntas abiertas

- ¿Algunos rasgos de criatura deberían ignorar, suavizar o alterar Saturación y Colapso de zona?
