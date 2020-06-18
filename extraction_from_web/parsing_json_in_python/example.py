import urllib.request as req
import json

fhand=req.urlopen("http://py4e-data.dr-chuck.net/comments_454063.json")
total=0
data=fhand.read().decode()
# data from the external web is in utf-8 format which needs to be converted into unicode format used in python
dictt=json.loads(data)
#print(dictt)
# inorder to pretty print
pretty_data=json.dumps(dictt, indent=2)
#print(pretty_data)
#print(dictt.keys())
for item in dictt['comments']:
    total+=item['count']
print(total)
