#Lets create the function
def Ternaysearch(l,r,x,arr):
    #create a while loops
    while l<=r:
        #what we done we divided the array into 3 parts
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        #difine the condition if the target is equal the mid1 it return to the mid1
        if x==arr[mid1]:
            return mid1
        # Checking the another condition if the targets is equel to the mid2 it return to the mid2
        elif x==arr[mid2]:
            return mid2
        #If the targe less then the mid1 then it return the the index of the element in mid1-1 it means subtrcat the mid1 index
        elif x< arr[mid1]:
            return Ternaysearch(l,mid1-1,x,arr)
        # if the target greater then  it return the adding the element to the mid2 condition
        elif x> arr[mid2]:
            return Ternaysearch(mid2+1,r,x,arr)
        # if the elements between then mid1 and mid2 it return the add index mid1 and substact the index mid2
        else:
            return Ternaysearch(mid1+1,mid2-1,x,arr)
    # if the element not in the array it return to the -1
    return -1
#difine the sorted_array
arr=[1,2,3,4,5,6,7,8,9]
# Define the target value
x=9
#hear l is the starting index
l=0
#r is the ending index
r=len(arr)-1
result=Ternaysearch(l,r,x,arr)
print(result)