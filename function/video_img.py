import re
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+")
cont = request.content
soup = BeautifulSoup(cont, "html.parser")
for element in soup.find_all('a', {"rel": "spf-prefetch"}):
    img_val = element.get('href').split("=")[1]
    all_img = soup.find_all('img', {"alt": True, "width": True, "height": True, "onload": True, "data-ytimg" :True})
    img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_val), str(all_img))).strip("[\"\']")
    video_img = img.replace("&amp","&")
    print(video_img)
