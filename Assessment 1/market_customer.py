from view_fruit import fruits
def market_customer():
    global fruits # use shared fruits dict
    
    while True:
        print("1)View Fruit Stock \n2)Buy fruits \n3)Exit \n")
        Choice=int(input("enter a choice:"))
       
        match Choice:
            #view fruits for customer
            case 1:
                print("\nview fruit stock")
                print("\n AVailable fruits")
                for name,info in fruits.items():
                    print(f"{name}:{info['qty']} kg available @ ₹{info['price']}per kg")


            case 2:
                #buy fruits
                print("\nbuy fruits")
                name=input("Enter the fruit name to buy:")
                
                if name in fruits:
                    qty=int(input("Enter quantity (in kg):"))
                    if qty<=fruits[name]['qty']:
                        total=qty*fruits[name]['price']
                        fruits[name]['qty']-=qty
                        print(f"you bought {qty} kg of {name} for ₹{total}.") 
                    else:
                        print(f"Sorry, only {fruits[name]['qty']} kg of {name} is Available.")
                else:
                    print(f"{name} is not available in stock.")       
            case 3:
                #exit
                print("\nThank you for visiting! see you again")
                break


            case _:
                print("enter valid option")