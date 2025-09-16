c_even=0
c_odd=0
for i in range(0,10):
    if i%2==0:
       c_even+=1
    else:
        c_odd+=1

print(f"number of even number{c_even}")
print(f"number of odd number{c_odd}")
