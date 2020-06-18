import urllib.request as req,urllib.parse as parse
import json

url="http://py4e-data.dr-chuck.net/json?"
params=dict()
params['address']="Beloit College"
params['key']=42
final_url_to_hit=url+parse.urlencode(params)

fhand=req.urlopen(final_url_to_hit)
data_read=fhand.read().decode()
dictt=json.loads(data_read)
data=json.dumps(dictt,indent=2)
##print(data)#data is a string
#print(dictt.keys())
#print(type(dictt['results']))
for item in dictt['results']:
     ans=item["place_id"]
print(ans)
