#BinarySearch algorithm 
def bineary_search(L,e):
    def bineary_search_helper(L,e,low,high):
        #if the element is low and high equal to return false
        if high==low:
            return False
        #take the midle element low element and high element dividedby 2
        mid=(low+high)//2
        #if enter number equal to middle number return True
        if L[mid]==e:
            return True
        # 
        elif L[mid]>e:
            if low==mid:
                return False
            else:
                return bineary_search_helper(L,e,low,mid-1)
        else:
            return bineary_search_helper(L,e,mid+1,high)
    if len(L)==0:
        return False
    else:
        return bineary_search_helper(L,e,0,len(L)-1)


array=[2,3,4,5,6,7,8]
e=5
print(bineary_search(array,e))