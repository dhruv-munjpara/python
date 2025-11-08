#- Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
def altrnate_case(s):
    result=""
    for i in range(len(s)):
        if i%2==0:
            result+=s[i].upper()
        else:
            result+=s[i].lower()
    return result
text=input("enter a text")
print(altrnate_case(text))