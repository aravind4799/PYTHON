def anticlockwise_rotation(a):
        top=0
        bottom=len(a)-1
        left=0
        right=len(a[0])-1

        while left<right and top<bottom:
                prev=a[top+1][right]
                for i in range(right,left-1,-1):
                    curr=a[top][i]
                    a[top][i]=prev
                    prev=curr
                top=top+1

                for i in range(top,bottom+1):
                    curr=a[i][left]
                    a[i][left]=prev
                    prev=curr
                left=left+1

                for i in range(left,right+1):
                    curr=a[bottom][i]
                    a[bottom][i]=prev
                    prev=curr
                bottom=bottom-1

                for i in range(bottom,top-1,-1):
                    curr=a[i][right]
                    a[i][right]=prev
                    prev=curr
                right=right-1
        return a

def clockwise_rotation(a):
    top=0
    bottom=len(a)-1
    left=0
    right=len(a[0])-1

    while left<right and top<bottom:

        prev=a[top+1][left]
        for i in range(left,right+1):
            curr=a[top][i]
            a[top][i]=prev
            prev=curr
        top=top+1

        for i in range(top,bottom+1):
            curr=a[i][right]
            a[i][right]=prev
            prev=curr
        right=right-1

        for i in range(right,left-1,-1):
            curr=a[bottom][i]
            a[bottom][i]=prev
            prev=curr
        bottom=bottom-1

        for i in range(bottom,top-1,-1):
            curr=a[i][left]
            a[i][left]=prev
            prev=curr
        left=left+1
    return a

def print_matrix(a):
    for i in range(len(a)):
        print()
        for j in range(len(a[0])):
            print(a[i][j],end=" ")

matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]
        ]
#matrix=clockwise_rotation(matrix)
matrix=anticlockwise_rotation(matrix)
print_matrix(matrix)
