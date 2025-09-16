# num=int(input("enter a number:"))
# print(f'your number is {num}')
# degit=str(num)
# rev=""

# for i in degit:
#     rev=i+rev
# print("Reversed number:", rev)

num=int(input("enter the number:"))
print(num)
temp=num
rev=0
while temp>0:
    degit=temp%10
    rev=rev*10+degit
    temp=temp//10
print("Reversed number:", rev)

