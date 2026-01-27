import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get (url)
print (response.status_code)
content = response.content
soup = BeautifulSoup(content,'html.parser')
# print (soup.body)
# json_data = json.loads(soup.body.get_text())
with open(r"22_Day_Web_scraping/bu_facts_stats.json", "w", encoding="utf-8") as f:
        json.dump(soup.body, f, indent=4, ensure_ascii=False)