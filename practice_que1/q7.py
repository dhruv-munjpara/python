# Write a Python program that uses `map()` to convert a list of strings to uppercase. 
# Input: `['apple', 'banana', 'cherry']` -
#  Output: `['APPLE', 'BANANA', 'CHERRY']`
  
fruits=['apple', 'banana', 'cherry']
upper_fruits=list(map(str.upper,fruits))

print(upper_fruits)