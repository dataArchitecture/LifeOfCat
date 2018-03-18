# CSS class 에서 색상을 이용해서 데이터 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

