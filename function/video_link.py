import  requests
from  bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+") #get url
cont = request.content #content 找出編碼
soup = BeautifulSoup(cont,"html.parser") # (content,HTML 解析)
for element in soup.find_all('a',{"rel":"spf-prefetch"}): #for迴圈找全部搜尋出來的youtube title 標籤<a...rel=spf-prefetch...
   print(element)
   video_title = element.get('title')
   video_link = element.get('href') #html 語法 herf 連結
   print(video_title)
   print("https://www.youtube.com{}".format(video_link))