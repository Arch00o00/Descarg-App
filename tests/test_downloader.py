import unittest
from unittest.mock import patch
from src.downloader import download_and_convert

class TestDownloader(unittest.TestCase):
    @patch('src.downloader._download_from_youtube')
    @patch('src.downloader._download_from_spotify')
    def test_download_and_convert_youtube(self, mock_spotify, mock_youtube):
        download_and_convert('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        mock_youtube.assert_called_once()
        mock_spotify.assert_not_called()

    @patch('src.downloader._download_from_youtube')
    @patch('src.downloader._download_from_spotify')
    def test_download_and_convert_spotify(self, mock_spotify, mock_youtube):
        download_and_convert('https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC')
        mock_spotify.assert_called_once()
        mock_youtube.assert_not_called()

if __name__ == '__main__':
    unittest.main()
