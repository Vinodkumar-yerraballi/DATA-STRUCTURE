def Linearsearch(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1
arr=[33,45,66,99,123,54,9]
x=99
print(Linearsearch(arr,x))