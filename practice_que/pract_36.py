words=["Mango","Banana","Melon","Apple"]
cnt=0
for i in words:
    if i.startswith("M"):
        cnt+=1
print(f"number of words starting with 'M':{cnt}")