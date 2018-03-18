# 현재 python 3.5.2 버전으로 아나콘다 설치 환경에서 작업을 하고 있음
# 기본적인 라이브러리는 다 설치되었을 것으로 예상


# urllib 테스트
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

# BeautifulSoup 실행 테스트
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)

