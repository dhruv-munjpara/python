#6. Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
string=input("enter string:")
not_p=-1
poor_p=-1

for i in range(len(string) -2):
    if string[i]=="n" and string[i+1]=="o" and string[i+2]=="t":
        not_p=i
        break

for i in range(len(string) -3):
    if string[i]=="p" and string[i+1]=="o" and string[i+2]=="o" and string[i+3]=="r":
        poor_p=i
        break

if not_p !=-1 and poor_p !=-1 and not_p<poor_p:
    result=string[:not_p] + "good" + string[poor_p+4:]

else:
    result=string

print(result)

