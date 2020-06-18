#printing all primes in given range
lb=int(input("enter lowerbound"))
ub=int(input("enter upperbound"))
for x in range(lb,ub+1):
    flag=0
    for y in range(2,x):
        if(x%y==0):
            flag=1
            break;
    if(flag==0):
        print(x)
