#Exercises: Level 1
"""Write a function which count number of lines and number of words in a text.
 All the files are in the data the folder: 
 a) Read obama_speech.txt file and count number of lines and words
  b) Read michelle_obama_speech.txt file and count number of lines and words
   c) Read donald_speech.txt file and count number of lines and words 
d) Read melina_trump_speech.txt file and count number of lines and words"""
import sys

sys.path.append("data")
import os
import json
import re
from collections import Counter
import string
from stop_words import stop_words as sw
import math
import csv


def counter(fname):
    num_words = 0
    num_lines = 0

    with open(fname, "r") as f:
        for line in f:
            line = line.strip(os.linesep)
            wordslist = line.split()
            num_lines = num_lines + 1
            num_words = num_words + len(wordslist)

    print("Number of words in text file: ", num_words)

    print("Number of lines in text file: ", num_lines)


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def most_spoken_languages(fname, value):
    f = open(fname, encoding="UTF8")
    to_analyse = json.load(f)

    total_languages_initial = []
    counts = {}
    output_list = []

    for i in to_analyse:
        total_languages_initial.extend(i["languages"])

    for i in total_languages_initial:
        counts[i] = counts.get(i, 0) + 1

    counts = sort_dict_by_value(counts, True)

    for i in list(counts.items())[:value]:
        output_list.append(i)

    f.close()

    return [(sub[1], sub[0]) for sub in output_list]
