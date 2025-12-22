def personDetails(**kwargs):
    if kwargs['age']>=30:
        print(kwargs['name'])
def details():
    return 1,"dhruv",30,"python"
personDetails(name="dhruv",age=30)
personDetails(city="limbdi",name="ram",age=30)
personDetails(name="Abhijit",age=22)
personDetails(name="etets",age=30)
print(details())