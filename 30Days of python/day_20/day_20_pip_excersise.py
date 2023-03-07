#importing labries
import pandas as pd
import requests
import webbrowser
import csv
import json
from os import remove

#Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
df = pd.read_html(requests.get(romeo_and_juliet).content)[3]
