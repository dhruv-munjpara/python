# # Lab task : convert those city into upper case whose length is more then 5
# city=["ahemdabad","ramol","limbdi","rajkot","kheda","dholka"]
# def city_len(city):
#     if  len(city)>5:
#         return city

# new_city=list(filter(city_len,city))
# print(new_city)
# new_city_upper=list(map(str.upper,new_city))
# print(new_city_upper)


#Lab task : convert those city into upper case whose length is more then 5  with lambda
city=["ahemdabad","ramol","limbdi","rajkot","kheda","dholka"]
result=list(map(lambda c:c.upper() if len(c)>5 else c,city))
print(result)
 

#Lab task : convert  city into upper case whose length is more then 5  with lambda
city=["ahemdabad","ramol","limbdi","rajkot","kheda","dholka"]
result=list(filter(lambda c:len(c)>5,city))
print("whose len is greter then 5",result)
result1=list(map(lambda c:c.upper(),result))
print("upper city",result1)