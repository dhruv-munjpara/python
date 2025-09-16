num=int(input("enter a num"))
# for i in range(num+1,0,-1):
#     for j in range(i):
#         print("* ",end=" ")
#     print()



i=num+1
while i>0:
    j=0
    while j<i:
        print("* ", end="")
        j+=1
    print()
    i-=1