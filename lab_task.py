start=int(input("start point"))
end=int(input("end point"))
sum=0
for i in range(start,end):
    if i%2==0:
        sum+=i
print(f"sum of even numbers{sum}")
sum=0
for i in range(start,end):
     if i%2!=0:
        sum+=i
print(f"sum of odd numbers{sum}")