# Catálogo de Técnicas por Superficie

**Fuente de verdad:** `Transcendence-publications/core-books/transcendence-techniques/es/`  
**Propósito:** Referencia de no-solapamiento antes de diseñar cualquier técnica nueva.  
**Estado:** Extrae de los archivos reales — no depende del YAML (desactualizado).

> **Regla de acceso:** Este catálogo está organizado por superficie mecánica, **no por especie**.  
> La especie es origen de lore únicamente. Cualquier personaje con el perfil de arma,  
> tipo de armadura, o especialización correcta puede usar la técnica.  
> Cuando diseñes una técnica nueva, compara contra **toda** la columna de su superficie.

---

## Actualización

Cuando se agrega una técnica nueva, actualiza la tabla de su superficie con:
- número de técnica
- título
- tipo (Activo-Ataque / Reactivo-Utilidad / etc.)
- salida principal (efecto mecánico concreto en 4-6 palabras)

---

## 1. Técnicas de Perfil de Arma

22 perfiles definidos en `data/system/weapon-technique-profiles.yaml`.  
La tabla muestra cuántas técnicas existen por perfil y qué terreno mecánico han cubierto.  
Antes de diseñar: leer la columna completa del perfil y mapear gaps reales.

### Acecho / Shadow Pressure (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Robar la Orilla | Activo - Ataque | Presión desde Oculto; penaliza T.D. |
| — | Lo que Cedió Primero | Reactivo - Utilidad | Contraataque al mover; window post-oculto |
| — | El Ángulo Muerto | Reactivo - Ataque | Pursecución desde Oculto; hereda Efectos |

### Bastión (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Plantar la Guardia | Activo - Ataque | Postura; Derriba en contacto |
| — | La Línea que No Se Rompe | Activo - Utilidad | Postura; eje de control con maza |
| — | El Marco Antes del Paso | Activo - Utilidad | Postura; escudo + absorción de desplazamiento |

### Cadencia / Volley (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Clavar la Cadencia | Reactivo - Utilidad | Control de movimiento al disparar; acumula presión |
| — | Cobrar el Paso | Reactivo - Ataque | Presión de rango al avanzar enemigo |

### Control de Línea (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Cerrar la Línea | Reactivo - Utilidad | Anti-desplazamiento; estabilidad posicional |
| — | La Masa Continúa | Activo - Ataque | Desplazamiento forzado con escudo |
| — | [Naghii — lanza] | Reactivo - Ataque | Control de línea con asta |

### Corrosión (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Ensuciar la Herida | Activo - Ataque | Residuo corrosivo; bloquea tratamiento |
| — | Sostener el Canal | Activo - Utilidad | Residuo a distancia; aplicación preventiva |
| — | La Capa que Cede | Activo - Ataque | Penaliza T.D. armadura; degrada superficie defensiva |

### Desgarro / Rend (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Abrir la Costura | Activo - Ataque | Lacerado; presión de herida abierta |
| — | Cortar la Mano Tarde | Activo - Ataque | Setup de desgarro; ventaja en seguimiento |
| — | El Eje que Cede | Activo - Ataque | Ventaja en T.I.; precisión en zona expuesta |

### Desvío / Deflection (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 78 | El Ángulo que Falla | Reactivo - Ataque | Desvío reactivo con arma natural; contraataque |
| 141 | El Ángulo que Expone | Reactivo - Defensa | Desvío con hoja; penaliza ataque siguiente |

### Embestida / Charge (1)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | La Carga que No Acaba | Activo - Ataque | Entrada forzada; rompe línea defensiva |

### Fluidez / Flow (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Cobrar con la Otra | Activo - Ataque | Salida con lacerado; presión de secuencia |
| — | Lo que Este Lugar Recuerda | Activo - Ataque | Cadena; reposicionamiento entre golpes |
| — | Lo que Se Conoce No Sorprende | Activo - Ataque | Cadena; bonificador en segundo golpe |

### Hostigamiento / Skirmish (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Robar el Ángulo | Activo - Ataque | Entrada-salida con movilidad |
| — | Antes de que Cambie | Activo - Ataque | Disrupción de tempo; hurto de ATB |
| — | [Naghii — flexible] | Activo - Ataque | Movilidad en hostigamiento ligero |

### Imparable / Unstoppable (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | La Corriente No Retrocede | Activo - Ataque | Avance forzado; ignora bloqueo parcial |
| — | El Peso que Gira | Activo - Ataque | Bloqueo convertido en empuje; desplaza defensor |

### Impacto / Impact (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Anclar el Contrapeso | Activo - Ataque | Valida ruptura de material |
| — | Romper el Caudal | Activo - Ataque | Desequilibrado; disruption de guardia |
| — | El Peso que Planta | Activo - Ataque | Derriba con mazo |

### Impredecible / Unpredictability (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Nublar la Señal | Activo - Utilidad | Rompe lectura; Desequilibrado sin T.A. |
| — | La Vuelta que Suelta | Activo - Ataque | Secuencia de cierre con Desequilibrado |
| — | El Golpe sin Eco | Activo - Ataque | Enmascaramiento acústico; bypass T.D. |

### Intercepción / Interception (4)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Tomar el Resguardo | Reactivo - Utilidad | Cubre a aliado; intercepta golpe entrante |
| — | Anudar la Vasija | Reactivo - Ataque | Escolta; escudo contra atacante de aliado |
| — | El Tránsito que No Llega | Reactivo - Utilidad | Deniega movimiento con Impedido |
| — | La Base que Falta | Reactivo - Utilidad | Cierre posicional; deniega posición |

### Interrupción / Interruption (5)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Trabar el Gesto | Reactivo - Utilidad | Atrapa; deniega movimiento |
| — | Clavar el Paso | Reactivo - Ataque | Interrumpe acción; Desequilibrado |
| — | Anudar el Paso | Reactivo - Ataque | Interrumpe; cuarentena de efecto |
| — | Leer el Calor del Paso | Reactivo - Ataque | Interrupción flexible; contraataque |
| — | [Drak'kai] | Reactivo - Ataque | Desequilibrado; alteración en interrupción |

### Letalidad / Lethality (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Encontrar la Parte Blanda | Activo - Ataque | Finalización; explota zona expuesta |
| — | La Salida que Cobra | Reactivo - Ataque | Contraataque en crítico; letalidad reactiva |

### Perforación / Perforation (3)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Sentar el Tercer Punto | Activo - Ataque | Perforación; presión de entrada |
| — | Cerrar la Compuerta | Activo - Ataque | Perforación; deniega avance |
| — | La Posición que Se Hunde | Activo - Ataque | Bypass de armadura; precisión de línea |

### Precisión / Precision (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Marcar la Lectura | Activo - Ataque | Marcado a distancia; penaliza siguiente acción |
| — | La Brecha Contada | Activo - Ataque | Perjuicio de ataque ranged del objetivo |

### Rebote / Ricochet (1)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 9 | Doblar el Tiro | Activo - Ataque | Tiro angulado; geometría de rebote |

### Ruptura / Sunder (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Quebrar la Vuelta | Activo - Ataque | Rompe protección; abre zona |
| — | El Cierre que No Se Negocia | Activo - Ataque | Ruptura de armadura con maza |

### Torsión (4)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Tocar y Ceder | Reactivo - Utilidad | Redirección angular; control con flexible |
| — | Barrer la Orilla | Activo - Ataque | Reposicionamiento forzado con giro |
| — | Devolver al Cauce | Activo - Utilidad | Desarme; alteración de control |
| — | La Cuenta del Cuerpo | Activo - Ataque | Desequilibrado por eje de torsión acústica |

### Guarda / Ward (1)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| — | Sellar la Presa | Activo - Utilidad | Postura; control de zona con asta |

---

## 2. Técnicas de Armadura

Una técnica puede cubrir más de un tier (e.g. Intermedia + Pesada simultáneamente).

### Armadura Pesada (4)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 46 | Cerrar la Coraza | Activo - Utilidad | Postura de bloqueo; 3 piezas requeridas |
| 47 | Volver la Placa | Reactivo - Utilidad | Evita chequeo de ruptura en crítico |
| 86 | El Golpe que Cobra | Reactivo - Utilidad | Presión ATB reactiva; contraataque posicional |
| 87 | El Cuerpo que Se Calibra | Activo - Utilidad | Postura; acumulación de bloqueo |

### Armadura Intermedia (1)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 47 | Volver la Placa | Reactivo - Utilidad | Evita chequeo de ruptura en crítico (compartida con Pesada) |

### Armadura Ligera (2)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 58 | Soltar la Capa Muerta | Reactivo - Utilidad | Reposicionamiento reactivo; deniega contacto |
| 134 | El Eje sin Fisura | Reactivo - Ataque | Contraataque desde lectura acústica; hereda Efectos |

### Evasión (4)

| # | Título | Tipo | Salida principal |
|---|---|---|---|
| 19 | Cruzar la Punta | Reactivo - Utilidad | Reposicionamiento; evade y recupera ángulo |
| 20 | Vaciar el Blanco | Reactivo - Utilidad | Quiebra continuidad; ventana de supervivencia |
| 57 | Quebrar la Vuelta | Reactivo - Utilidad | Quiebra ángulo; repositioning post-contacto |
| 137 | La Brecha sin Ruido | Reactivo - Utilidad | Lectura acústica del atacante; penaliza ataque |

---

## 3. Técnicas de Especialización

Listado de especializaciones con al menos 1 técnica activa o reactiva publicada.  
Las resistencias híbridas (pasivas) están en la sección 4.

| Especialización | Cantidad | Técnica(s) |
|---|---|---|
| Agarre | 1 | Sellar la Grieta |
| Alquimia | 1 | Guardar el Pulso |
| Aplomo | 1 | Asentar la Piedra |
| Arquitectura | 1 | Sentar el Tercer Punto *(arquitectura táctica)* |
| Arqueología | 1 | Leer la Línea Ausente |
| Astronomía | 1 | Medir el Ciclo |
| Contención | 1 | Tomar la Corriente |
| Destreza | 1 | Cerrar la Salida |
| Enfoque | 1 | La Posición que Se Hunde |
| Equilibrio | 1 | Tomar el Eco |
| Geografía | 1 | El Espacio Se Sabe |
| Herboristería | 1 | Hacer Esperar la Podredumbre |
| Historia | 2 | La Grieta que ya Apareció Antes · La Referencia que Queda |
| Identificación | 2 | El Margen que Se Mueve · Lo que el Cuerpo Anuncia |
| Interpretación | 2 | Leer el Propósito · Lo que el Gesto Revela |
| Intimidación | 1 | Reír en la Brecha |
| Lanzamiento | 1 | Tirar la Advertencia |
| Lingüística | 1 | Oír la Costura |
| Medicina | 2 | Levantar el Dique · La Señal Repetida |
| Meditación | 1 | Sostener la Mano Necesaria *(activa; la resistencia híbrida está en §4)* |
| Minería | 1 | Tomar la Secuencia |
| Nadar | 1 | Sellar la Presa |
| Orientación | 2 | Pasar Como Parte del Fondo · El Ángulo Estudiado |
| Percepción | 2 | Leer lo que Siguió · La Grieta Elegida |
| Rastreo | 2 | Lo que el Cuerpo Delata · El Margen que Quedó Abierto |
| Resonancia | 2 | Marcar la Grieta · Nombrar el Umbral |
| Sigilo | 3 | Pesar el Umbral · Reír Donde Más Suena · El Eco que Persiste |
| Supervivencia | 1 | Tomar la Costura |
| Taumaturgia | 1 | Fijar el Umbral *(activa; la resistencia híbrida está en §4)* |
| Tolerancia | 1 | Darle a la Pieza Útil *(activa; las resistencias híbridas están en §4)* |
| Trampas | 1 | Tomar la Parte Útil |

**Total de especializaciones representadas:** 31 de 54+

**Especializaciones sin ninguna técnica publicada aún (muestra, no exhaustiva):**  
Acrobacia, Actuación, Atletismo, Comercio, Cocina, Enseñanza, Escritura, Escultura, Etiqueta, Herrería, Jardinería, Liderazgo, Navegación, Negociación, Orfebrería, Ornitología, Pintura, Tejeduría, Vidriería, y otras.

---

## 4. Resistencias Híbridas

Técnicas pasivas que combinan una **resistencia del sistema** con una **especialización**.  
Siempre: tipo `Pasivo - Resistencia`, coste Ritmo 0 / Desgaste 0.

Las 5 resistencias del sistema: Veneno, Infección, Aflicción, Calor/Frío, Taumática.

| # | Título | Resistencia | Especialización | Origen de lore |
|---|---|---|---|---|
| — | Templar el Veneno | Veneno | Tolerancia | Naghii |
| — | Atajar el Brote | Infección | Tolerancia | Zarnag |
| — | Mantener Cerrada la Línea de Contagio | Infección | Medicina | Zarnag |
| — | Bajar el Núcleo | Aflicción | Meditación + Contención | Naghii |
| — | Hacer Ceder el Resguardo | Calor | Aclimatación | Sauri |
| — | Cerrar el Juicio | Aflicción | Teología | Sauri |
| — | La Carcajada | Terror (Aterrorizado) | Contención | Vesper |
| — | Protección Natural | Ensordecido | Tolerancia | Vesper |
| — | El Umbral sin Quiebre | Fatiga | Meditación | Drak'kai |
| — | Lo que Se Conoce No Sorprende | Taumática | Taumaturgia | Drak'kai |

**Total:** 10 resistencias híbridas publicadas.

---

## 5. Técnicas Innatas

Una por especie. No tienen perfil de arma ni especialización — representan la capacidad biológica propia de cada especie.

| # | Título | Especie |
|---|---|---|
| 98 | La Carcajada | Zarnag |
| 99 | Protección Natural | Sauri |
| 100 | Piel de Sombra | Naghii |
| 101 | Magnetorrecepción | Drak'kai |
| 102 | La Batida | Rokhart |
| 103 | Señal Química | Formix |
| 104 | Olfato Profundo | Loxod |
| 105 | Integridad de la Señal | Ceratox |
| 106 | El Veredicto | Chelicer |
| 107 | Adaptabilidad | Panin |
| 108 | La Presa del Oso | Ursari |
| 109 | El Ancestro Despierta | Luphran |
| 110 | Urdimbre | Arakhel |
| 111 | Golpe sin Eco | Bufoni |
| 112 | Zona de Eco | Vesper |
| 113 | Aceleración del Caos | Lapinni |
| 114 | Depredador Umbrío | Kesh |
| 115 | Tórax de Forja | Talpan |
| 116 | El Ayuno de la Mente | Soricin |
| 117 | Saturación | Yacani |

---

## Notas de mantenimiento

- Los títulos en §1 y §3 son aproximados donde no se leyó el archivo directamente. Verificar contra los archivos `.md` si hay duda.
- El catálogo refleja el estado al terminar el pase de Vesper (técnica #141).
- La numeración de técnicas en §1-3 se completará en futuras actualizaciones.
- `Rebote` y `Desvío` son dos perfiles distintos aunque ambos "desvían" fuerza. Rebote = tiro angulado/físico; Desvío = redirección de golpe cuerpo a cuerpo.
