import urllib.request as req
import xml.etree.ElementTree as et

fhand=req.urlopen("http://py4e-data.dr-chuck.net/comments_454062.xml")

data=fhand.read()
#print(data)
total=0
tree=et.fromstring(data)
#fromstring takes the xml data and generates a tree structure
lst=tree.findall('comments/comment')
#print(lst)
#findall searchs the tree using the given Xpath and returns a list of comments
for item in lst:
    #now iterate through each comment to extract data from count tag using find method.
    total+=int(item.find('count').text)
print(total)
