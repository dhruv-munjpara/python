''' armstrong numbers menas 
if we have 153 =total degits=3
so 1**3,5**3,3**3=153
so its armstrong
'''
# num=int(input("enter a number"))
# print(num)
# degits=len(str(num))
# print(degits)
# sum=0
# temp=num
# while temp>0:
#     degit=temp%10
#     sum+=degit**degits
#     temp=temp//10

# if sum==num:
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number")

num=int(input("enter the number:"))
print(num)
n=len(str(num))
print(n)
sum=0
for i in str(num):
    sum+=int(i)**n
if sum==num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")    