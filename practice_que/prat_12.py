text=input("enter a number:")
count=0
for ch in text:
    if ch.isdigit():
        count+=1
print("number of degits",count)