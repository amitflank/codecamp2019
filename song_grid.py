import os
import sys
import glob
import time
import datetime
import numpy as np
import reader
from copy import deepcopy
from math import floor
import math
#https://www.geeksforgeeks.org/python-program-for-binary-insertion-sort/
def binary_search(arr, val, start, end, axis):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start].params[axis] > val.params[axis]:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = floor((start+end) / 2)

    if arr[mid].params[axis] < val.params[axis]:
        return binary_search(arr, val, mid+1, end, axis)
    elif arr[mid].params[axis] >  val.params[axis]:
        return binary_search(arr, val, start, mid-1, axis)
    else:
        return mid

def binary_search2(arr, val, start, end, axis):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start].params[axis] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = floor((start+end) / 2)

    if arr[mid].params[axis]  < val:
        return binary_search2(arr, val, mid+1, end, axis)
    elif arr[mid].params[axis]  >  val:
        return binary_search2(arr, val, start, mid-1, axis)
    else:
        return mid

def insertion_sort(arr, axis):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1, axis)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr


class Song_Grid():

    def __init__(self):
        self.axis = {'loudness':[], 'duration': [], 'tempo': [], 'danceability': []}
        self.add_all_songs()
        self.calculate_adj_factors()

    def calculate_adj_factors(self):
        self.adj_factors = {}
        for key, _ in self.axis.items():
            last = self.axis[key][-1].params[key]
            first = self.axis[key][0].params[key]
            self.adj_factors[key] = abs(last - first)

    #sort our axis
    def sort_axis(self):
        for key, _ in self.axis.items():
            self.axis[key] = insertion_sort(self.axis[key], key)

    def add_song(self, song):
        for key, _ in self.axis.items():
            self.axis[key].append(song)

    def add_all_songs(self):
        song_list = reader.create_songs()

        for song in song_list:
            self.add_song(song)

        self.sort_axis()


    def get_closest_idx(self, axis_copy, key, pos):
        idx = binary_search2(axis_copy[key], pos[key], 0, len(axis_copy[key]) - 1, key)

        valid_right = True
        if idx == len(axis_copy[key]):
            idx -= 1
            valid_right = False
        diff = abs(pos[key] - axis_copy[key][idx].params[key])
        clossest_idx = idx

        if idx > 0:
            left = idx - 1
            tmp = abs(pos[key] - axis_copy[key][left].params[key])
            if tmp < diff:
                clossest_idx = left
                diff = tmp

        if valid_right:
            right = idx + 1
            tmp = abs(pos[key] - axis_copy[key][right].params[key])
            if tmp < diff:
                clossest_idx = right
                diff = tmp

        return clossest_idx, diff

    def calculate_dist(self, pos, params):
        sum_diff = 0

        for key in pos:
            diff = (params[key] - pos[key]) / (self.adj_factors[key] + .01) #aviod /0
            sum_diff += (diff * diff)

        return math.sqrt(sum_diff)


    def smart_search(self, pos):
        closest_idx = {}
        closest_diff = {}

        axis_copy = deepcopy(self.axis)

        for key, _ in axis_copy.items():
            closest_idx[key], closest_diff[key]  = self.get_closest_idx(axis_copy, key, pos)

        min_diff = self.calculate_dist(pos, closest_diff)
        best_diff = [None, 1000000000000096]
        dist = -1

        while(dist != best_diff[1]):
            for key, _ in axis_copy.items():
                cur_param = axis_copy[key][closest_idx[key]].get_song_param_dict() #get song at closses idx for key
                dist = self.calculate_dist(pos, cur_param)


                if dist < best_diff[1]:
                    best_diff[0] = axis_copy[key][closest_idx[key]] #current song
                    best_diff[1] = dist

                del axis_copy[key][closest_idx[key]]
                closest_idx[key], closest_diff[key] = self.get_closest_idx(axis_copy, key, cur_param)
                min_diff = self.calculate_dist(pos, closest_diff)


        return best_diff

    def remove_song(self, song, axis_copy):
        for key, _ in axis_copy.items():
            for idx, val in enumerate(axis_copy[key]):
                    if song == axis_copy[key][idx]:
                        del axis_copy[key][idx]

    def get_nearest_n_songs(self, song, num_songs):
            n_song = song
            song_list = []
            idx = self.axis['loudness'].index(song)
            axis_copy = deepcopy(self.axis)
            for i in range(num_songs):
                self.remove_song(n_song, self.axis)
                tmp = self.smart_search(n_song.get_song_param_dict())
                song_list.append(tmp[0])
                n_song = tmp[0]

            self.axis = axis_copy
            return song_list

    def find_transform_song(self, song, transform):
        new_pos = {}
        for key, val in song.params.items():
            new_pos[key] = val + transform[key]

        return smart_search(new_pos)
