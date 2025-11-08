# Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`


def c_to_f(lst):
    f=(lst*9/5)+32
    return f
lst=[0,25,100]
ans=list(map(c_to_f,lst))
print(ans)