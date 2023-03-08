import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
#url = 'https://github.com/FatimaMuhammadAdam/ArewaDS-30Days-of-Python/blob/main/30Days%20of%20python/day_21/day_21_class_exer.py'
response = requests.get(url)
status = requests.status_codes

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)

# store the data as a JSON file
#with open('bu_facts.json', 'w') as f:
    #json.dump(data, f, indent=4)