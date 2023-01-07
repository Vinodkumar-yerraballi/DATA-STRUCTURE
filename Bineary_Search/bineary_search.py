#When the do the bineary_search alogrithm the arr must be sorted
# in the bineary_search problem divided into sub problems 
# Create function for the binearsearch
def binearysearch(arr,i,j,x):
    #in the function arr is the array, i is the starting index,j is the ending index,x is the value
    #checking the i value greater than j
    while i<=j:
        #Lets find the middle value 
        mid=i+(j-i)//2
        #after the finding the element if our searching number is midel number return mid
        if arr[i]==x:
            return mid
        #if number index less than the index move to the left
        elif arr[i]<x:
            #when we use the return function the time complecity and recurison we use another method
            # return binearysearch(arr,mid+1,j,x)
            i=mid+1
        
        # if number index greater than return the right
        else:
            # return binearysearch(arr,i,mid-j,x)
            j=mid-1
    #if the value not in the arry it's return the -1 value
        
    return -1

arr=[1,2,4,5,9,15,20,25,30]
i=0
j=len(arr)-1
x=15
print(binearysearch(arr,i,j,x))