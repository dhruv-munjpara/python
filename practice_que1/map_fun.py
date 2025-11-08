# Write a Python program that uses the `map()` function to square each number in a given list of integers. Input: `[1, 2, 3, 4]` , Output: `[1, 4, 9, 16]`
def squre(num):
    return num*num
lst=[1,2,3,4]
nums_squre=list(map(squre,lst))
print(nums_squre)