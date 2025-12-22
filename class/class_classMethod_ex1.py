class person:
    name="python"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=person()
p1.changeName("dhruv")
print(p1.name)
print(person.name)