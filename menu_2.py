while True:

    print(" \n1. Convert into Uppercase  \n2. Convert into Lowercase  \n3. Find length  \n4. Replace  \n5. Exit ")
    choice = int(input("Please enter your choice : "))
    match choice:
        case 1:
            string=input("pls enter a string:")
            print(f"convert string to upper:{string.upper()}")
        case 2:
            string=input("pls enter a string:")
            print(f"convert string to lower:{string.lower()}")
        case 3:
            string=input("pls enter a string:")
            print(f"convert string to find length:{len(string)}")
        case 4:
            string=input("pls enter a string:")
            old_str=input("enter a old word of string:")
            new_str=input("enter a new word you want set in string:")
            print(f"after replace{string.replace(old_str,new_str)}")

        case 5:
            break
        case _:
            print("enter a valid choice:")
