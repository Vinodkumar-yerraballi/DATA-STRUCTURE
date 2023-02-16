#Lets' define function for the buble sort
def buble_sort(arr):
    swap=False
    while not swap:
        swap=True
        #create a loop iterationg to the each element
        for j in range(1,len(arr)):
            #checking the element if element is greater than it will be swapped
            if arr[j-1]>arr[j]:
                #take swap will be false
                swap=False
                #take the temp element is arr[j] and comapreing the next element if greate the will be swap it and palce to the temp element 
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp







arr=[1,3,5,2,0,99,34,83,930,3993,3030]
print('')
print(buble_sort(arr))
print(arr)