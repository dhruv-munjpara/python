start=int(input("enter a starting pointe:"))
end=int(input("enter a ending pointe:"))

for i in range(start,end+1):
    if i%2==0:
        print("even num",i)
    else:
        print("odd num",i)