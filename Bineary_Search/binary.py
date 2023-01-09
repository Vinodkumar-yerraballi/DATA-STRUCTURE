matrix=[[1,2,3],
[4,5,6],[60,70,90]]
i=0
j=len(matrix)-1
x=60
def binerysearch(matrix,i,j,x):
    mid=i+(j-1)//2
    while True:
        if matrix[i]==x:
            return mid
print(binerysearch(matrix,i,j,x))