# 🎵 YouStream2Audio

Convierte videos y música de plataformas de streaming a formatos de audio de alta calidad.

## 📌 Descripción

**YouStream2Audio** es una herramienta diseñada para descargar videos y pistas de servicios populares como YouTube, Spotify, YouTube Music y otros sitios de streaming, con el fin de convertirlos fácilmente a formatos de audio como **MP3**, **WAV**, **FLAC** y **ALAC**.

Este programa está desarrollado en **Python** y puede ejecutarse tanto localmente como a través de una interfaz web sencilla. El objetivo es ofrecer una solución flexible, moderna y multiplataforma para tus necesidades de conversión de audio.

## 🚀 Funcionalidades principales

- Descargar contenido de distintas plataformas (YouTube, Spotify, YouTube Music, etc.)
- Conversión de archivos a MP3, WAV, FLAC y ALAC
- Opción de interfaz de línea de comandos o interfaz web simple
- Descarga y conversión simultánea en lote
- Selección de calidad de salida y metadatos personalizables

## 🛠️ Tecnologías y dependencias

- Python 3.8+
- Librerías recomendadas:
  - `yt-dlp`
  - `spotdl`
  - `ffmpeg-python`
  - `Flask` o `FastAPI` (para la versión web)
  - `rich` (para mejorar la CLI)
- `ffmpeg` (para la conversión de formatos)
- Docker (opcional, para empaquetar la app)

## 📦 Instalación (provisional)

Clona este repositorio:

```bash
git clone https://github.com/tuusuario/YouStream2Audio.git
cd YouStream2Audio
```

## 🚀 Despliegue

Para desplegar esta aplicación en un servicio de alojamiento como Heroku o Render, sigue estos pasos:

1.  **Crea una cuenta** en la plataforma de tu elección.
2.  **Crea una nueva aplicación** y conéctala a este repositorio de GitHub.
3.  **Configura las variables de entorno**:
    *   `SPOTIFY_CLIENT_ID`: Tu client ID de Spotify.
    *   `SPOTIFY_CLIENT_SECRET`: Tu client secret de Spotify.
4.  **Añade los buildpacks necesarios**:
    *   `heroku/python`
    *   `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
5.  **Despliega la aplicación**. La plataforma instalará las dependencias y ejecutará la aplicación usando el `Procfile`.
