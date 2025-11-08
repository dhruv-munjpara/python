# Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
lst=['apple', 'banana', 'cherry']
lst_upper=list(map(str.upper,lst))
print(lst_upper)
