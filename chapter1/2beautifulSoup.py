from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# explicitly specify parser
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.h1)