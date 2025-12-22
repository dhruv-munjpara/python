# - Write a function create_frequency_dict(lst) that accepts a list and returns a dictionary where the keys are the elements of the list, and the values are the count of how often each element appears.
def frequency_dict(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
lst = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = frequency_dict(lst)
print(result)
