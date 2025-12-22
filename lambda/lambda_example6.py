# # length of city
# city=["ahemdabad","baroda","limbdi","rajkot"]
# length=list(map(len,city))
# print(length)

# # upper
# city=["ahemdabad","baroda","limbdi","rajkot"]
# upper=list(map(str.upper,city))
# print(upper)


# length of city with lambda
city=["ahemdabad","baroda","limbdi","rajkot"]
length=list(map(lambda c:len(c),city))
print(length)


# upper city with lambda
city=["ahemdabad","baroda","limbdi","rajkot"]
upper=list(map(lambda c:str.upper(c),city))
print(upper)