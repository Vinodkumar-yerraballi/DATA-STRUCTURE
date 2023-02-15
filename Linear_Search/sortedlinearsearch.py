def linear_search(array,e):
    #create a loop for iterating the each element
    for i in range(len(array)):
        #Just given the condition is equal to searching element then return to True
        if array[i]==e:
            return True
        elif array[i] >e:
            return False
    #if element not in the list return to false
    return False

array=[2,3,5,6,9]
e=0
print(linear_search(array,e))