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
   
   
   def most_populated_countries(fname, value):
    f = open(fname, encoding="UTF8")
    list_data = json.load(f)
    populations = {}
    final = []

    for i in list_data:
        populations[i["name"]] = i["population"]

    populations = sort_dict_by_value(populations, True)

    for data in list(populations.items())[:value]:
        final.append({"Country": data[0], "Population": data[1]})

    f.close()

    return final


# print(most_spoken_languages(fname="data\countries_data.json", value=3))
# print(most_populated_countries(fname="data\countries_data.json", value=3))

#level 2

def list_of_words(fname):
    output = []
    with open(fname, "r", encoding="UTF8") as file:
        for line in file:
            for word in line.split():
                output.append(word)
    return list(set(output))


def check_email(word):
    if re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", word):
        return True
    else:
        return False


def extract_emails(fname):
    words = list_of_words(fname)
    email_list = []

    for word in words:
        if check_email(word):
            email_list.append(word)

    return email_list
