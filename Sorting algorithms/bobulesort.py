#Let's define the function
def bublesort(arr):
    #take the length
    n=len(arr)
    #create a loop for iteration
    for i in range(n):
        #create for another for loop starting the index 0 to n-i-1 mean lenght of the index - i for -1
        for j in range(0,n-i-1):
            # define the condition if index of arry of greate then next element then swap
            if arr[j]>arr[j+1]:
                #then the element must be swaped 
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr






#let's difine the array
arr=[20,40,5,1,9,10,100,235,459,66]
result=bublesort(arr)
print("After the sorting the arr the result will be",result)