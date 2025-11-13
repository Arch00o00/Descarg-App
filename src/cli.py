import argparse
from rich.console import Console
from rich.progress import Progress
from downloader import download_and_convert

def main():
    """
    The main function for the command-line interface.
    """
    parser = argparse.ArgumentParser(description="Download and convert videos to audio.")
    parser.add_argument("urls", nargs='*', help="One or more video URLs to download.")
    parser.add_argument("-i", "--input-file", help="A file containing a list of URLs to download.")
    parser.add_argument("-f", "--format", default="mp3", help="The audio format to convert to (mp3, wav, flac, alac).")
    parser.add_argument("-o", "--output", default="./downloads", help="The output directory.")
    parser.add_argument("--title", help="The title of the audio (only works for single file downloads).")
    parser.add_argument("--artist", help="The artist of the audio (only works for single file downloads).")
    parser.add_argument("--album", help="The album of the audio (only works for single file downloads).")

    args = parser.parse_args()

    urls = args.urls
    if args.input_file:
        with open(args.input_file, 'r') as f:
            urls.extend(f.read().splitlines())

    if not urls:
        parser.error("No URLs provided. Please provide at least one URL directly or via an input file.")

    console = Console()

    metadata = None
    if len(urls) == 1:
        metadata = {
            'title': args.title,
            'artist': args.artist,
            'album': args.album,
        }
    elif args.title or args.artist or args.album:
        console.print("[yellow]Warning: Custom metadata can only be applied to single file downloads.[/yellow]")

    with Progress() as progress:
        task = progress.add_task("[cyan]Processing URLs...", total=len(urls))

        for url in urls:
            success = download_and_convert(url, args.output, args.format, metadata=metadata)
            if not success:
                console.print(f"[red]Failed to process URL: {url}[/red]")
            progress.update(task, advance=1)

    console.print("[green]All downloads and conversions complete![/green]")

if __name__ == "__main__":
    main()
