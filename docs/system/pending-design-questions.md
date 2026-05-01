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
- `wounds-and-damage.md` ya define la diferencia provisional entre estabilizar, tratar y curar. Los descansos de 30 y 60 minutos estabilizan; solo el descanso completo con tratamiento libera ranuras.
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
