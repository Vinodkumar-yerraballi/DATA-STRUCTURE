def reverse(s):
    return s[::-1]

hello='Hello world'
print(reverse(hello))
def swap_case(s):
    for i in range(len(s)):

        if (s.swapcase()):
            return s.swapcase()


    return
print(swap_case(hello))

def merge_list(test_input_list1, test_input_list2):
    # final=[]
    # for i in range(len(test_input_list1)):
    #     for j in range(len(test_input_list2)):
    #         mid=i+j//2
    #         if mid[i]<mid[j]:
    result=test_input_list1.append(test_input_list2)
    print(result)

list1 = [1,2,5]
list2 = [2,4,6]
result=list1+list2
for i in range(len(result)):
    for j in range(0,len(result)-1):
        if result[j]>result[j+1]:
            result[j],result[j+1]=result[j+1],result[j]
        print(result)

# print(result)
# print(merge_list(list1,list2))