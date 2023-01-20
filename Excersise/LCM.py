#To calculate the LCM of two numbers
def find_lcm(a,b):
    if a >b:
        greater=a
    else:
        greater =b

    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater +=1
    return lcm


num1=int(input("Enter a number"))
num2= int(input("Enter another number"))
print("The solution of the given numbers is ", find_lcm(num1,num2))