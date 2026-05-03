# Marco de Interacción de Técnicas

**Estado:** Draft
**Datos de autoridad:** `data/system/techniques.yaml`, `data/system/technique-interaction-surfaces.yaml`
**Referencias primarias:** `docs/system/techniques.md`, `docs/system/mechanics-overview.md`
**Referencias relacionadas:** `docs/system/roll-types.md`, `docs/system/atb-reference.md`, `docs/system/attrition-fatigue.md`, `docs/system/wounds-and-damage.md`, `docs/system/cover-visibility-concealment.md`, `docs/system/ailments.md`, `docs/system/environmental-conditions.md`, `docs/system/equipment-overview.md`, `docs/system/specializations.md`

---

## Propósito

Este documento define cómo una **Técnica** puede interactuar con el resto del sistema.

La intención es que las Técnicas de Transcendence no sean solo:

- texto evocador con daño adicional;
- texto evocador con descuento de Ritmo;
- ataques nombrados sin consecuencia sistémica;
- paquetes arbitrarios de bonificadores.

Una buena Técnica debe producir una interacción funcional con una o más superficies reales del juego: tiempo, desgaste, impacto, heridas, cobertura, ocultación, resistencias, equipo, ambiente, recuperación, partes rompibles, información, progresión o cualquier otro sistema que ya exista.

Esto permite que las Técnicas eventualmente abarquen todo el juego sin perder claridad.

---

## Regla Central

Cada Técnica debe declarar al menos una **superficie mecánica primaria**.

Una Técnica fuerte suele tener:

- `1` superficie primaria;
- `1` superficie secundaria;
- a veces `1` superficie terciaria menor, si la ficción la justifica claramente.

Más superficies son posibles, pero deben tratarse como presión de balance. Si una Técnica toca demasiadas cosas, empieza a sentirse como una mini-lista de poderes en lugar de una acción entrenada.

La interacción debe nacer de la ficción de la Técnica:

- movimiento;
- postura;
- presión;
- equipo;
- anatomía;
- entrenamiento;
- lectura del entorno;
- control del ritmo;
- contacto material;
- exposición corporal;
- oportunidad táctica.

Si la Técnica no puede explicar por qué toca una superficie, no debería tocarla.

---

## Campo Recomendado Para Técnicas

Toda Técnica nueva debería registrar:

```yaml
mechanical_surfaces:
  primary: ""
  secondary: []
  operations: []
  counterplay: []
  balance_notes: ""
```

### Primary

La superficie que define lo que la Técnica realmente hace.

Ejemplos:

- `critical_breaking_parts`
- `cover_positioning`
- `visibility_concealment`
- `timing_atb`
- `ailments_resistance`

### Secondary

Superficies que apoyan la identidad principal sin reemplazarla.

Ejemplo:

- una Técnica de escudo puede tener `cover_positioning` como primaria y `timing_atb` como secundaria si funciona como Reacción.

### Operations

Los verbos mecánicos que explican cómo la Técnica altera el sistema.

Ejemplos:

- `grant_bonus`
- `impose_penalty`
- `convert`
- `trigger`
- `suppress`
- `reveal`
- `relocate`
- `break`
- `downgrade`
- `escalate`

### Counterplay

La forma en que otro personaje, criatura o sistema puede responder.

Ejemplos:

- `T.R.`
- `T.D.`
- Percepción;
- cobertura;
- romper el equipo;
- salir del área;
- gastar Ritmo;
- esperar a que termine la duración;
- atacar una parte vinculada.

---

## Superficies Mecánicas

Las superficies son los sistemas que una Técnica puede tocar. No son etiquetas de sabor: son puertas hacia reglas existentes.

| Superficie | Qué puede modificar |
| --- | --- |
| `roll_resolution` | T.A., T.D., T.I., T.E., T.C., T.R., T.P., bonificadores, penalizadores, oposición, repetición |
| `thresholds` | Dificultad, NR, grados de exigencia, umbrales fijos |
| `timing_atb` | Ritmo, Reacción, ventanas de respuesta, acciones rápidas/pesadas, seguimiento |
| `cost_pressure` | Desgaste, Aguante, Fatiga, carga sostenida, costo corporal |
| `damage_impact` | Impacto, Bloqueo, daño contra HP, daño contra zonas de NPC |
| `critical_breaking_parts` | Impacto Crítico, dado crítico, Potencia Crítica, Durabilidad, romper partes |
| `wounds_body_state` | heridas, ranuras, saturación, colapso, estados corporales, estabilizar/tratar/curar |
| `equipment_material` | armas, escudos, armaduras, bloqueo de piezas, material, calidad, durabilidad |
| `cover_positioning` | cobertura, línea de ataque, protección de escudo, zonas, movimiento, empuje |
| `visibility_concealment` | visibilidad, ocultación, detección, posición aproximada, sentidos especiales |
| `ailments_resistance` | agravios, alteraciones, venenos, infecciones, aflicciones, maldiciones, T.R. |
| `environment` | terreno, clima, condiciones naturales/extranaturales, severidad ambiental |
| `recovery_rest` | descanso, recuperación de Desgaste, tratamiento médico, continuidad de expedición |
| `information` | verdades tácticas, lectura, identificación, rastreo, información accionable |
| `progression_learning` | progreso, fallos, afinidad, acceso, entrenamiento, desbloqueos |
| `npc_encounter_parts` | partes de criatura, habilidades vinculadas, fases, puntos vitales, HP por parte |
| `manifestation` | detección o manejo limitado de manifestaciones del Limbo, sin convertirse en magia |

---

## Verbos Mecánicos Canónicos

Cuando una Técnica toca una superficie, debe usar verbos claros.

| Verbo | Uso |
| --- | --- |
| `grant_bonus` | da un bono a una tirada o valor específico |
| `impose_penalty` | impone penalizador a una tirada, acción o zona concreta |
| `reroll` | permite repetir o reemplazar una tirada bajo condición |
| `convert` | convierte un tipo de presión en otro |
| `replace` | usa una regla alternativa en lugar de la base |
| `trigger` | activa un efecto cuando ocurre una condición concreta |
| `suppress` | apaga temporalmente un efecto, estado o permiso |
| `extend` | amplía duración, rango, área o ventana |
| `reduce` | reduce costo, severidad, ritmo, desgaste o dificultad |
| `escalate` | aumenta severidad, costo, presión o consecuencia |
| `downgrade` | baja una herida, agravio, severidad o resultado |
| `mark` | deja una marca táctica que otro efecto puede usar |
| `reveal` | revela información, posición, debilidad o intención |
| `hide` | permite ocultarse, mantener ocultación o falsear ubicación |
| `relocate` | mueve una criatura, parte, zona de efecto o línea de ataque |
| `intercept` | se interpone en una línea, ataque, movimiento o efecto |
| `break` | rompe parte, equipo, cobertura o estructura |
| `degrade` | reduce Durabilidad sin romper todavía |
| `restore` | recupera función, ranura, desgaste o estabilidad |
| `consume` | gasta recurso, postura, carga, preparación o ventana |
| `refund` | devuelve o evita un costo bajo condición |

Si un efecto no cabe en ningún verbo, probablemente necesita aclararse antes de convertirse en Técnica.

---

## Patrones Por Superficie

### Tiradas y Resolución

Una Técnica puede modificar una tirada, pero el bono plano debe ser el último recurso.

Buenos usos:

- cambia cuándo se tira;
- cambia qué tirada se opone;
- da un bono condicionado a una lectura previa;
- castiga una defensa específica;
- convierte una T.E. exitosa en una ventaja de apertura.

Riesgo:

- inflar números sin crear decisiones nuevas.

### Ritmo y ATB

Una Técnica puede cambiar quién actúa, cuándo reacciona o qué ventana queda abierta.

Buenos usos:

- Reacción contra un disparador estrecho;
- seguimiento más barato después de una preparación;
- castigo si el enemigo actúa dentro de una zona;
- cierre de línea antes de que el ataque se complete.

Riesgo:

- reducir Ritmo de forma genérica;
- negar turnos completos sin contrajuego.

### Desgaste, Aguante y Fatiga

Una Técnica puede ahorrar esfuerzo, absorber presión o forzar un costo corporal mayor.

Buenos usos:

- usar más Desgaste para sostener una defensa;
- reducir Desgaste si la Técnica se ejecuta con el equipo correcto;
- operar con Fatiga a cambio de penalizadores;
- convertir carga sostenida en presión táctica.

Riesgo:

- crear recuperación infinita;
- hacer irrelevante el Aguante.

### Impacto, Bloqueo y Daño

Una Técnica puede alterar cómo un golpe transmite presión después de conectar.

Buenos usos:

- aumentar Impacto solo contra una zona preparada;
- ignorar parte del Bloqueo si se cumple una condición física clara;
- cambiar daño contra HP de NPC;
- convertir una apertura en daño contra una parte específica.

Riesgo:

- duplicar daño e ignorar Bloqueo al mismo tiempo sin costo alto;
- convertir todo ataque en daño superior.

### Impacto Crítico y Romper Partes

Una Técnica puede ampliar, anticipar o especializar la ruptura.

Buenos usos:

- permitir intento de ruptura sin crítico bajo condición muy específica;
- aumentar Potencia Crítica contra una clase de material;
- declarar una parte no obvia como objetivo;
- degradar Durabilidad aunque no se rompa;
- romper una parte para apagar una habilidad de criatura.

Regla base:

- si `Potencia Crítica >= Durabilidad`, la parte se rompe;
- si es menor, la parte pierde `1` Durabilidad en ese intento válido;
- los ataques normales no reducen Durabilidad por defecto.

Riesgo:

- romper partes sin contacto material creíble;
- invalidar jefes sin exponer al usuario a costo, defensa o preparación.

### Heridas y Estados Corporales

Una Técnica puede interactuar con ranuras, saturación, colapso o tratamiento.

Buenos usos:

- estabilizar una zona en escena;
- evitar que una zona saturada escale durante una ventana breve;
- permitir actuar con una zona colapsada pagando Desgaste;
- convertir una herida menor en presión táctica si el objetivo repite la acción comprometida.

Límite importante:

- una Herida Crítica no fuerza T.R. por defecto;
- puede forzar T.R. si causa Colapso en zona vital, si la Técnica lo dice, si el Agravio lo exige o si la circunstancia extrema lo justifica.

Riesgo:

- curar ranuras demasiado rápido;
- saltarse tratamiento, descanso y Medicina sin costo claro.

### Cobertura, Posición y Movimiento

Una Técnica puede crear, mover, negar o explotar líneas.

Buenos usos:

- usar un escudo como cobertura fuera de su celda normal;
- cubrir a otra criatura como Reacción;
- mover al objetivo fuera de cobertura;
- hacer que un área reduzca parcialmente el beneficio de cobertura;
- empujar, arrastrar o fijar una posición.

Riesgo:

- convertir una protección localizada en inmunidad de área;
- permitir cubrir aliados gratis sin Técnica o costo.

### Visibilidad y Ocultación

Una Técnica puede crear oportunidad de ocultarse, detectar, mantener ocultación o falsear posición.

Buenos usos:

- ocultarse mientras se rompe línea de visión;
- mantener ocultación al moverse entre coberturas;
- detectar una posición aproximada mediante olfato, vibración o lectura;
- negar ventaja de apertura si se supera Percepción;
- crear una falsa señal en una dirección.

Riesgo:

- invisibilidad práctica sin reglas de detección;
- permitir desaparecer mientras el objetivo te percibe claramente.

### Agravios y Resistencias

Una Técnica puede aplicar, modificar, resistir o explotar agravios.

Buenos usos:

- aplicar Alteración si el golpe impacta y el objetivo falla T.R.;
- reducir severidad de Veneno si el personaje está entrenado;
- hacer que una Maldición exija otra forma de resistencia;
- explotar una Vulnerabilidad menor o mayor definida en el perfil de una criatura, material u objeto;
- dar contrajuego a través de T.R. y duración clara.

Riesgo:

- estados persistentes sin salida;
- resistencias usadas como única identidad de Técnica.

Las resistencias de personaje no reducen daño elemental. Si una Técnica interactúa con fuego, agua, luz, oscuridad u otro origen elemental, esa interacción debe operar como origen del efecto, Alteración, entorno, material o rasgo de Vulnerabilidad/Resistencia definido por el objetivo.

### Equipo, Material y Objetos

Una Técnica puede depender de armas, escudos, armaduras, herramientas o materiales.

Buenos usos:

- una Técnica de escudo pesado que requiere tamaño/carga suficiente;
- una Técnica de lanza que depende de alcance y línea;
- una Técnica de daga que aprovecha crítico frecuente pero baja Potencia;
- una Técnica que da valor a material sin cambiar daño base.

Riesgo:

- meter reglas que deberían pertenecer al objeto;
- ignorar carga, tamaño o manejo.

### Información

Las Técnicas de lectura no deberían ser solo bonos pasivos.

Buenos usos:

- revelar una verdad táctica inmediata;
- identificar la parte más vulnerable;
- saber qué ruta intenta tomar el enemigo;
- detectar que una conclusión es falsa;
- exponer una intención antes de que se ejecute.

Riesgo:

- convertir toda Técnica de conocimiento en `+X a la siguiente tirada`.

### Progresión y Aprendizaje

Esta superficie debe usarse con cuidado.

Buenos usos:

- permitir acceso a una Técnica por mentor, rango o especialización;
- modificar progreso solo en casos de entrenamiento muy específicos;
- crear afinidad con una familia de Técnica.

Riesgo:

- acelerar progreso como recompensa genérica;
- mezclar economía de aprendizaje con cada Técnica de escena.

---

## Peso de Interacción

No todas las superficies pesan igual.

### Peso bajo

- bono pequeño y condicionado;
- una verdad informativa concreta;
- movimiento corto;
- reducción menor de costo;
- ventaja consumible de un solo uso.

### Peso medio

- Reacción con disparador claro;
- condición recuperable;
- modificación de cobertura;
- daño o Impacto condicionado;
- ocultación o detección con Percepción como contrajuego;
- degradar Durabilidad.

### Peso alto

- negar una acción;
- romper equipo o parte;
- ignorar Bloqueo;
- curar ranuras;
- alterar la economía de Ritmo;
- aplicar estado persistente;
- forzar movimiento;
- afectar múltiples objetivos;
- interactuar con zonas vitales o Colapso.

Una Técnica con una superficie de peso alto debe pagar con al menos una de estas cosas:

- rango mínimo mayor;
- costo de Ritmo más alto;
- Desgaste mayor;
- disparador estrecho;
- equipo obligatorio;
- T.R., T.D. o Percepción como contrajuego;
- duración breve;
- uso limitado;
- preparación visible.

---

## Patrón Bueno

Una Técnica sólida suele verse así:

- fantasía clara;
- superficie primaria definida;
- superficie secundaria que nace de la misma ficción;
- costo real;
- contrajuego visible;
- duración y alcance claros;
- términos canónicos.

Ejemplo:

- fantasía: el escudo corta la línea antes del impacto;
- primaria: `cover_positioning`;
- secundaria: `timing_atb`;
- operación: `intercept`, `impose_penalty`;
- costo: Reacción con Ritmo y Desgaste;
- contrajuego: atacar desde otro ángulo, romper escudo, usar área, forzar al portador a moverse.

---

## Patrón Malo

Evita Técnicas que:

- suman daño, defensa, movimiento, curación y estado a la vez;
- modifican demasiadas tiradas;
- tocan una superficie solo porque existe;
- inventan sinónimos para términos que ya están en el glosario;
- no tienen costo, límite o contrajuego;
- curan, rompen, ocultan o niegan acciones sin una regla de respuesta;
- parecen magia sin pertenecer al subsistema mágico.

Si una Técnica empieza a leerse como una lista de compras, necesita compresión.

---

## Checklist de Autoría

Antes de aceptar una Técnica, responder:

1. ¿Cuál es su superficie primaria?
2. ¿Cuál es su superficie secundaria, si existe?
3. ¿Qué verbo mecánico usa?
4. ¿Qué término canónico del glosario toca?
5. ¿En qué momento exacto se declara?
6. ¿Ocurre antes o después de la tirada relevante?
7. ¿Tiene alcance, área y duración definidos?
8. ¿Cuánto cuesta en Ritmo y Desgaste?
9. ¿Qué la detiene, resiste o mitiga?
10. ¿Se acumula, reemplaza o expira?
11. ¿Depende de equipo, zona, parte, cobertura, sentido o material?
12. ¿El efecto sigue teniendo sentido si se elimina un bono numérico?

Si no puede responder esas preguntas, todavía no está lista para publicación.

---

## Fuera de Alcance

Las siguientes áreas no son buenos pilares primarios de Técnicas por defecto:

- expresión amplia de rasgos de personalidad;
- economía completa de fabricación;
- extracción de recursos como loop principal;
- aprendizaje de idiomas;
- simulación social abierta sin presión de escena;
- interludios largos sin riesgo, oposición o consecuencia inmediata.

Pueden aparecer como contexto, requisito o recompensa, pero no deberían definir la mayoría de Técnicas.

---

## Estándar Actual

Las Técnicas de Transcendence deben aspirar a ser:

- temáticas;
- espectaculares;
- tácticamente legibles;
- conectadas a sistemas reales;
- contenidas por costo y contrajuego;
- variadas entre sí.

El juego debe recompensar a los jugadores por aprender a usar:

- tiempo;
- presión;
- cuerpo;
- equipo;
- cobertura;
- visibilidad;
- partes rompibles;
- resistencias;
- ambiente;
- información;
- recuperación;
- progresión;

no solo por encontrar el número más alto.
