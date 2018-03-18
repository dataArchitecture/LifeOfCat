# 책에서 기본 오브젝트를 가져오는 부분을 만듦
## getSiteHTML : html 오브젝트 생성
## getTitle : 타이틀 정보 가져옴


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getSiteHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

def getTitle(html):
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title


