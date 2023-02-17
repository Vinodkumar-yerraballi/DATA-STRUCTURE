# DATA-STRUCTURE

### Linear_search
   1) Linear search is very simple to understand to find the element in the given array
   2) a for loop iterating the eache element in the given array. ie for i in range(len(arr))
   3) codition is very simple that is 
     if arr[i]==x:
     return i
    3) Above the code return to the given index of the elementn
### Bineary_search
   1)In This algorithm to find the specific value in the given array and The array must and shoud be sorted.
   2) we take l=0 and j=len(array)-1 we get the how many elements in the array if the array greater than find the middele element
   3) Middle element is mid=i+(j-1)//2
   4) if the searching element is midele element then it return to the midle index
   5) if searching elemnt not midle element if it's less than the midle element add the mid+1
   6) if searching elemnt not midle element if it's grater than the midle element add the mid-1

## Soritng algorithms
### Bubblesort algorithm
  1) This algorithms is do given array is sorted. This is the main aim to the all sorting algorithms
  2) create two for loop in the function one is iterating to the len of elements. Second loop iterating the stating index to lenght array -1 it menan n=len(arr) . The loop contains this
  " for j in range(0,len(arr)-i-1)"
  3) We write the if condition, What happend in the condition the first element check with other elements if first element is greater than first element then it swap.The code is written below
  " if arr[j]< arr[j+1]:
       arr[j],arr[j+1]=arr[j+1],arr[j] "

### Selection sort
    1) This algoritms is to sort the array in orderwise They are two methods to searh this algorihmns
    1) the the varible equal to 0 and checking the while condition if variable not eaual to length of arrya then move to the for loop in the range of variable and length.
    2) Checking the condition if index of array greager then index of the varibel then it will be swapped.What happend realy the first element is checking the each element in given arry if it's greater than first element it will be swap or other wise it's place as first element the process repet until the array sorted.
    This is the entire process is done in the selection sort algorithms

### Merge sort
    1) The given problem divided into subclass which means. we given an array and it's unsorted array to given the sorted array, The algorithms says the array divided to two arrays .
      "For example if the array have 8 element 8 element divdes two part one araay contains 4 and another one contains 4 elements. The 4 elements divided into 2 pairs. The each pair element checking weathe it' greater then the element in the pair it will replace or same the pair is checking with next pair of the elements. Weather it's greater then it will replace it other wise not replace it. Finaly we check the four pair and merge it as two pair and two pairs will be merge one pair.

### insertion sort algorithms
    In this algorithms we take the first index of the element of and checking it next element if the elelemnt is greater than if swap it and then thrid element add and compare to the each element it greater than it.it replace it the process is still done the array is sorted. the process is done untill the array is sorted.