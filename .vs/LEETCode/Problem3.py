def find_len_string(s):
    result=""
    for i in range(len(min(s))):
        if all(x[i]==s[0][i] for x in s):
            result= result +s[0][i]
            
        else:
            break
    return result

    








list1=['fruit','friend','frist']
a=['dog','apple','car']
print(find_len_string(list1))
print("Second list",find_len_string(a))