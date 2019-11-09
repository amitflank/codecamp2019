import pandas as pd
import json
import os
import hdf5_getters

class Song():

    def __init__(self, loudness, duration, danceability, tempo, title, hotttnesss, artist):
        self.params = {'loudness': loudness, 'duration': duration,
        'danceability': danceability,'tempo': tempo, 'title': title,
         'hotttnesss': hotttnesss, 'artist': artist }

    def get_song_param_dict(self):
        return {'loudness': self.params['loudness'], 'duration': self.params['duration'],
        'danceability': self.params['danceability'], 'tempo': self.params['tempo']}

    def __eq__(self, other):
        if self.params['title'] == other.params['title'] and self.params['artist']==other.params['artist']:
            return True
        else:
            return False
            
def create_songs():
    h5 = hdf5_getters.open_h5_file_read('msd_summary_file.h5')
    num_songs = hdf5_getters.get_num_songs(h5)
    song_list = []

    for i in range(500):
        duration = hdf5_getters.get_duration(h5, i)
        tempo = hdf5_getters.get_tempo(h5, i)
        loudness = hdf5_getters.get_loudness(h5, i)
        danceability = hdf5_getters.get_danceability(h5, i)
        artist = hdf5_getters.get_artist_name(h5, i)
        title = hdf5_getters.get_title(h5, i)
        hotttnesss = hdf5_getters.get_song_hotttnesss(h5, i)
        song_list.append(Song(loudness, duration, danceability, tempo, title, hotttnesss, artist))

    h5.close()
    return song_list
