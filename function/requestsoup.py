import  requests
from  bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=+Ultimate+Nightcore+Gaming+") #get url
cont = request.content #content 找出編碼
soup = BeautifulSoup(cont,"html.parser") # (content,HTML 解析)
print(soup)