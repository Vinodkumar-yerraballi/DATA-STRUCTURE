#List Comprisoon.py
# Sample Input 0
# 1
# 1
# 1
# 2
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Each variable  and  will have values of  or . All permutations of lists in the form
#create empty list

x=int(input("Enter number"))
y=int(input("Enter number"))
z=int(input("Enter number"))
n=int(input("Enter number"))
a=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k==n:
                continue
            a.append([i,j,k])
print(a)



