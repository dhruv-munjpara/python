# - Write a function that accepts a string and counts how many vowels are in the string.
def cnt_vowels(text):
    vowels="aeiou"
    cnt=0
    for i in text:
        if i in vowels:
            cnt+=1
    return cnt

string=input("enter a string:")
print("number of vowels:",cnt_vowels(string.lower()))
