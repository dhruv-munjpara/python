from view_fruit import fruits,save_fruits,log_transaction

def input_int(msg):
    """take only integer values(qty,price,menu choice)."""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("enter a valid number!!")
def market_manager():
    global fruits # use shared fruits dict
    
    while True:
        print("1)Add Fruit Stock \n2)Veiw Fruit Stock \n3)Update Fruit Stoke \n4)exit to main menu\n")
        Choice=input_int("enter a choice:")
       
        match Choice:
            #add new fruits or upadte one
            case 1:
                print("\nAdd Fruit Stock")
                name=input("enter Fruit name:")
                qty=int(input("enter a qty(in kg):"))
                price=int(input("enter price:"))
                # add or update fruit in dict
                if name in fruits:
                    fruits[name]['qty']+=qty
                    fruits[name]['price']=price
                    print(f"{name} updated successfully!")
                    log_transaction("UPDATE_STOCK",f"{name} updated")
                else:
                    fruits[name]={'qty':qty , 'price':price}
                    print(f"{name} added successfully!")
                    log_transaction("ADD_STOCK",f"{name} added")
                save_fruits(fruits)  # save
                print("Saved!")

            case 2:
                #viwe full stoke
                print("\nVeiw Fruit Stock")
                print(fruits)
                log_transaction("VIEW_STOCK","manager view stock")
            case 3:
                #update a fruit stock manually
                print("\nUpdate Fruit Stoke")
                name=input("Enter fruit name to update")

                if name in fruits:
                    new_qty=int(input("Enter a new quantity (in kg):"))
                    new_price=int(input("Enter a new price (for kg):"))
                    fruits[name]['qty']=new_qty
                    fruits[name]['price']=new_price
                    print(f"{name} updated successfully!")
                    save_fruits(fruits)
                    print("Updated")
                    log_transaction("MANAGER_UPDATE",f"{name} updated")
                else:
                    print(f"{name} not found in stock!")

            case 4:
                print("\n Returning to main menu...")
                log_transaction("EXIT_manager","manager exited to main menu")
                break
            case _:
                print("enter valid option")
        again=input("\n DO you want to perform more opration: press y for yes and n for no:").lower()
        if again !='y':
            break