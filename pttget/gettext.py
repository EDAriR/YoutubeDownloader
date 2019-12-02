import requests
from bs4 import BeautifulSoup
from scipy.misc import imread

import ç.pyplot as plt
import jieba
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
from wordcloud import WordCloud, ImageColorGenerator
from jieba.analyse import extract_tags

res = requests.get('https://www.ptt.cc/bbs/Lifeismoney/M.1542512557.A.2AA.html')

soup = BeautifulSoup(res.text, 'html.parser')


tee = soup.text

import jieba

seg_list = jieba.cut(tee, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(tee, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(tee)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(tee)  # 搜索引擎模式
print(", ".join(seg_list))