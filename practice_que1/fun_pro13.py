# - Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.
def email_check(email):
    if email.endswith("@gmail.com"):
        return True
    else:
        return False
    
email=input("emter a email:")
print(email_check(email))