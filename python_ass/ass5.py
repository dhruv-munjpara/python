#5. Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3). If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged
string=input("enter the string:")

if len(string)<3:
    result=string
elif string.endswith("ing"):
    result=string+"ly"
else:
    result=string+"ing"
print("your string:",result)