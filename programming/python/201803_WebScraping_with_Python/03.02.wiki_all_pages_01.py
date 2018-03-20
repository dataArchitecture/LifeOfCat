# 이전 결과를 보면 이 링크들은 id 가 bodyContent인 div 안에 있습니다.
# URL에는 세미콜론이 포함되어 있지 않습니다.
# URL은 /wiki/로 시작합니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 페이지를 발견했을 때
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
