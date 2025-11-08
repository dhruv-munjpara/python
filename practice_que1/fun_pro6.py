# - Write a function that accepts a list of strings and returns the longest string in the list.
lst=["dhruv","het","deep","tarang","miten"]
def longest_string():
    longest=""
    for i in lst:
        if len(i)>len(longest):
            longest=i
    return longest
print(longest_string())