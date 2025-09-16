age=int(input("enter the age:"))
weight=int(input("enter weight:"))
if age>18:
    if weight>50:
        print("you can donate your blood")
    else:
        print("you can't donate")
else:
     print("you can't donate")


if age>18 and weight>50:
    print("you can donate")
else:
     print("you can't donate")