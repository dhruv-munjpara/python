from market_manager import market_manager
from market_customer import market_customer
while True:
    print("WELCOME TO FRUIT MARKET\n")
    print("1)Manager \n2)Customer \n")
    Choice=int(input("enter a choice:"))
    match Choice:
        case 1:
            print("\nFruit Market Manager")
            result=(market_manager())
            if result:
                print(result)

        case 2:
            print("Fruit Maerket Customer")
            result1=(market_customer())
            if result1:
                print(result1)
        
        case 3:
            print("Thank you for visiting!")
            break
        
        case _:
            print("enter valid option")