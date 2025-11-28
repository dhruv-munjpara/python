class student:
    def __init__(self,name):
        self.name=name
s1=student("dhruv")
print(s1.name)  #this is print

del s1.name
print(s1.name) #this is give excption bcause we will del to s1.name


