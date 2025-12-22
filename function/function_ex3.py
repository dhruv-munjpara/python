#parametrized function
def greet(name,grade,age):
    print("good moring",name,"your grade is",grade,"and age",age)
for i in range(3):
    n=input("enter name")
    g=input("enter grade")
    a=int(input("enter a age"))
    greet(n,g,a)