
dimension = int(input("enter dimension of matrix"))

# rows,col = (5,5)

arr=[[0 for i in range(dimension)] for j in range(dimension)]
a=[[0 for i in range(dimension)] for j in range(dimension)]
b=[[0 for i in range(dimension)] for j in range(dimension)]
number = int(input("enter matrix generator"))

for i in range(dimension):
    for j in range(dimension):
        arr[i][j]=number
        number=number+1

for i in range(dimension):
    print()
    for j in range(dimension):
        print(arr[i][j],end=" ")

for i in range(dimension):
    for j in range(dimension):
        a[i][j]=arr[j][i]


print()
for i in range(dimension):
    print()
    for j in range(dimension):
        print(a[i][j],end=" ")

for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):
            b[i][j]+=arr[i][k]*a[k][j]

print()
for i in range(dimension):
    print()
    for j in range(dimension):
        print(b[i][j],end=" ")
