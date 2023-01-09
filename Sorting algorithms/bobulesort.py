#Let's define the function
def bublesort(arr):
    #take the length
    n=len(arr)
    #create a loop for iteration
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr






#let's difine the array
arr=[20,40,5,1,9,10,100,235,459,66]
result=bublesort(arr)
print("After the sorting the arr the result will be",result)