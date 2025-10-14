# Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
# cel=[0,25,100]

# def cel_to_fer(c):
#     return (c*9/5)+32

# fer=list(map(cel_to_fer,cel))
# print(fer)

# with out using function

cel=[0,25,100]
fer=[]
for c in cel:
    f=(c*9/5)+32
    fer.append(f)

print(fer)