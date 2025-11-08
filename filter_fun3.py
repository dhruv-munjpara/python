# Lab task : convert those city into upper case whose length is more then 5
city=["ahemdabad","ramol","limbdi","rajkot","kheda","dholka"]
def city_len(city):
    if  len(city)>5:
        return city

new_city=list(filter(city_len,city))
print(new_city)
new_city_upper=list(map(str.upper,new_city))
print(new_city_upper)