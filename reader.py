import pandas as pd
import json
import os
import hdf5_getters

class Song():

    def __init__(self, loudness, duration, danceability, tempo, title, hotttnesss, artist):
        self.loudness = loudness
        self.duration = duration
        self.danceability = danceability
        self.tempo = tempo
        self.title = get_title
        self.hotttnesss = hotttnesss
        self.artit = artist



def create_songs():
    h5 = hdf5_getters.open_h5_file_read('msd_summary_file.h5')
    num_songs = hdf5_getters.get_num_songs(h5)
    song_list = []

    #test = h5.root.metadata.songs.cols
    #for val in test:
#        print(val)

    for i in range(num_songs):
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
