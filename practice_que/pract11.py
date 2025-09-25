text=input("enter something:")
letters=0
degits=0

for ch in text:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        degits+=1
print("letters:",letters)
print("degit:",degits)
