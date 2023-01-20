#reverse the string
def reverse(s):
    str= " "
    for i in s:
        str=i+str
    return str
s='Hello world'
print("Before reverse the string",s)
print("After reveser the output",reverse(s))