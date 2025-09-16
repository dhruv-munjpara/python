# num=int(input("enter number:"))
# prev=0
# next=1
# sum=0



#this is start with 1
# for i in range(num):
#     prev=next
#     next=sum
#     sum=prev+next
#     print(sum)




#this is start with 0
# for i in range(num):
#     if i==0:
#         sum=0
#     else:
#         prev=next
#         next=sum
#         sum=prev+next
#     print(sum)

num = int(input("Enter num: "))

a, b = 0, 1
sum = 0

while sum < num:
    print(a, end=" ")
    a, b = b, a + b
    sum += 1