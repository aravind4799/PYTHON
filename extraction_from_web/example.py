import requests

def get_rhymes(word):
    # read datamuse api for query parameters syntax
    base_url="https://api.datamuse.com/words"
    param_dict={}#set up empty dict for query
    param_dict["rel_rhy"]=word
    param_dict["max"]=3
    response=requests.get(base_url,params=param_dict)

    word_ds=response.json()

    return [d['word'] for d in word_ds]


def get_opposites(word):
    base_url="https://api.datamuse.com/words"
    dict={}
    dict["rel_ant"]=word
    resp=requests.get(base_url,dict)
    #resp=requests.get("https://api.datamuse.com/words?rel_ant=word")
    return [d['word'] for d in resp.json() ]



print(get_rhymes("funny"))
print(get_opposites("bad"))
