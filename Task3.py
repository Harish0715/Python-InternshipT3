import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h2")

with open("headlines.txt","w",encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text:
            print(text)
            file.write(text + "\n")
            
