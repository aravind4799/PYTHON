#program to return nth fibonacci number
def getNthFib(n):
    lst=[0,1]
    i=0
    j=1
    for x in range(n):
        lst.append(lst[i]+lst[j])
        i=j
        j=j+1
    return lst[n-1]
ans=getNthFib(8)
print(ans)
