age=int(input("enter the num:"))
if age>=0 and age<=12:
    print("child")  
elif age>12 and age<=18:
    print("teenager")
elif age>18 and age<=60:
    print("adult")
else:
    print("senior citizen") 
    