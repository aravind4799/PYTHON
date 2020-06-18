import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

fhand=urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Zander.html")
html_data=fhand.read()
soup=BeautifulSoup(html_data,'html.parser')
tags=soup('a')
link=tags[17].get('href',None)
print(link)

def fetch(link):
    fhand=urllib.request.urlopen(link)
    html_data=fhand.read()
    soup=BeautifulSoup(html_data,'html.parser')
    tags=soup('a')
    return tags[17].get('href',None)

for i in range(6):
    link=fetch(link)
    print(link)
