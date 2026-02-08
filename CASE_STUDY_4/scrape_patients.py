import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:5000/")
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")[1:]

for r in rows:
    cols = r.find_all("td")
    print({
        "Name": cols[0].text,
        "Age": cols[1].text,
        "Disease": cols[2].text,
        "Doctor": cols[3].text
    })
