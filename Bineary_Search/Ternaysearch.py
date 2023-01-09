#define the function 
#calling the function name in the function leds to the recursion that's way i choose another method to used it 
def Ternaysearch(l,r,x,arr):
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if x==arr[mid1]:
           return mid1
        elif x==arr[mid2]:
           return mid2
        elif x<arr[mid1]:
           r=mid1-1
        elif x> arr[mid2]:
            l=mid2+1
        else:
            r,l=mid1+1,mid2-1
    return -1
    



#difine the sorted_array
arr=[1,2,3,4,5,6,7,8,9]
# Define the target value
x=3
#hear l is the starting index
l=0
#r is the ending index
r=len(arr)-1
result=Ternaysearch(l,r,x,arr)
print(result)