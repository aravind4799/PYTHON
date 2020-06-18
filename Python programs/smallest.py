#locking key problem
#Smallest possible number that can be formed using given number
a = int(input("enter a number:"))
arr=[]
i=0
num=0
while(a!=0):
    n=a%10
    arr.append(n)
    a=int(a/10)
arr.sort()
#print(arr)
len=len(arr)
x=len
#print(len)
if(arr[0]!=0):
    while(len!=0):
         y=len
         num+=arr[i]*pow(10,y-1)
         i=i+1
         len=len-1
else:
    j=0
    while(x!=0):
       if(arr[j]!=0):
            t=arr[j]
            break
       j=j+1
       x=x-1
    #print(t)
    #this code swaps two elements in an array
    ###################################
    f=arr[j]
    arr.pop(0)
    arr.pop(j)
    arr.insert(0,f)
    arr.insert(j,0)
    ####################################
    #print(arr)
    while(len!=0):
          y=len
          num+=arr[i]*pow(10,y-1)
          i=i+1
          len=len-1
print("{0} is smallest possible number using the given numbers".format(num))
