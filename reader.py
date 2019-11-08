import pandas as pd
import json
import os

def read_folder(folder_name):
    file_list = []
    for subdir, dirs, files in os.walk(folder_name):
        for file in files:
            file_list.append(os.path.join(subdir, file))

            song_info = []

    for file in file_list:
        with open(file, 'r') as json_file:
            song_info.append(json.load(json_file))

    return song_info
