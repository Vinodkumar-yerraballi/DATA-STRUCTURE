#create a function to merge sort 
def merge_srot(left,right):
    #create an empty list
    result=[]
    #i and j variable 0 and o
    i,j=0,0
    #checking the i less then the left and lessthan right 
    while i<len(left) and j<len(right):
        #checking the left element is less than the right element then append the left element 
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
        #if above condition not satisfied then move append right elemnt
            result.append(right[j])
            j+=1
    #checking the i less than the length of left element then append the left index
    while (i<len(left)):
        result.append(left[i])
        i+=1
    #Checking the right element th lessthan we append the right element and finally print the result
    while (j<len(right)):
        result.append(right[j])
        j+=1
    print('merge'+str(left)+str(right))
    return result
#create another function for mergesort
def mergesort(arr):
    #checking the length of lessthan 2 elements return to 
    if len(arr)<2:
        return arr[:]
    #Than checking len arr is divideed by 2
    else:
        mid=len(arr)//2
        #add the left element and right element to return the fianall resutl
        left=mergesort(arr[:mid])
        right=mergesort(arr[mid:])
        return merge_srot(left,right)
test=[5,3,2,1,0,9,8,5,7,6]
print('')
print(mergesort(test))