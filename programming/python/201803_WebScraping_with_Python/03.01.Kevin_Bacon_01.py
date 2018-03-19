# 위키 검색 해보기

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(), "html.parser")

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
