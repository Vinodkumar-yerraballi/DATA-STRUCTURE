def selection_sort(arr):
    suffix=0
    while suffix!=len(arr):
        for i in range(suffix,len(arr)):
            if arr[i]<arr[suffix]:
                arr[suffix],arr[i]=arr[i],arr[suffix]
                # suffix +=1



print('')
test=[2,5,6,92,3,50,56]
print(selection_sort(test))
print(test)