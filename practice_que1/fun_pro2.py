#  - Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
def check_text(text):
    if len(text)>5:
        print(text.upper())
    else:
        print(text.lower())
s=input("enter a text:")
check_text(s)