import requests
import json

def get_movies_from_tastedive(movie_name):
    lst=[]
    base_url="https://tastedive.com/api/similar"
    p_dict={}
    p_dict["q"]=movie_name
    p_dict["limit"]=5
    p_dict["type"]="movies"
    page=requests.get(base_url,params=p_dict)
    py_data=json.loads(page.text)
    return py_data

def extract_movie_titles(dictt):
    lst=[]
    for val in dictt['Similar']['Results']:
        lst.append(val['Name'])
    return lst

def get_related_titles(lst):
    new_lst=[]
    for movie in lst:
        for related_movie in extract_movie_titles(get_movies_from_tastedive(movie)):
            if related_movie not in new_lst:
                new_lst.append(related_movie)
    return new_lst

def get_movie_data(movie_name):
    #API_KEY=3461bf8e
    base_url="http://www.omdbapi.com/?apikey=3461bf8e&r=%22json%22&t={}".format(movie_name)
    response=requests.get(base_url)
    dictt=json.loads(response.text)
    return dictt


def get_movie_rating(resp):
    val=0
    for dictt in resp['Ratings']:
        if dictt['Source'] is "Rotten Tomatoes":
            val=int(dictt['Value'].replace("%"," "))
    return val

def get_sorted_recommendations(lst):
    ans=[]
    related_movies=get_related_titles(lst)
    ratings=[]

    for movie in related_movies:
        ratings.append(get_movie_rating(get_movie_data(movie)))

    temp_tuple=list(zip(related_movies,ratings))
    #print(temp_tuple)
    temp_tuple=sorted(temp_tuple,key=lambda x:x[0],reverse=True)
    temp_tuple=sorted(temp_tuple,key=lambda x:x[1],reverse=True)

    for item in temp_tuple:
        ans.append(item[0])
    return ans
app=get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
print(app)
