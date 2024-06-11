# -*- coding: utf-8 -*-
"""webscraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iXtl75NZJUJv3ZVMS_EKiASBgSm9fc8E
"""

from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.bbc.com/news"
# fetch the content from url
response = requests.get(url)
html = response.content
 # Parse HTML content
soup = BeautifulSoup(html, 'html.parser')
 # Find elements containing headlines
elements = soup.find_all(["h2", "a"])
# Create a CSV file and write the data
with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])

    for element in elements:
        headline_text = element.text.strip()
        headline_url = element.get('href')
        writer.writerow([headline_text, headline_url])

print("Data scraping complete and saved to headlines;csv.")