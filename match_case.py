print("1.add \n 2.sub \n 3.mul \n 4.div")
choice=int(input("enter the choice"))
match choice:
    case 1:
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(f"add is {num1+num2}")
    case 2:
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(f"sub is {num1-num2}")
    case 3:
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(f"mul is {num1*num2}")
    case 4:
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(f"div is {num1/num2}")
    case _:
        print("enter valid option")