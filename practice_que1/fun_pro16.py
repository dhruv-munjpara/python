# - Write a function that accepts two strings and returns the common characters between them
def common(str1,str2):
    common=""
    for ch in str1:
        if ch in str2 and ch not in common:
            common+=ch
    return common

str1="apple"
str2="grape"
print(common(str1,str2))