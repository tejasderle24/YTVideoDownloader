from flask import Flask, render_template, request, redirect, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('Please enter a valid YouTube URL.')
            return redirect('/')

        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            flash('Video downloaded successfully!')
        except Exception as e:
            flash(f'Error: {str(e)}')

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
