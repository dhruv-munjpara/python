def check_Even(num):
    if num%2==0:
        print("even number")
    else:
        print("odd number")

def check_p_n(num):
    if num>0:
        print("number is positive")
    else:
        print("number is nagative")

def check_prime(num):
    temp=1
    for i in range(2,num):
        if num%i==0:
            temp=1
            break 
        else:
            temp=0

    if temp==1:
        print(f"{num} is not prime")
    else:
        print(f"{num} is  prime")