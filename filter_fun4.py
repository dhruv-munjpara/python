# Lab task :  Convert temperatures from Celsius to Fahrenheit
def c_to_f(lst):
    f=(lst*9/5)+32
    return f
lst=[1,8,9]
ans=list(map(c_to_f,lst))
print(ans)