a=[1,2,3,4,5]

def rotate_left(a,n):
    mod=n%len(a)
    for i in range(len(a)):
        print((a[(mod+i)%len(a)]),end=" ")

def rotate_right(a,n):
    mod=n%len(a)+1
    for i in range(len(a)):
        print((a[(mod+i)%len(a)]),end=" ")

rotate_right(a,2)
#rotate_left(a,2)
#o(n) logic
    #for x in range(d):
    #    i=0
    #    t=a[0]
    #    for i in range(len(a)-1):
    #        a[i]=a[i+1]
    #    a[len(a)-1]=t

    #return a
