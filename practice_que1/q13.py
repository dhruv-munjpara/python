    # "Write a program to create a dictionary having data like 
    # {
    # Ahemdabad : ((""Ambawadi"", 380006) ,(""Bodakdev"",380054),(""Gandhi Ashram"",380027)),
    # Mumbai : ((""Mandvi"",400003),(""Mumbai Central"",400008),(""Worli"",400018))
    # } 

    # output If user enters Mumbai : then output is area Mandvi -->400003 , Mumbai Central --> 400008, Worli-->400018
    # if user enter 400018 then output  Worli , Mumbai
    # if user enters Mandvi then output is pin code is 400003 and it's in Mumbai"

cities={
    "Ahemdabad" : (("Ambawadi", 380006) ,("Bodakdev",380054),("Gandhi Ashram",380027)),
    "Mumbai" : (("Mandvi",400003),("Mumbai Central",400008),("Worli",400018))
    } 
# it is give city of dict
# city_name=input("enter a name:")
# print(cities[city_name])



# output If user enters Mumbai : then output is area Mandvi -->400003 , Mumbai Central --> 400008, Worli-->400018

city_name=input("enter a name:")
if city_name in cities:
    for area,pin in cities[city_name]:
        print(f"{area}--->{pin}")


# if user enter 400018 then output  Worli , Mumbai
pin_code=int(input("enter a pin_code:"))
for k,v in cities:
    if pin==pin_code:
        print(area,",",city_name)



# if user enters Mandvi then output is pin code is 400003 and it's in Mumbai"
for city, data in cities.items():
    for area, code in data:
            print("Pin code is", code, "and it's in", city)