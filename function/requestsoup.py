import  requests
from  bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/watch?v=WsdO93LCvDo") #get url
cont = request.content #content 找出編碼
soup = BeautifulSoup(cont,"html.parser") # (content,HTML 解析)
print(soup)

qq = soup.findAll('meta' ,{"property": 'og:title'})[0]
print(type(qq))
print(qq['content'])