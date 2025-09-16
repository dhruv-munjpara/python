#7. Program to find Greatest Common Divisor of two numbers. For example, theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14

a=int(input("enter a:"))
b=int(input("enter b:"))

while b!=0:
    a,b=b, a%b

print("GCD is",a)