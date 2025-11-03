#fun with return
def CheckNumber(num):
    if num%2==0:
        return "Even"
    else:
        return "ODD"
    
# ans=CheckNumber(23)
# print(ans)
# ans=CheckNumber(922222)
# print(ans)
for i in range(100):
    print(f"{i}-{CheckNumber(i)}")