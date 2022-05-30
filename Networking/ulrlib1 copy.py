from cgitb import html
import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup


html = urllib.request.urlopen('https://www.dr-chuck.com/page1.html').read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))