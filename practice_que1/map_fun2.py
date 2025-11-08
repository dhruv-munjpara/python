# Write a Python program that uses `map()` to find the length of each string in a list of strings. Input: `['hello', 'world', 'python']` Output: `[5, 5, 6]`
def count_len(lst):
    return len(lst)
lst=['hello', 'world', 'python']
new_lst=list(map(count_len,lst))
print(new_lst)