#*args vriable 
def addition(*args):
    sum=0
    for i in args:
        if type(i)==int:
            sum+=i
    print(sum)
addition(12,"hhhh",23)
addition(23,234,567)