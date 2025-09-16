num=int(input("enter no:"))
temp=0
i=2
while i<num:
    if num%i==0:
        temp=1
        break
    i+=1
   
   
if temp==1:
    print(f"{num} is not prime number")
else:
    print(f"{num} is  prime number") 