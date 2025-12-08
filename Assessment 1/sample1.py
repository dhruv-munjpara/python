from market_manager import market_manager
from market_customer import market_customer
from view_fruit import log_transaction

def input_int(msg):
    """accpet only valid integer input"""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("invalid input!! enter a numbers only.")

while True:
    print("WELCOME TO FRUIT MARKET\n")
    print("1)Manager \n2)Customer \n3)exit \n")
    Choice=input_int("enter a choice:")
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
            print("Thank you for visiting! Goodbye.")
            log_transaction("EXIT_program","program exited by user from main menu")
            break
        
        case _:
            print("enter valid option")

