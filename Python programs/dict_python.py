from collections import Counter,defaultdict
def checkMagazine(magazine, note):

    ##############  SOLUTION1##########################
    ###### note capital C for Counter function
    #if(Counter(note)-Counter(magazine)=={}):
    #    print("Yes")
    #else:
    #    print("No")
    ####################################################


    ################### SOLUTION2 ####################################
    ##################################################################
    #d=defaultdict(int)
    #this means? we are creating a dictionary and if a key value is not found in a search , then key:0(as given default value as int)
    #will be inserted into the dictionary
    #flag=0
    #for word in magazine:
    #    d[word]+=1
    #for word in note:
    #    if d[word]==0:
    #        print("No")
    #        flag=1
    #        break
    #    d[word]-=1
    #if(flag!=1):
    #    print("Yes")
    ####################################################################

    #################### SOLUTION3 ###################################
    #d={}
    #for word in magazine:
    #    d.setdefault(word,1)
    #    d[word]+=1

    #    what does setdefault do?
    #    it is similar to get(word,number)
    #    but get method throws an keyerror is the specified word is no found
    #    setdefault and defaultdict are similar

    #    in this case if word is not found it adds a entry word:1 into dictionary d
    #    else it returns the values of the key

       #for word in note:
       #    if d[word]==0:
       #        print("No")
       #        flag=1
       #        break
       #    d[word]-=1
       #if(flag!=1):
       #    print("Yes")
    
m=["give", "me", "one" , "grand","today" ,"night"]
n=["give", "one","grand" ,"today"]
checkMagazine(m,n)
