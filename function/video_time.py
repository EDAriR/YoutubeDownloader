import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+")
cont = request.content
soup = BeautifulSoup(cont,"html.parser")
for time in soup.find_all('span',{"class": "video-time"}):
    print(time.text)