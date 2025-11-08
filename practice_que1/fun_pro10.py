# - Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
lst=["dhruv","het","tarang","deep","darshan","sumo","miten"]

def odd_length(lst):
    lst1=[]
    for i in lst:
        if int(len(i))%2 != 0:
            lst1.append(i)
    return lst1

print(odd_length(lst))