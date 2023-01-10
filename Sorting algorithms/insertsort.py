#define the function
def insertsort(arr):
    #create loop for the second index to len of array
    for  i in range(1,len(arr)):
        #we take the variable of the second element
        key=arr[i]
        # define the anothe j value that will be subtract the i value with -1
        j=i-1
        #define the while loop for the condition
        while j>=0 and key<arr[j]:
            #then the element will the index of the j+1 will be j
            arr[j+1]=arr[j]
            #then j value the subtrac the j-1
            j=j-1
            #then element with j+1 index is replaced with key value
            arr[j+1]=key
    return arr
    

#let's given the array
arr=[50,2,75,67,82,1,0,66,99,129,590]
#define the variable names
result=insertsort(arr)
print('After sorting the array we get the result',result)