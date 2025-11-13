from flask import Flask, render_template, request, redirect, url_for, flash
from downloader import download_and_convert

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    urls = request.form['urls'].splitlines()
    audio_format = request.form['format']

    metadata = None
    if len(urls) == 1:
        metadata = {
            'title': request.form['title'],
            'artist': request.form['artist'],
            'album': request.form['album'],
        }
    elif request.form['title'] or request.form['artist'] or request.form['album']:
        flash('Custom metadata can only be applied to single file downloads.', 'warning')

    success_count = 0
    error_count = 0

    for url in urls:
        if url.strip(): # Ignore empty lines
            if download_and_convert(url, audio_format=audio_format, metadata=metadata):
                success_count += 1
            else:
                error_count += 1

    flash(f'{success_count} downloads succeeded, {error_count} failed.', 'info')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
