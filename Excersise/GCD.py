m=int(input("Enter a number"))
n=int(input("Enter a number"))

if m>n:
    small_number=m
else:
    small_number=n
for i in range(1,small_number+1):
    if m%i==0 and n%i==0:
        gcd=i
print(gcd)
