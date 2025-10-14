# Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
str=input("enter a string:")
final=""
for i in range(0,len(str)):
    if i%2==0:
        final+=str[i].upper()
    else:
        final+=str[i].lower()

print(final)
