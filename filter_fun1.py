def length_gre(city):
    if len(city)>7:
        return city
city=["ahemdabad","baroda","limbdi","rajkot"]
len_ans=list(filter(length_gre,city))
print(len_ans)