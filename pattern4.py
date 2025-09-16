num=int(input("enter a num:"))
cnt=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(cnt,end=" ")
    print()
    cnt+=2