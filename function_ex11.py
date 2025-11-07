# lst=[1,2,3]
# def square():
#     lst1=[]
#     for i in lst:
#         lst1.append(i**2)
#     print(lst1)

# square()

lst=[1,2,3]
lst1=[]

def square(num):
   return num*num

lst1=list(map(square,lst))
print(lst1)