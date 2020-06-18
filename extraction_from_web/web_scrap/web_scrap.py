
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

fhand=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_454060.html")
html=fhand.read()
soup=BeautifulSoup(html,'html.parser')
total=0
tags = soup('span')
for data in tags:
    total+=int(data.contents[0])
print(total)
