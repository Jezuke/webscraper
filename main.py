from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# TODO Make plan to extract vocab
req = Request( url="https://junyu.org/study/vocab/",headers={'User-Agent':'Edge/135.0.3179.54'})
page = urlopen(req)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div")

for div in divs:
    print(div["class"])
