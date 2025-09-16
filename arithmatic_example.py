# arithmatic operator
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

print("addition is:",num1+num2)
print("substracation is:",num1-num2)
print("mul is:",num1*num2)
print("division is:",num1/num2)
print("floor division is:",num1//num2)
print("mod is:",num1%num2)
print("exponent:",num1**num2)

# arithmatic operator with formate

print("hello"*3)
print("addition is {} and {} is {}".format(num1,num2,num1+num2))
print(f"addition of {num1} and {num2} is {num1+num2}")
print(f"sub of {num1} and {num2} is {num1-num2}")
print(f"mul of {num1} and {num2} is {num1*num2}")
print(f"div of {num1} and {num2} is {num1/num2}")
print(f"floor div of {num1} and {num2} is {num1//num2}")
print(f"mod of {num1} and {num2} is {num1%num2}")
print(f"exponent of {num1} and {num2} is {num1**num2}")