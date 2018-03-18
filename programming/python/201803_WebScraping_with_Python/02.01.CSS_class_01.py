# CSS class 에서 색상을 이용해서 데이터 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

nameList = bsObj.findAll("span",{"class":"green"})

for name in nameList:
    print(name.get_text())

