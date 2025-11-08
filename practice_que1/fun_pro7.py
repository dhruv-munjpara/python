# # - Write a function that accepts a number and checks if it is an Armstrong number.
# num=int(input("enter the number:"))
# print(num)
# n=len(str(num))
# print(n)
# sum=0
# for i in str(num):
#     sum+=int(i)**n
# if sum==num:
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number")

def armstrong_or_not(num):
    n=len(str(num))
    sum=0
    for i in str(num):
        sum+=int(i)**n
    if sum==num:
        print("its armstong")
    else:
        print("its not armstrong")\

num=int(input("enter a num:"))
armstrong_or_not(num)