'''
we have one number so its number is start and end all side same 
menas 121=121
and 123=321 so its not palindrome
'''
# num=int(input("enter the number:"))
# print(num)
# temp=num
# rev=0
# while temp>0:
#     degit=temp%10
#     rev=rev*10+degit
#     temp=temp//10

# if num==rev:
#     print("its a palindrome")
# else:
#     print("its not palindrome")


num=int(input("enter a number:"))
print(f'your number is {num}')
degit=str(num)
rev=""

for i in degit:
    rev=i+rev
print("Reversed number:", rev)

if num==int(rev):
    print("its a palindrome")
else:
    print("its not palindrome")