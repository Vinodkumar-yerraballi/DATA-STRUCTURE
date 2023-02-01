def merge_list(test_input_list1, test_input_list2):
    #fristy add the two list and get the finall output
    finall=test_input_list1+test_input_list2
    #using the buble sorting method
    #using the loop condition iterating to the entire elements
    for i in range(len(finall)):
        # The second loop it iterating to start to ending index
        for j in range(0,len(finall)-1):
            # we using condition if the first element is greate then second element then we swap it and the codition check for entire the list and return the list
            if finall[j]>finall[j+1]:
                finall[j],finall[j+1]=finall[j+1],finall[j]
            return finall

list1 = [1,2,5]
list2 = [2,4,6]
print(merge_list(list1,list2))

#Output will be
# [1,2,2,4,5,6]