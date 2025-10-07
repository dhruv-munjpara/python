#write a program to find GCD of 2 numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b!=0:
#     a,b=b,a%b

# print("GCD is:",a)

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD is:", math.gcd(a, b))