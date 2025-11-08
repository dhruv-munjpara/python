# - Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
def found(s,s1):
    if s1 in s:
        return True
    else:
        False

string=input("enter a string:")
sub_string=input("enter a sub string:")
print(found(string,sub_string))