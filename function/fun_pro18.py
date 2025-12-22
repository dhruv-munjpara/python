# - Write a function concatenate_with_separator(lst, separator) that accepts a list of strings and a separator string, then returns a new string where all elements of the list are joined using the separator.
def concatenate_separator(lst, separator):
    return separator.join(lst)

lst = ["apple", "banana", "cherry"]
separator = ", "
result = concatenate_separator(lst, separator)
print(result)
