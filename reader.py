import pandas as pd
import json
import os


file_list = []
for subdir, dirs, files in os.walk('lastfm_train/A/A'):
    for file in files:
        file_list.append(os.path.join(subdir, file))

song_info = []

for file in file_list:
    with open(file, 'r') as json_file:
        song_info.append(json.load(json_file))

print(song_info)
