# Write a Python program that uses `map()` to add a given number to each element in a list. - Input: `[1, 2, 3, 4]`, `5` Output: `[6, 7, 8, 9]`
lst = [1, 2, 3, 4]
num = 5
def add_number(x):
    return x + num
result = list(map(add_number, lst))
print(result)
