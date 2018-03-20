# 모든 페이지는 제목이 h1 태그에 있으며, 페이지당 하나만 존재합니다.
# 모든 바디 텍스트는 div#bodyContext 태그에 들어 있습니다. 더 정확하게 본다면 div#mw-context-text -> p로 첫번째 문단만 선택하는 것이 좋습니다.
# 편집 링크가 항목 페이지에만 존재합니다. 존재한다면 li#ca-edit -> span -> a 로 찾을 수 있습니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id = "mw-content-text").findAll("p")[0]) # body 의 첫번째 항목만 가져오게 
        print(bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 페이지를 발견했을 때
                newPage = link.attrs['href']
                print("--\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
