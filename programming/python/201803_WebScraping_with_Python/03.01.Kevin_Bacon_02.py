# 이전 결과를 보면 이 링크들은 id 가 bodyContent인 div 안에 있습니다.
# URL에는 세미콜론이 포함되어 있지 않습니다.
# URL은 /wiki/로 시작합니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(), "html.parser")

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# ^ : 바로 뒤에 있는 문자 혹은 하위 표현식이 문자열의 맨 앞에 나타납니다.
# () : 하위 표현식. 묶음으로 처리
# ?! : 다음 문자나 하위표현식은 이 위치에 나오지 않습니다. (특정 문자를 완전히 배제하려면 ^,$를 앞 뒤에 써야 함)
# . : 문자 하나가 나타남
# * : 앞의 문자가 여러 반복해서 나타남
# $ : 앞의 문자 or 하위 표현식이 문자열의 마지막
