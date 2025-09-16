num=int(input("enter a num"))
# for i in range(num+1):
#     for j in range(i):
#         print("* ",end=" ")
#     print()

i=1
while i<=num:
    j=1
    while j<=i:
        print("* ",end=" ")
        j+=1
    print()
    i+=1