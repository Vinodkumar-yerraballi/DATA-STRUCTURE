lst=[1,2,3,3,4,5,5]
flag=True
frlag_adj=False
count=0
for i in range(len(lst)-1):
    if lst[i] !=lst[i+1]:
        flag=False
    else:
        count +=1

if flag==True:
    count_color=1
else:
    if(len(lst)-count)%2:
        count_color=3
    else:
        count_color=2
print(count_color)