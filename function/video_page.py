import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+")
cont = request.content
soup = BeautifulSoup(cont,"html.parser")
page = {}
for page_val in soup.find_all('a', {"class": True, "data-sessionlink": True, "data-visibility-tracking": True, "aria-label": True,}):
    page['{}'.format(page_val.text)] = page_val.get('href')
print(page)
