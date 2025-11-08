# - Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and returns a single dictionary that contains the merged key-value pairs from both dictionaries.
dict1={1:"one",2:"two",3:"three"}
dict2={4:"four",5:"five",6:"six"}
def merge_dicts(dict1,dict2):
     merged = dict1 | dict2   #  | (pipe symbol)
     return merged
print(merge_dicts(dict1,dict2))