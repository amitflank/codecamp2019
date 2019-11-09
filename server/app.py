from flask import Flask, request, jsonify, json
from flask_cors import CORS
from song_grid import Song_Grid
import reader

app = Flask(__name__)
CORS(app)

song_grid = Song_Grid()

@app.route("/")
def hello():
    print("heeeey")
    return "Flask says fuck you!"

@app.route("/initialize")
def initialize():
    data = reader.create_songs()
    a = {}
    for index, song in enumerate(data):
        a[index] = song.params
    return a

@app.route('/find_song', methods=['POST'])
def find_song():
    print("oog")
    pos = {'tempo': request.form['tempo'], 'loudness':request.form['loudness'],
    'duration': request.form['duration'], 'danceability': 0.0}
    tmp = song_grid.smart_search(pos)
    return tmp[0]

if __name__ == "__main__":
    app.run()
