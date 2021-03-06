# 내가 수집하려는 사이트는 어떤 곳이지? 몇 개만? 아니면 존재 조차 모르는 사이트도 방문해야 할까?
# 크롤러가 특정 웹사이트에 도착하면 새 웹사이트를 찾아가야 할까? 아니면 현재 웹 사이트를 파고들어야 할까?
# 특정 웹 사이트를 제외해야 하나? 비영어권도 탐색해야 하는가?
# 특정 웹 사이트가 크롤러의 방문을 인지했을 경우에 나 자신을 법적으로 보호할 수 있을까?

from urllib.request import urlopen
from urllib.parse import urlparse   ## 정오표 추가 라인
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 페이지에서 발견된 내부 링크를 모두 목록으로 만든다.
def getInternalLinks(bsObj, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []

    # /로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):                      ## 정오표에서 if 문장 추가
                    internalLinks.append(includeUrl+link.attrs['href']) 
                else: 
                    internalLinks.append(link.attrs['href']) 
    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http 나 www 로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)  ## 정오표로 추가한 라인
#    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0]) ## 정오표로 삭제한 라인
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bsObj, domain)                             ## 정오표 추가 라인
#        internalLinks = getInternalLinks(bsObj, startingPage)                      ## 정오표 삭제 라인
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])   ## 정오표로 수정한 라인
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")
