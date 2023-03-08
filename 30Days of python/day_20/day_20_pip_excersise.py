#importing labries
import pandas as pd
import requests
import webbrowser
import csv
import json
from os import remove
import urllib.request
from collections import Counter
from bs4 import BeautifulSoup
import re
#Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# Read the text from the URL
url = "http://www.gutenberg.org/files/1112/1112.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# Removing symbols and characters and didiving the data
data = re.sub('[^A-Za-z]+', ' ', data)
words = data.split()

# Count the frequency of each word
word_counts = Counter(words)

# Print the 10 most common words
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#the min, max, mean, median, standard deviation of cats' weight in metric units.
#the min, max, mean, median, standard deviation of cats' lifespan in years.
#Create a frequency table of country and breed of cats
import statistics
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats_data = response.json()
#cats_data= ('/30Days of python/day_20/to/cats_data.json')
#cats_data = pd.read_json('cats_data.json')
#let extract the data
cat_weight = [cat['weight']['metric'] for cat in cats_data]
cat_lifespan = [cat ['life_span'].split()[0]for cat in cats_data]
#let perform the statistical operation on the weight data
cat_weight = [float(weight.split()[0])for weight in cat_weight ]
min_weight = min(cat_weight)
max_weight = max(cat_weight)
mean_weight = statistics.mean(cat_weight)
meadian_weight = statistics.median(cat_weight)
std_weight = statistics.stdev(cat_weight)
#let perform the statistical operation on the life span data
cat_lifespan =[int(lifespan)for lifespan in cat_lifespan]
min_lifespan = min(cat_lifespan)
max_lifespan = max(cat_lifespan)
mean_lifespan = statistics.mean(cat_lifespan)
meadian_lifespan = statistics.median(cat_lifespan)
std_lifespan = statistics.stdev(cat_lifespan)
#frequency of the cat based on the country
data_country_breed = [(cat['origin'], cat['name']) for cat in cats_data]
freq_breed_country = Counter(data_country_breed)
#LET PRINT THE WORK
print(f"weight: min={min_weight:.2f}, max ={max_weight}, mean = {mean_weight}, meadian={meadian_weight},std = {std_weight}")
print(f"Lifespan: Min = {min_lifespan}, Max = {max_lifespan}, Mean = {mean_lifespan:.1f}, Median = {meadian_lifespan}, Std Dev = {std_lifespan:.1f}")
print("Frequency table of country and breed:")
for country_breed, count in freq_breed_country.items():
    print(f"{country_breed[0]}:{country_breed[1]} - {count}")
#ead the countries API and find
"""
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API"""

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def freq_origin(data):
    origins = []
    for breed in data:
        origins.append(breed['origin'])
    print(sort_dict_by_value(dict(Counter(origins)), True))


r = requests.get('https://archive.ics.uci.edu/ml/datasets.php')
soup = BeautifulSoup(r.content, features='lxml')
print(soup.prettify())
