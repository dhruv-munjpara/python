data=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

freq={}

for i in  data:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key in sorted(freq):
    print(f"{key} : {freq[key]}", end=" , ")
