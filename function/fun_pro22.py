# - Write a function merge_lists_into_dict(list1, list2) that accepts two lists of equal length and merges them into a dictionary where the keys are the indices (0 to n-1) and the values are the elements from both lists.
def merge_lists_into_dict(list1, list2):
    merged_dict = {}
    for i in range(len(list1)):
        merged_dict[i] = (list1[i], list2[i])
    return merged_dict
list1 = ["apple", "banana", "cherry"]
list2 = [10, 20, 30]
result = merge_lists_into_dict(list1, list2)
print(result)
