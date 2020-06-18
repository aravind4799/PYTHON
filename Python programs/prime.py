a=int(input("enter a number?"))
flag=0
for x in range(2,a):
    if(a%x==0):
        flag=1
        break;
if(flag==0):
    print("Prime")
else:
    print("Not Prime")
