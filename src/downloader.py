import yt_dlp
import os
from spotdl import Spotdl
from dotenv import load_dotenv
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4
from mutagen.wave import WAVE

load_dotenv()

def _edit_metadata(filename, metadata):
    """
    Edits the metadata of the downloaded audio file.
    """
    try:
        if not os.path.exists(filename):
            print(f"File not found for metadata editing: {filename}")
            return

        if filename.endswith('.mp3'):
            audio = EasyID3(filename)
        elif filename.endswith('.flac'):
            audio = FLAC(filename)
        elif filename.endswith('.m4a'):
            audio = MP4(filename)
        elif filename.endswith('.wav'):
            audio = WAVE(filename)
        else:
            print(f"Unsupported file format for metadata editing: {filename}")
            return

        for key, value in metadata.items():
            if value:
                audio[key] = value
        audio.save()
    except Exception as e:
        print(f"Error editing metadata: {e}")

def _download_from_youtube(url, output_path, audio_format, metadata=None):
    """
    Downloads and converts a video from YouTube using yt-dlp.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        final_filename = info_dict.get('requested_downloads')[0]['filepath']
        if metadata:
            _edit_metadata(final_filename, metadata)

def _download_from_spotify(url, output_path, audio_format, metadata=None):
    """
    Downloads a track from Spotify using spotdl.
    """
    spotdl = Spotdl(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        user_auth=False,
        output_format=audio_format,
        output=f"{output_path}/{{title}}.{{output-ext}}",
    )
    songs = spotdl.search([url])
    results = spotdl.download_songs(songs)
    song, path = results[0]

    if metadata:
        _edit_metadata(path, metadata)


def download_and_convert(url, output_path='./downloads', audio_format='mp3', metadata=None):
    """
    Downloads a video from a given URL and converts it to the specified audio format.
    Detects the source (YouTube or Spotify) and uses the appropriate downloader.
    """
    try:
        os.makedirs(output_path, exist_ok=True)
        if "spotify.com" in url:
            _download_from_spotify(url, output_path, audio_format, metadata)
        else:
            _download_from_youtube(url, output_path, audio_format, metadata)
        print(f"Successfully downloaded and converted.")
        return True
    except Exception as e:
        print(f"Error during download or conversion: {e}")
        return False
