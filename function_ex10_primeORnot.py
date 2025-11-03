# Lab task : create function which accept a number and return "Prime" or "Not Prime"
def prime(num):
    for i in range(2,num):
        if num%i==0:
            return "not prime"
    return "prime"

n=int(input("enter a number:"))
print(prime(n))