# create function to check string is palidrome or not 
def check_palindrome(text):
    if text==text[::-1]:
        return "palindrome"
    else:
        return "Not palindrome"

s=input("enter a string:")
print(check_palindrome(s))