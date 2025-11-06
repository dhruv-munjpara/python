num=12
num1=13
def printNum():
    global num
    num=1200
    num1=14
    print(num,num1)
num=300
print(num)
printNum()
print(num,num1)