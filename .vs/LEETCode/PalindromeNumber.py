def isPalindrome(x):
    x=str(x)
    n=x[::-1]
    if x==n:
        return True
    else:
        return False









x=121
print(isPalindrome(x))



# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.