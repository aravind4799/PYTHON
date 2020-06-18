#anticlockwise rotation of matrix 90 deg = transpose + reverse columns
#clockwise rotation of matrix 90 deg = transpose + reverse rows

def print_matrix(a):
    for i in range(len(a)):
        print()
        for j in range(len(a[0])):
            print(a[i][j],end=" ")

def transpose(a):
    for i in range(len(a)):#iterating rows
        for j in range(i,len(a[0])):#iterating columns
            t=a[i][j]
            a[i][j]=a[j][i]
            a[j][i]=t

def reverse_column(a):
  for i in range(len(a[0])):
      j=0
      k=len(a[0])-1
      while(j<k):
          t=a[k][i]
          a[k][i]=a[j][i]
          a[j][i]=t
          k=k-1
          j=j+1

def reverse_rows(a):
    for i in range(len(a)):
        j=0
        k=len(a)-1
        while(j<k):
            t=a[i][j]
            a[i][j]=a[i][k]
            a[i][k]=t
            j=j+1
            k=k-1

def anticlockise_90deg_rotation(A):
    transpose(A)
    reverse_column(A)

def clockwise_90deg_rotation(A):
    transpose(A)
    reverse_rows(A)

arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ];
#anticlock_90deg_rotation(arr)
#print_matrix(arr)
clockwise_90deg_rotation(arr)
print_matrix(arr)
