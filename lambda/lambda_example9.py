# def length_gre(city):
#     if len(city)>7:
#         return city
# city=["ahemdabad","baroda","limbdi","rajkot"]
# len_ans=list(filter(length_gre,city))
# print(len_ans)

# print city wich is greter then 7 with lambda
city=["ahemdabad","baroda","limbdi","rajkot"]
len_ans1=list(filter(lambda i:len(i)>7,city))
print(len_ans1)