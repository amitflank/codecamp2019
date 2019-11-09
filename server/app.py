from flask import Flask, request, json
from song_grid import Song_Grid
import reader

app = Flask(__name__)

song_grid = Song_Grid()

@app.route("/initialize")
def hello():
    return reader.create_songs()

@app.route('/find_song', methods=['POST'])
def find_song():
    pos = {'tempo': request.forms['tempo'], 'loudness':request.form['loudness'],
    'duration': request.form['duration'], 'danceability': 0.0}
    tmp = song_grid.smart_search(pos)
    return tmp[0]

if __name__ == "__main__":
    app.run()
