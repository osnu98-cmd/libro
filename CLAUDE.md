# CLAUDE.md — Libro «Soy del Campo — La historia de la batalla cultural chilena»

Oscar Antonio Núñez Llanca · Fundación Soy del Campo Chile
Configuración de trabajo para Claude Code · v01 — 24-jul-2026

> Copia del protocolo que vive en Dropbox
> (`/Soy del Campo/Libro Derecho Animal/claude/CLAUDE.md`). Si se edita
> allá, actualizar acá.

---

## 0. Jerarquía normativa

Ante conflicto entre reglas, prevalece en este orden:

1. **Regla Cero** (verificación de fuentes) — innegociable.
2. **Regla del Testimonio** — el relato es del autor, no de Claude.
3. **Regla de Etapa** — Etapa 1 es bruta; no se depura antes de tiempo.
4. Todo lo demás.

Si una instrucción del autor en sesión contradice este archivo, se le
advierte el conflicto y se pide confirmación expresa antes de proceder.

---

## 1. REGLA CERO — Fuentes (innegociable)

Vigente en todo el proyecto, sin excepción:

- Toda fuente debe ser **real, existente y verificada contra fuente
  primaria** antes de usarse.
- Toda cita —legal, jurisprudencial, documental o fáctica— debe ser real
  y chequeada. **Nunca se cita de memoria ni se aproxima.**
- La forma de citar se ajusta al contexto. En el libro: nota al pie con
  referencia completa.
- **Prohibido inventar** datos, autores, fallos, boletines, montos, roles
  o contenidos. Lo que no consta se marca `[REQUIERE VERIFICACIÓN DE
  FUENTE]` y el capítulo queda incompleto en ese punto. **No se completa
  a ojo.**
- Única excepción: un ejemplo hipotético o ilustrativo se permite **solo
  si se declara EXPRESAMENTE que es hipotético**. Jamás presentar como
  real una fuente inventada.

### 1.1 Aplicación específica al dictado

El dictado oral es la fuente de riesgo más alta del proyecto, porque el
autor habla de memoria y Whisper puede alucinar cifras plausibles.

Por tanto, **nunca se toman de la transcripción**:

- Números de boletín, rol, causa o expediente
- Artículos de ley, números de ley, fechas de promulgación
- Nombres propios de personas o instituciones que suenen dudosos
- Cifras, porcentajes, montos, cantidades
- Fechas
- Citas textuales de autores

Todos esos elementos van a `[REQUIERE VERIFICACIÓN DE FUENTE]` aunque el
autor los haya dicho con seguridad, y aunque Claude Code crea saber la
respuesta.

---

## 2. REGLA DEL TESTIMONIO

Este libro es un relato histórico en primera persona. La verdad que
contiene es **la que el autor narra y confirma**, no la que Claude
compruebe por fuentes externas.

- Claude no da hechos por establecidos ni salta a conclusiones.
- Se procede hecho por hecho, confrontando con el autor.
- Las búsquedas web son material de apoyo y contraste **ofrecido** al
  autor, nunca base del relato.
- Lo incorporado sin confirmación del autor se marca
  `[POR CONFIRMAR CONTIGO]`.

---

## 3. REGLA DE ETAPA

### Etapa 1 — Borrador bruto (actual)

Objetivo: llevar las siete partes a borrador completo, **lo más crudo
posible**. No se depura editorialmente ningún capítulo hasta que el
conjunto esté completo.

Razón: la prosa pulida esconde argumentos débiles y huecos de fuente.
En bruto quedan a la vista. Además, depurar capítulo por capítulo
produce capítulos que no calzan entre sí.

**Criterio de paso a Etapa 2:** las 7 partes en borrador, cada una con
su cola de verificación levantada. No antes.

### Etapa 2 — Depuración editorial (futura)

Se activa solo por instrucción expresa del autor. Comprende unificación
de voz, eliminación de redundancias entre capítulos, trabajo de
formulación, verificación final y armado del aparato de citas.

**Mientras rija la Etapa 1, esta sección no se ejecuta.**

---

## 4. DEPURACIÓN CONSERVADORA (Etapa 1)

Al convertir transcripción cruda en borrador:

### Sí se hace

- Eliminar muletillas, repeticiones de dictado y titubeos
- Cerrar frases que quedaron colgando
- Corregir concordancia, ortografía y puntuación
- Reordenar una oración **solo** cuando el orden dictado la vuelve
  ininteligible
- Separar en párrafos

### No se hace

- No cambiar el vocabulario del autor por sinónimos "mejores"
- No sustituir su registro coloquial o rural por uno formal
- No fusionar sus oraciones cortas en períodos largos
- No reordenar el argumento
- No agregar conectores que el autor no dijo, para "dar fluidez"
- No completar razonamientos insinuados pero no desarrollados
- No agregar el fundamento jurídico "que obviamente corresponde"

### Prueba de control

Si al leer el borrador el autor reconoce su forma de hablar, está bien
hecho. Si suena a abogado escribiendo, se pasó de la raya.

### Principio rector

**Cada afirmación del borrador debe poder rastrearse a algo que el autor
efectivamente dijo.** Si Claude Code quiere agregar algo, lo agrega como
pregunta al margen, nunca como prosa.

---

## 5. LOS CUATRO REGISTROS DEL DICTADO

Al dictar libremente, el autor mezcla material de naturaleza distinta.
Claude Code lo clasifica al depurar:

| Registro | Qué es | Destino |
|---|---|---|
| **Relato** | Material del libro | Borrador del capítulo |
| **Cavilación** | Pensamiento en voz alta, sin ubicar | `02-materia-prima/cavilaciones.md` |
| **Instrucción** | "Esto va en la Parte IV", "corta acá" | Se ejecuta |
| **Recordatorio** | "Hay que buscar tal fallo" | `04-fuentes/por-verificar.md` |

El autor puede marcar el registro verbalmente al dictar ("nota al
margen:", "esto es cavilación:", "instrucción:"). Cuando no lo marque,
Claude Code infiere y **deja constancia de la inferencia** en el
encabezado del borrador.

---

## 6. AUTOCORRECCIONES DEL DICTADO (opción C)

Cuando el autor se corrige o cambia de rumbo a mitad de dictado:

1. El borrador lleva **la versión final**, la que quedó después de la
   corrección.
2. La formulación descartada se archiva en
   `02-materia-prima/descartes.md`, numerada correlativamente
   (`D-001`, `D-002`...).
3. En el punto exacto del borrador donde se descartó, queda la
   referencia: `[→ D-014]`.

Razón: a veces la formulación descartada era mejor y solo se advierte al
releer en frío. Nada se pierde, pero el borrador queda limpio.

---

## 7. MARCADORES OBLIGATORIOS

| Marcador | Cuándo se usa |
|---|---|
| `[REQUIERE VERIFICACIÓN DE FUENTE]` | Dato que necesita fuente primaria |
| `[POR CONFIRMAR CONTIGO]` | Afirmación que Claude no puede validar solo |
| `[DICTADO POCO CLARO: se entendió "X". Confirmar.]` | Claude no siguió el razonamiento |
| `[NOTA: ...]` | Observación de Claude al margen |
| `[→ D-000]` | Remite a formulación descartada |
| `[HIPOTÉTICO]` | Ejemplo declarado como ilustrativo |

**Sobre `[DICTADO POCO CLARO]`:** es preferible declarar que no se
entendió, a producir prosa fluida sobre una base malinterpretada. No hay
penalización por usarlo; sí la hay por adivinar.

---

## 8. VERSIONADO Y MARCA DE ACTUALIDAD

### Numeración

Cada borrador de capítulo lleva versión correlativa: `v01`, `v02`,
`v03`... Un borrador nuevo **no sobrescribe** al anterior; se guarda al
lado.

### Encabezado obligatorio

Todo archivo de borrador abre con este bloque, sin excepción:

```
---
capítulo: [parte y número]
versión: v03
estado: VIGENTE | SUPERADA POR v04 | EN REVISIÓN
fecha: 2026-07-24
dictado de origen: 2026-07-24-parte-i-origen.md
pendientes de verificación: 7
---
```

La marca de actualidad va **dentro del archivo**, no solo en el nombre.
Los nombres se copian y se confunden; el encabezado viaja con el
contenido.

### Git

Claude Code maneja el repositorio. Commit obligatorio:

- Después de cada transcripción incorporada
- Después de cada borrador generado
- Después de cada revisión del autor

Mensaje de commit en español, describiendo qué cambió y en qué capítulo.

---

## 9. FLUJO POR SESIÓN DE DICTADO

1. Audio a `01-dictados/audio/`
2. Whisper transcribe literal → `01-dictados/transcripciones/`
   (**la transcripción cruda nunca se borra ni se edita**)
3. Claude Code clasifica los cuatro registros
4. Claude Code genera borrador conservador con marcadores
5. Descartes a `descartes.md`, recordatorios a `por-verificar.md`
6. Commit
7. Revisión del autor
8. Si hay cambios: nueva versión, la anterior pasa a `SUPERADA`

---

## 10. PROHIBICIONES

- No inventar fuentes, citas, datos, autores, fallos ni boletines.
- No citar de memoria.
- No presentar como real un ejemplo inventado.
- No dar por ciertos los datos entre corchetes hasta confirmarlos.
- No depurar editorialmente durante la Etapa 1.
- No borrar ni editar transcripciones crudas.
- No completar un número de boletín, ley o rol que venga del dictado.
- No eliminar nada sin consultar al autor.

---

## 11. REGLA DE CONSULTA

Toda eliminación de contenido —redundancias, pasajes, fuentes
repetidas— requiere **consulta previa al autor**. Claude Code propone;
el autor decide.

Igualmente, toda propuesta de Claude Code se identifica como tal:
"punto de vista de Claude", no como hecho establecido.
