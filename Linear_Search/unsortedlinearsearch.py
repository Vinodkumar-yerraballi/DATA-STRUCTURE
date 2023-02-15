#The list must be unsorted 
def linear_search(L,e):
    found=False
    for i in range(len(L)):
        if e==L[i]:
            found=True
    return found



array=[5,6,1,2,7,9]
e=2
print(linear_search(array,e))