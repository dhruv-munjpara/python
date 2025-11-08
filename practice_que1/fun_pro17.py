# - Write a function count_character(string, char) that accepts a string and a character, and returns the number of times the character appears in the string.
def count_char(str,char):
    cnt=0
    for ch in str:
        if ch==char:
            cnt+=1
    return cnt

text="programing"
char="m"
print(count_char(text,char))