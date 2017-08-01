import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+") #get url
cont = request.content #content 找出編碼
soup = BeautifulSoup(cont,"html.parser") # (content,HTML 解析)
for element in soup.find_all('a',{"rel":"spf-prefetch"}): #搜尋出來的youtube title 標籤<a...rel=spf-prefetch...
   #print(element)
   video_title = element.get('title')
   print(video_title)