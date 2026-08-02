# Producción de video — Fundación Soy del Campo

Instrucciones para Claude Code. Cómo se arma un video de tomas grabadas a
cámara: empalme, versión sobria para envío directo, versión para redes con
subtítulos.

Nace del video a diputados sobre la prohibición de carreras de galgos
(agosto 2026). Todo lo que dice acá está probado en ese trabajo.

---

## 0. Antes de tocar nada

**Las herramientas están en el entorno, no hay que instalar casi nada.**

| Qué | Dónde |
|---|---|
| ffmpeg | `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2` |
| Fuentes | `/mnt/skills/examples/canvas-design/canvas-fonts/` |
| Reconocimiento de voz | sherpa-onnx + whisper-small int8 |
| Composición de imagen | Pillow (`pip install Pillow`) |
| Componentes conexas | scipy (`pip install scipy`) |

**Dos cosas que este ffmpeg NO tiene:**

- **`drawtext` no está compilado.** No sirve para poner texto. Se usa
  `subtitles` (libass, sí está) o se dibuja con Pillow y se monta con
  `overlay`.
- `ffprobe` no viene. Para medir duración exacta:
  `ffmpeg -i x.mp4 -map 0:v -c copy -f null -` y leer el último `time=`.

**Los archivos que sube el autor caen en**
`/root/.claude/uploads/<sesión>/`. Las imágenes **pegadas** en el mensaje no
llegan ahí: se ven pero no existen como archivo. Hay que pedirlas como
adjunto o dentro de un `.zip`.

**El proxy bloquea Dropbox** (`dropboxusercontent.com`, `www.dropbox.com`).
El conector de Dropbox sirve para *encontrar* archivos, no para bajarlos. No
intentar rodear el proxy.

---

## 1. Empalmar las tomas

### 1.1 Medir antes de cortar

```
ffmpeg -i toma.mp4 -af "silencedetect=noise=-35dB:d=0.30" -f null -
```

Da los silencios. El primero y el último son la cola de grabación: hay que
sacarlos. En el trabajo de galgos había tomas con **5,3 segundos de nada** al
principio.

Dejar **0,25 s de entrada y 0,30 s de salida** en cada toma. Eso es lo que
necesita la disolvencia para caer sobre el silencio y no sobre una palabra.

### 1.2 Emparejar el volumen

Esto es lo que más delata un pegado, más que la imagen. Dos pasadas:

```
# medir
ffmpeg -ss A -to B -i toma.mp4 -vn -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -
# aplicar en modo lineal con lo medido
-af "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=...:measured_TP=...:\
measured_LRA=...:measured_thresh=...:linear=true"
```

**Modo lineal, no dinámico.** Si las tomas ya están parejas —menos de 3 dB de
diferencia— el modo dinámico bombea y se nota.

### 1.3 Unir con disolvencia

```
[0:v][1:v]xfade=transition=fade:duration=0.25:offset=<acumulado - 0.25>
[0:a][1:a]acrossfade=d=0.25:c1=tri:c2=tri
```

El `offset` es acumulativo: cada disolvencia consume 0,25 s del total.

**`xfade` exige cuadro constante.** Si antes hubo `trim`, hay que reponer
`fps=30,settb=AVTB` en cada rama o falla con
*«current rate of 1/0 is invalid»*.

### 1.4 Comprobar los empalmes

Sacar tres cuadros por empalme —antes, medio, después— y montarlos en una
hoja de contactos con `tile`. Se revisa que calcen posición, luz y encuadre.

```
ffmpeg -pattern_type glob -i "empalmes/*.png" -filter_complex "tile=3x5:margin=6:padding=6" -frames:v 1 hoja.png
```

**No se puede juzgar el ritmo así.** Los cuadros sueltos dicen si el corte
calza; el ritmo lo juzga el autor viendo el video.

---

## 2. Acortar las pausas internas

Las pausas de más de 0,9 s dentro de una toma arrastran. Se recortan a 0,45 s
sin tocar una palabra:

- Detectar con `silencedetect=noise=-35dB:d=0.9`
- Partir el video dejando **0,325 s a cada lado** de la pausa
- Unir con `xfade` de 0,2 s → queda 0,45 s de silencio

**Consultar antes.** Algunas pausas están puestas a propósito —la que sigue a
«sin embargo» hace trabajo—. El protocolo del proyecto exige preguntar antes
de eliminar contenido.

---

## 3. Versión sobria (envío directo a una persona)

Cuadrado, 720 × 720. Solo tres elementos:

- **Zócalo de identificación** en los primeros 7 segundos: nombre y cargo,
  abajo a la izquierda.
- **Alguna lista** en el momento que corresponda, si hay que enumerar algo
  que de oído no se retiene.
- **Placa de cierre** con la petición, sostenida 5 segundos al final.

Todo dibujado con Pillow sobre lienzo transparente y montado con `overlay`
más `enable`/`setpts`. Degradado suave abajo (`scrim`) para que el blanco se
lea sobre ropa clara.

**Lo que no va en esta versión:** subtítulos karaoke, colores neón, zooms,
material de archivo. Si la pieza refuta a los influencers, no puede parecerse
a un video de influencer.

---

## 4. Versión para redes (TikTok, Reels)

### 4.1 Formato

**Vertical 720 × 1280, a sangre.** Nada de barras negras ni fondo
desenfocado: se amplía el cuadrado y se recorta por los lados.

```
scale=1280:1280:flags=lanczos,crop=720:1280:280:0,setsar=1
```

**Comprobar antes que el recorte no corte la cabeza.** Sacar un cuadro y
mirarlo. Si corta, bajar a `scale=1120` y dejar una franja abajo.

### 4.2 Subtítulos — las cinco reglas que costó aprender

**a) La altura de la letra nunca cambia.**
El error natural es armar los trozos contando letras y achicar los que no
caben. Eso castiga justo a las palabras largas —«espaldarazo»,
«investigación»— que quedan diminutas. Lo correcto: **cuerpo fijo (142) y
condensado horizontal (`\fscx`) cuando no cabe.** Alto constante, ancho
variable.

**b) Los trozos se arman por ancho medido, no por número de palabras.**
Con Pillow se mide el ancho real del texto en la fuente y se agrega palabra
por palabra mientras quepa. Máximo tres.

**c) Palabra activa en ámbar.**
Un `Dialogue` por palabra: el trozo completo, con la palabra que se está
diciendo en `\c&H00C8FF&` y las demás en blanco. No se usa `\k` (karaoke)
porque deja las palabras ya dichas coloreadas.

**d) Palabras clave solas y gigantes.**
Se sacan del flujo, van solas, en mayúscula, hasta 240 pt, condensadas hasta
el 62%.

> **Mientras más corta la palabra, más golpea.** A 720 de ancho, una palabra
> de 4-5 letras llega a 240 pt; una de 13 no pasa de 140 y no vale la pena
> como clave. `FUERA` y `NADA` funcionan; `INVESTIGACIÓN` no.

Quitarles el punto o la coma final: se comen ancho y obligan a achicar.

Emphasizar **solo la primera aparición** de cada clave. Si «canal» sale tres
veces y se agranda las tres, deja de significar algo.

Una cada diez o quince segundos. Si todo grita, nada grita.

**e) Los nombres propios NO se hacen con libass.**
Con `BorderStyle=3` (caja opaca) libass dibuja **una cajita por carácter**, y
al condensar quedan rendijas verticales. Se nota y se ve mal.

Se dibujan con Pillow: rectángulo blanco redondeado, texto negro, condensado
por `resize` horizontal. Altura fija para todas —si se usa el `bbox` del
texto, las tildes de `GONZÁLEZ` hacen la placa más alta que la de `MUSANTE`—.
Se montan con `overlay`.

### 4.3 Márgenes y posición

- Laterales: **16 px**. Menos se ve forzado.
- Vertical: `MarginV=132`, o sea unos 54 px más arriba de lo natural.

**Razón:** TikTok y Reels tapan la franja inferior con el nombre de usuario,
el texto del post y la música — más o menos los últimos 180 px de un video de
1280. Texto pegado al borde queda debajo de la interfaz.

### 4.4 Movimiento

Un plano fijo de tres minutos no aporta nada visualmente. El texto tiene que
dar el pulso:

```
{\fscx<90% del destino>\fscy90\t(0,95,\fscx<destino>\fscy100)}
```

**Solo en la primera palabra de cada trozo.** Si se anima cada palabra, tirita.

Contorno 9, sombra 5. Sin recuadro: el degradado de abajo basta.

### 4.5 Logo

Si el PNG no tiene transparencia real —fondo negro sólido—, **no intentar
quitárselo automáticamente.** Los logos suelen tener negro también adentro
(siluetas, contornos) y el borrado se los come. Comprobar así:

```python
a = Image.open(f).convert("RGBA").split()[3]
print(a.getextrema())     # (255,255) = no hay transparencia
```

Solución: meterlo en una **tarjeta redondeada oscura** y montarla arriba a la
derecha. El logo queda íntegro y se lee como marca de agua.

### 4.6 Audio para teléfono

El parlante de un celular no tiene graves. La cadena que funcionó:

```
highpass=f=90,
afftdn=nr=8:nf=-30,
equalizer=f=260:t=q:w=1.1:g=-2.5,      # saca el barro de la voz masculina
equalizer=f=3200:t=q:w=1.3:g=3.5,      # banda de la consonante: inteligibilidad
equalizer=f=8000:t=h:g=2,              # aire
acompressor=threshold=-21dB:ratio=3:attack=8:release=180:makeup=2,
alimiter=limit=0.94,
loudnorm=I=-14:TP=-1.5:LRA=11:...:linear=true,
volume=-1.3dB
```

Objetivo: **−15 LUFS con pico en −1,5 dBTP.** Ahí es donde TikTok e Instagram
quieren el audio; más fuerte y lo re-comprimen mal.

Comprobar el resultado midiendo, no de oído:
`ffmpeg -i final.mp4 -vn -af loudnorm=print_format=json -f null -`

El rango dinámico (`LRA`) debe bajar. Si pasa de 4 a 2 dB, ya no hay partes
que se oyen más bajo que otras.

---

## 5. Transcribir para subtitular

**Esta es la parte donde se cometen los errores caros.**

### 5.1 El reconocimiento automático no sirve para nombres

whisper-small sobre audio de teléfono devuelve «Camila sozando»,
«Ole-Yuan», «soscanuñquer». Escrito en pantalla, en un video público, un
apellido mal puesto es munición gratis para el otro lado.

**Los nombres se escriben a mano y los confirma el autor.** Incluidas las
tildes: si el autor escribió «sagardia» sin tilde, preguntar antes de poner
«SAGARDÍA».

### 5.2 Ventanas largas, no segmentos cortos

Decodificar segmento por segmento **empeora mucho** el resultado: sin
contexto, whisper alucina. Ventanas de 21-24 s con solape dan texto
utilizable.

Aun así, algunas ventanas fallan —se ponen a traducir al inglés o entran en
bucle—. Hay que detectarlas y volver a pasarlas con otros límites.

### 5.3 El método que funciona

1. **Tiempos** de `silencedetect` (`noise=-33dB:d=0.16`). Son exactos.
2. **Texto** de las ventanas largas, corregido a mano.
3. **Bloques** de 15-25 s, cada uno con su lista de segmentos de habla y su
   texto limpio.
4. Dentro del bloque, repartir las palabras **proporcional al largo**
   (`len(palabra) + 1.6`), sobre el tiempo de habla, **saltándose los
   silencios**.

Los silencios absorben la deriva. Dentro de un bloque de 20 s el error queda
por debajo de un segundo.

**Verificar los límites de bloque** decodificando ventanas cortas en los
puntos dudosos y comprobando que la palabra que cae en ese instante sea la
que corresponde.

---

## 6. Entrega

- **Menos de 30 MB** para poder mandarlo por el canal de la sesión.
  Dos pasadas: `-b:v 850k -maxrate 1000k -bufsize 2000k` más `-b:a 96k` deja
  unos 24 MB en 3 minutos y medio.
- `-movflags +faststart` siempre.
- Guardar el master en calidad alta (`-crf 18`) aparte del archivo de envío.

---

## 7. Lo que hay que decirle al autor

- **Qué no se puede ver.** Se revisan cuadros sueltos, no el movimiento. El
  ritmo lo juzga él.
- **Qué se perdió.** Si el material llegó por WhatsApp viene a 368 × 368; el
  detalle no vuelve. Pedir los originales **como documento**.
- **Qué falta verificar.** Todo nombre, cifra, fecha o número de boletín que
  aparezca en pantalla, marcado y consultado antes de publicar.
- **Qué decisión es suya.** Eliminar contenido, cambiar el registro, o
  cualquier cosa que altere lo que él dijo.
