class emp:
    def __init__(self,age):
        self.age=age
    
    def __lt__(self,obj):
        age1=self.age<obj.age
        return emp(age1)
    
    def dispaly(self):
        print(self.age)

e1=emp(3)
e2=emp(25)
e1.dispaly()
e2.dispaly()
e3=e1<e2
e3.dispaly()