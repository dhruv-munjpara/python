# armstrong number or not
# num=int(input("emter a nuber:"))
# sum=0
# temp=num
# n=len(str(num))
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10

# if num==sum:
#     print(f"{num} is an armstronge") 
# else:
#     print(f"{num} is note armstrong")



num=int(input("emter a nuber:"))
sum=0
n=len(str(num))
for i in str(num):
    sum+=int(i)**n
if sum==num:
    print(f"{num} is an armstronge") 
else:
    print(f"{num} is note armstrong")

