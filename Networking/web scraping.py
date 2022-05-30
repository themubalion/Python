import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('enter the url - ')
itag = input('What tag you wanna search? - ')
iattribute = input('Enter the attribute for tag - ')
html = urllib.request.urlopen(url).read()
bs = BeautifulSoup(html,'html.parser')

tags = bs(itag)
for tag in tags:
    print(tag.get('mailto',None))