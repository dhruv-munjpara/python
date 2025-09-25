import random
number=random.randint(1,100)
while True:
    guess_number=int(input("enter guess number:"))
    if number>guess_number:
        print("pls enter high number:")
    elif number<guess_number:
        print("pls enter a lower number:")
    else:
        print("congrates you have a guessed correct number")
        break