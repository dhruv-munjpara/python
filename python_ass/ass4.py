#4. Write a Python program to get a single string from two given strings, separatedbya space and swap the first two characters of each string.

str1=input("enter the str1:")
str2=input("enter the str2:")

newstr3=str1 +" "+str2
print(newstr3)

str4=str1[:2] + str2[2:]
str5=str2[:2] + str1[2:]
print(f"{str4}  {str5}")