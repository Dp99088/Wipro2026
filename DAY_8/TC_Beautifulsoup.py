import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

pagetitle = soup.title.string if soup.title else "No title"
print(pagetitle)
