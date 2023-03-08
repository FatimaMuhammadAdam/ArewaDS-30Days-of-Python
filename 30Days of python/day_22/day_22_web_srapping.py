
import requests
from bs4 import BeautifulSoup
import json

# specify the URL of the website to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the table element with the class 'facts-table'
table = soup.find('table', {'class': 'facts-table'})

# extract the data from the table
data = {}
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 2:
        key = cells[0].text.strip()
        value = cells[1].text.strip()
        data[key] = value

# store the data as a JSON file
with open('bu_facts.json', 'w') as f:
    json.dump(data, f, indent=4)


#question two
#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

import pandas as pd
url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)
html_contents =response.content
soup = BeautifulSoup(html_contents, "html.parser")

table = soup.find("table", {"class": "wikitable sortable"})
df = pd.read_html(str(table))[0]


#to change it json 
json_df = df.to_json(oreint = "record")

with open("data.json", "w") as outfile:
    outfile.write(json_df)
    
