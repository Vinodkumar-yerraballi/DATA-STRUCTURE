def addtwo_number(a,b):
    result=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if len(a)==len(b):
                return result.append(a[i]+b[j])
            else:
                return False






l1 = [2,4,3]
l2 = [5,6,4]
#output 
# [7,0,8]
result=[]
final=result.append(l1*l2)
print(final)
print(addtwo_number(l1,l2))