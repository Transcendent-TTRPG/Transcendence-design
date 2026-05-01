# Cobertura, Visibilidad y Ocultación

**Status:** Draft
**Authority data:** `data/system/cover-visibility-concealment.yaml`
**Related docs:** `docs/system/environmental-conditions.md`, `docs/system/difficulty-thresholds.md`, `docs/system/roll-types.md`, `docs/system/ailments.md`

---

## Propósito

Este sistema define cómo la mesa maneja tres situaciones que suelen confundirse:

- **Cobertura:** algo físico protege el cuerpo.
- **Visibilidad:** el entorno limita lo que puede verse o distinguirse.
- **Ocultación:** una criatura no está localizada con precisión por uno o más enemigos.

La separación es importante. Una criatura puede estar detrás de una roca y tener cobertura sin estar oculta. También puede estar en niebla densa y ser difícil de distinguir sin que una pared la proteja. Y puede estar oculta detrás de una barrera aunque el entorno tenga buena luz.

---

## Cobertura

La cobertura es protección física o estructural que interfiere con una línea de ataque.

La cobertura debe ser algo que pueda bloquear, desviar, absorber o interrumpir físicamente el ataque. Niebla, humo y oscuridad no son cobertura por sí mismos: son visibilidad reducida. Pueden ayudar a ocultarse, pero no detienen un golpe.

### Niveles de cobertura

| Cobertura | Criterio | Efecto |
| --- | --- | --- |
| Ligera | Protege una parte menor del cuerpo o interfiere parcialmente la línea | `-1` a la `T.A.` del atacante |
| Media | Protege una parte importante del cuerpo, dejando aperturas claras | `-3` a la `T.A.` del atacante |
| Total | No hay línea directa de ataque hacia el objetivo | No puede ser objetivo de ataques directos |

### Cobertura ligera

El objetivo no está completamente expuesto, pero todavía puede atacarse con una línea razonable.

Ejemplos:

- mueble bajo;
- baranda;
- roca pequeña;
- tronco delgado;
- borde de una puerta;
- cobertura que protege aproximadamente un cuarto del cuerpo.

### Cobertura media

El objetivo está protegido por un obstáculo significativo, pero conserva alguna exposición.

Ejemplos:

- árbol grueso;
- roca grande;
- barricada;
- ventana o abertura;
- esquina de muro;
- cobertura que protege aproximadamente la mitad o más del cuerpo, pero no todo.

### Cobertura total

El obstáculo bloquea completamente la línea directa.

Ejemplos:

- pared sólida;
- puerta cerrada;
- trinchera sin exposición;
- estructura cerrada;
- vehículo o masa que cubre por completo al objetivo.

Un objetivo con cobertura total puede ser afectado por ataques de área, técnicas que alteran la ruta de ataque, destrucción del obstáculo, rodeo, elevación, rebote, explosión u otra ficción que permita ignorar la línea directa.

### Destruir cobertura

La cobertura física puede destruirse si el objeto que la produce tiene material, Potencia y Durabilidad.

Para romper cobertura, usa la misma regla de ruptura:

```text
Potencia Crítica >= Durabilidad del objeto
```

Si la Potencia es igual o superior a la Durabilidad, la cobertura se rompe o deja de proteger, según su naturaleza.

Si la Potencia es menor, la cobertura no se rompe, pero pierde `1` Durabilidad. Los ataques normales no reducen Durabilidad por defecto: debe existir un intento válido de ruptura, un Impacto Crítico, una Técnica o una regla específica.

### Cobertura contra tipos de ataque

La cobertura aplica contra ataques cuerpo a cuerpo, ataques a distancia y proyectiles siempre que el objeto realmente interrumpa la línea del ataque.

Si el atacante está en un ángulo donde la cobertura ya no bloquea la línea, no aplica. La cobertura es geométrica y material, no un estado fijo pegado al personaje.

### Escudos como cobertura

Los escudos son la fuente principal de cobertura portátil.

Un escudo da cobertura principalmente a la celda o espacio de su portador. Cubrir a otra criatura normalmente requiere una Técnica, una reacción de escudo o una regla que permita extender esa cobertura fuera del espacio propio.

La cobertura otorgada por escudo depende de:

- tamaño del escudo;
- tamaño del portador;
- tamaño de la criatura cubierta;
- ángulo del ataque;
- si el portador puede cargar y controlar el escudo.

Un escudo pesado puede dar muy buena cobertura a una criatura pequeña, pero el personaje quizá no pueda cargarlo o combatir con él si supera su capacidad de carga.

### Cobertura y áreas

Contra ataques de área, la cobertura solo ayuda si el objeto puede interponerse entre la criatura y el origen, dirección o expansión del efecto.

Regla simple:

| Situación | Efecto |
| --- | --- |
| La cobertura bloquea claramente el área | Aplica cobertura normal. |
| La cobertura protege parcialmente contra el área | Aplica la mitad del penalizador de cobertura, redondeando hacia abajo. |
| El área rodea, llena o ignora la cobertura | La cobertura no aplica. |

Así, una barricada puede ayudar contra una explosión frontal, pero no contra gas que llena toda la zona o fuego que cae desde arriba.

---

## Visibilidad

La visibilidad define qué tan lejos y con qué claridad una criatura puede distinguir detalles visuales.

Para medición en tablero:

```text
1 metro = 1 casilla
```

El juego puede usarse con grid o con medición flexible. El grid es recomendable cuando hay combate, áreas, cobertura, posición aproximada o movimiento táctico relevante.

La visibilidad no reemplaza el sistema de Condiciones del Entorno. Cuando una situación ya está dominada por clima, humo, oscuridad o presión ambiental, el Narrador puede usar la severidad del entorno para asignar dificultad. Esta sección sirve como referencia rápida para escenas donde la visión importa de forma concreta.

### Rango visual estándar

En condiciones claras, una criatura puede reconocer detalles relevantes hasta:

```text
Rango visual estándar = 60 metros
```

Más allá de ese rango, una acción que dependa de distinguir detalles visuales requiere una `T.E. de Percepción`. El Narrador aumenta la dificultad según distancia, tamaño, movimiento, contraste y condiciones ambientales.

Regla simple:

```text
+1 NR por cada 10 metros más allá del rango visual efectivo
```

No uses incrementos de 2 metros: producen demasiado conteo en mesa y no aportan decisiones interesantes.

---

## Rangos de Visibilidad Reducida

| Condición | Intensidad | Rango visual efectivo |
| --- | --- | ---: |
| Lluvia | Ligera | 24 m |
| Lluvia | Intensa | 15 m |
| Lluvia | Tormenta | 8 m |
| Nieve | Ligera | 24 m |
| Nieve | Intensa | 15 m |
| Nieve | Tormenta de nieve | 8 m |
| Niebla | Ligera | 20 m |
| Niebla | Densa | 10 m |
| Niebla | Espesa | 5 m |
| Humo | Leve | 20 m |
| Humo | Denso | 5 m |
| Humo | Asfixiante | 2 m |
| Polvo o arena | Leve | 25 m |
| Polvo o arena | Moderado | 12 m |
| Polvo o arena | Tormenta | 5 m |
| Oscuridad absoluta | Sin fuente de luz | 0 m |
| Oscuridad extranatural | Activa | 0 m, salvo contramedida válida |

Estos valores son guías de referencia. Si la condición ya está representada como entorno Moderado, Severo, Desastroso o Extremo, usa la severidad del entorno como autoridad principal.

---

## Fuentes de Luz

Las fuentes de luz establecen un rango visual efectivo cuando el entorno no tiene iluminación suficiente.

| Fuente | Rango claro | En condición visual densa |
| --- | ---: | ---: |
| Vela | 2 m | 1 m |
| Antorcha | 4 m | 2 m |
| Lámpara de aceite | 6 m | 3 m |

Una fuente de luz no elimina humo, niebla, polvo ni oscuridad extranatural por sí sola. Solo permite ver dentro del rango que todavía pueda atravesar.

---

## Oscuridad Absoluta y Oscuridad Extranatural

La oscuridad absoluta ocurre cuando no hay luz natural, artificial ni reflejada suficiente para ver. En esas condiciones, el rango visual es `0 m`.

La oscuridad extranatural también reduce el rango visual a `0 m`, pero no se resuelve con una fuente de luz ordinaria. La oscuridad extranatural asociada al elemento Oscuridad bloquea luz natural y fuentes comunes de iluminación.

Para contrarrestarla se necesita una fuente compatible: luz extranatural asociada al elemento Luz, artefacto, Técnica, condición ambiental opuesta o regla específica.

En ambos casos, una criatura puede seguir usando otros sentidos, memoria espacial, contacto físico, sonido, olor, vibración, señales químicas o técnicas de percepción no visual si la ficción lo permite.

### Percepción y sentidos no visuales

`Percepción` no significa solo visión. Representa la capacidad de localizar, distinguir o interpretar señales sensoriales.

Un personaje puede usar Percepción para:

- ver;
- escuchar;
- oler;
- sentir vibración;
- reconocer contacto o textura;
- leer señales químicas;
- usar ecolocalización u otro sentido especial si lo posee.

Los sentidos especiales usan la misma estructura de Percepción salvo que una regla diga otra cosa. Una criatura con un sentido especial puede tener bonificadores adicionales y no queda bloqueada por efectos que no interfieran con ese sentido.

Ejemplo: una criatura que rastrea por olor puede ignorar oscuridad visual para localizar un objetivo, pero puede sufrir penalizadores por viento, agua, humo químico o una Técnica que altere olores.

---

## Combate sin visión

Una criatura que no puede ver a su objetivo no pierde automáticamente todas sus competencias.

En su lugar:

- no puede elegir con precisión objetivos que no haya localizado;
- no puede usar técnicas que requieran lectura visual clara;
- puede atacar una posición aproximada con penalización o dificultad aumentada;
- puede defenderse peor contra amenazas que no puede leer;
- puede usar otros sentidos si son relevantes.

Para evitar discusiones finas en mesa, usa dos estados principales:

| Situación | Efecto |
| --- | --- |
| Objetivo localizado por cualquier sentido relevante | Puede ser objetivo; aplica penalización o NR solo si la señal es débil, indirecta o difícil de interpretar. |
| Objetivo no localizado | No puede ser objetivo de ataque directo |

La `T.I.` o Impacto no pierde todos sus bonos por falta de visión. Si el ataque conecta, el Impacto se resuelve normalmente salvo que una regla específica diga lo contrario.

---

## Ocultación

La ocultación es un estado táctico: una criatura no está localizada con precisión por uno o más enemigos.

No es invisibilidad, no es inmunidad y no borra evidencia física. Significa que el enemigo no sabe exactamente dónde está la criatura o no puede fijarla como objetivo directo.

### Requisitos para ocultarse

Ocultarse es una acción base cuando se realiza bajo presión.

| Acción | Ritmo | Desgaste | Tirada |
| --- | ---: | ---: | --- |
| Ocultarse | 5 | 1 | `T.E.` apropiada contra dificultad del entorno o Percepción enemiga |

Fuera de una escena hostil, Ocultarse no necesita coste de Ritmo. El Narrador solo pide la tirada si hay riesgo, oposición o consecuencia.

Una criatura puede intentar ocultarse si cumple al menos una de estas condiciones:

- tiene cobertura media o total;
- está fuera del rango visual efectivo de los enemigos relevantes;
- está dentro de una condición de visibilidad reducida que pueda ocultar su posición;
- cuenta con una técnica, rasgo, artefacto o preparación que permita ocultación.

Además, ningún enemigo relevante debe tenerla localizada claramente por un sentido aplicable. No basta con "querer desaparecer" mientras alguien la ve, oye, huele o percibe con claridad.

Si un enemigo la tiene localizada sin obstrucción, la criatura debe crear primero una oportunidad real:

- romper línea de visión;
- entrar en cobertura media o total;
- entrar en humo, niebla, oscuridad, vegetación, multitud o ruido suficiente;
- usar una distracción;
- moverse fuera del rango efectivo del sentido que la localiza;
- usar una Técnica, rasgo, artefacto o preparación que permita ocultarse aun bajo observación.

### Tirada para ocultarse

La criatura realiza una `T.E.` apropiada contra la dificultad del entorno o contra la percepción de los enemigos, según la escena.

Especializaciones típicas:

- `Sigilo` para ocultarse por silencio, control corporal y posición;
- `Supervivencia` para ocultarse en terreno natural, vegetación, clima o rastros;
- otra especialización si un rasgo, técnica o artefacto lo justifica.

La especialización exacta depende de la ficción. Ocultarse en una sala con sombras y guardias puede ser `Sigilo`; perderse en selva, lluvia o terreno rocoso puede ser `Supervivencia`; una Técnica puede autorizar otra especialización si su método lo justifica.

### Estado de ocultación

La ocultación se registra por enemigo o por grupo de enemigos.

Un personaje puede estar oculto para un guardia, pero no para otro que lo vio entrar. Puede estar oculto para criaturas que dependen de visión, pero no para una criatura que rastrea calor, olor o vibración.

### Efectos de estar oculto

Mientras una criatura esté oculta para un enemigo:

- ese enemigo no puede elegirla como objetivo de ataques directos de “una criatura”;
- puede atacar un área o posición sospechada si tiene una razón para hacerlo;
- puede buscarla activamente;
- puede reaccionar a señales obvias, ruido, contacto o cambios del entorno.

La ocultación no protege contra efectos de área que cubran la posición real.

### Atacar desde ocultación

Atacar desde ocultación puede dar una ventaja de apertura si el objetivo no reacciona a tiempo.

Antes de resolver el ataque, las criaturas relevantes dentro de **10 metros** pueden intentar detectar la acción si tienen un sentido que pueda percibirla. Usa `T.E. de Percepción` contra la ocultación activa o la dificultad del entorno.

Una criatura fuera de 10 metros solo puede intentar esta detección si tiene un sentido especial, Técnica, preparación o posición que justifique reaccionar a esa señal.

| Resultado de Percepción | Efecto |
| --- | --- |
| Falla | El ataque conserva ventaja de apertura. |
| Tiene éxito | La criatura detecta la acción a tiempo; el atacante no obtiene ventaja de apertura contra esa criatura. |

Si el ataque conserva ventaja de apertura, obtiene `+3` a la `T.A.` contra objetivos que no detectaron la acción a tiempo.

Atacar desde ocultación siempre compromete la ocultación, incluso si el ataque falla. Después del ataque, resuelve posición aproximada o detección según la escena.

---

## Mantener y perder ocultación

La ocultación se mantiene mientras la criatura no dé una señal suficiente para localizarla.

Acciones que comprometen la ocultación:

- atacar cuerpo a cuerpo;
- atacar a distancia;
- moverse entre coberturas;
- correr;
- hablar fuerte;
- manipular un objeto visible o ruidoso;
- interactuar con una fuente de luz;
- cambiar de posición en un entorno silencioso.

Comprometer la ocultación no significa revelar automáticamente la posición exacta. Significa que hay una señal suficiente para que enemigos cercanos intenten localizarla.

Cuando una criatura compromete su ocultación, las criaturas relevantes dentro de **10 metros** pueden intentar una `T.E. de Percepción` si tienen un sentido aplicable. Criaturas fuera de 10 metros necesitan un sentido especial, Técnica, preparación o circunstancia que justifique la detección.

Si nadie detecta la posición exacta, el Narrador puede resolver posición aproximada.

Decir "creo que está allí" o señalar una posición sospechada no revela por sí mismo a una criatura oculta. Comunicar una sospecha permite coordinar ataques al área o dirigir búsqueda, pero no elimina penalizadores ni convierte la posición en exacta.

### Revelación parcial

Una acción puede revelar posición aproximada sin revelar posición exacta.

Ejemplos:

- una flecha sale desde una zona de arbustos;
- una piedra cae desde una cornisa;
- una voz se oye desde el oeste;
- una sombra cruza detrás de humo.

En ese caso, los enemigos pueden atacar el área aproximada, moverse para abrir línea, o hacer detección con Percepción o Técnicas.

### Posición aproximada incierta

Cuando una criatura oculta compromete su ocultación y otra criatura intenta localizarla, se hace una tirada enfrentada entre la Percepción del detector y la ocultación de la criatura escondida.

La posición aproximada incierta existe para que el detector reciba una pista jugable sin saber si acertó. El jugador debe saber que su personaje percibió algo, pero no si esa percepción fue correcta.

### Jugador oculto, criatura detecta

Si el jugador es quien está oculto:

1. El jugador tira la misma especialización que usó para ocultarse, o la especialización apropiada si la ficción cambió.
2. El Narrador tira `T.E. de Percepción` por la criatura que intenta detectarlo.
3. Si Percepción supera la ocultación, la criatura localiza la posición real del personaje.
4. Si Percepción no supera la ocultación, el Narrador tira `1d8` y la criatura actúa hacia la posición falsa indicada por esa dirección, si su comportamiento lo justifica.

### Criatura oculta, jugador detecta

Si una criatura es quien está oculta:

1. El jugador tira `T.E. de Percepción`.
2. El Narrador tira en secreto la ocultación de la criatura.
3. El Narrador también tira `1d8` en secreto al mismo tiempo, declarando solo que está resolviendo ocultación.
4. Si la Percepción del jugador supera la ocultación, el Narrador señala la posición real.
5. Si la Percepción del jugador no supera la ocultación, el Narrador señala la posición falsa indicada por el `1d8`.

El Narrador no declara si la tirada del jugador tuvo éxito o falló. El punto mostrado es lo que el personaje cree haber percibido.

Los empates favorecen a la criatura oculta.

Direcciones:

| 1d8 | Dirección |
| --- | --- |
| 1 | Noroeste |
| 2 | Norte |
| 3 | Noreste |
| 4 | Oeste |
| 5 | Este |
| 6 | Suroeste |
| 7 | Sur |
| 8 | Sureste |

En grid, el resultado del `1d8` corresponde por defecto a la casilla adyacente a la posición real de la criatura oculta en esa dirección.

Si la criatura ocupa más de una casilla, usa la casilla adyacente al borde de su espacio en esa dirección.

Si esa casilla no es válida, está bloqueada o no es plausible, usa la cobertura, celda o área plausible más cercana en esa misma dirección. En juego sin grid, usa una zona cercana creíble en esa dirección.

---

## Detectar criaturas ocultas

### Detección con Percepción

Usa:

```text
T.E. de Percepción contra la ocultación o contra la dificultad del entorno
```

No existe una acción universal separada llamada Buscar. Buscar se resuelve como una `T.E. de Percepción`, una Técnica, o una acción específica de la escena si el Narrador la exige por tiempo, posición o presión.

En un éxito, detecta la posición de la criatura oculta para sí misma. Puede comunicar una sospecha o dirección si la escena permite hablar, señalar o coordinarse, pero esa comunicación no revela automáticamente a la criatura para todos.

### Detección provocada

La detección provocada ocurre cuando una criatura oculta produce una señal suficiente para que otros tengan oportunidad de notarla.

El Narrador puede pedir una `T.E. de Percepción`, usar un umbral fijo o simplemente revelar información parcial si la señal es obvia.

La detección provocada no reemplaza el uso deliberado de Percepción o Técnicas. Sirve para resolver señales creadas por la criatura oculta, no para escanear gratis todo el entorno.

---

## Posición aproximada

Si una criatura oculta revela una señal sin revelar su posición exacta, el Narrador puede dar una ubicación aproximada.

Si la mesa necesita aleatorizar dirección, usa `1d8`:

| 1d8 | Dirección aproximada |
| --- | --- |
| 1 | Noroeste |
| 2 | Norte |
| 3 | Noreste |
| 4 | Oeste |
| 5 | Este |
| 6 | Suroeste |
| 7 | Sur |
| 8 | Sureste |

Esta regla puede usarse abiertamente para direcciones aproximadas, o en secreto como parte del procedimiento de posición aproximada incierta.

---

## Notas de balance

La ocultación necesita límites porque puede volverse demasiado fuerte si impide demasiadas respuestas.

Reglas de seguridad:

- ocultarse requiere una razón física, ambiental o técnica;
- la ocultación se mide por enemigo, no como estado universal;
- oculto no significa intocable;
- los efectos de área siguen funcionando si cubren la posición;
- atacar suele revelar o poner en riesgo la ocultación;
- la percepción especializada puede acelerar detección, pero no debe borrar todo el juego de señales;
- criaturas con sentidos no visuales pueden ignorar o reducir ocultación visual.
- habilidades, Técnicas o criaturas pueden declarar que ignoran ocultación bajo condiciones específicas.

---

## Preguntas abiertas

- ¿Qué especialización exacta representa Sigilo si todavía no está en el catálogo final?
- ¿Qué Técnicas permiten atacar sin revelar posición?
