#define the function 
def selectionsort(arr):
    #let's define varible with length
    n=len(arr)
    #create a loop for iteration to the entire array
    for i in range(n):
        #we take the middle index varible with starting index
        #it's mean the array starting index we take as mid_index
        mid_index=i
        #create another loop for the range the second index to length of array
        for j in range(i+1,n):
            #let's define a condition to the 
            #if the mid_index is less than the next elemetn then the middle index will be change
            if arr[j]<arr[mid_index]:
                #then the middle index is reaplced by i to j
                mid_index=j
                #if the condition is satasfied then the element will be swapped
            arr[i],arr[mid_index]=arr[mid_index],arr[i]
    #then finally return the array
    return arr


#let's given the array
arr=[50,2,75,67,82,1,0,66,99,129,590]
#define the variable names
result=selectionsort(arr)
print('After sorting the array we get the result',result)