#Selection sort
def selection_sort(arr):
    #Create a loop iterating the each element in the given array
    for i in range(len(arr)):
        #take the midel index as i
        mid_in=i
        #Create a another loop to iterating the next intdex of the i and len of array
        for j in range(i+1,len(arr)):
            #Write the codition if arr[j] is greater then middle of the index then it cosider the midle index as j
            if arr[j] < arr[mid_in]:
                mid_in=j
                #Swap the elements
                arr[i],arr[mid_in]=arr[mid_in],arr[i]
    return arr











arr=[4,5,1,9,11,2,999,33,3848,4848]
print(selection_sort(arr))