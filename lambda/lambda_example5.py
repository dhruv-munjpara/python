# # lst=[1,2,3,4,5,6,7,8,9,10]
# # lst1=[]

# # def square(num):
# #    if num%2==0:
# #       return "Even"
# #    else:
# #       return "Odd"
# # lst1=list(map(square,lst))
# # print(lst1)



# dict1={1:"",2:"",3:"",4:""}
# dict2={k:"even" if k%2==0 else "odd" for k,v in dict1.items()}
# print(dict2)


# print number is even or odd from list with lambda function
lst_numbers=[1,2,3,4,5,6,7,8,9]
ans=list(map(lambda i:"even" if i%2==0 else "odd",lst_numbers))
print(ans)

dict1={1:"",2:"",3:"",4:""}
ans1=lambda k:"even" if k%2==0 else "odd"
ans2={k:ans1(k) for k in dict1.keys()}
print(ans2)