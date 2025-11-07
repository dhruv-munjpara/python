# lst=[1,2,3,4,5,6,7,8,9,10]
# lst1=[]

# def square(num):
#    if num%2==0:
#       return "Even"
#    else:
#       return "Odd"
# lst1=list(map(square,lst))
# print(lst1)



dict1={1:"",2:"",3:"",4:""}
dict2={k:"even" if k%2==0 else "odd" for k,v in dict1.items()}
print(dict2)