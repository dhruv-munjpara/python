# "Filter active adults and get their names in uppercase
#     users = [
#     {""name"": ""Alice"", ""age"": 25, ""active"": True},
#     {""name"": ""Bob"", ""age"": 17, ""active"": False},
#     {""name"": ""Charlie"", ""age"": 35, ""active"": True}
#     ]"

users = [     
    {"name": "Alice", "age": 25, "active": True},
     {"name": "Bob", "age": 17, "active": False},
   {"name": "Charlie", "age": 35, "active": True} 
       ]

active_adults={user["name"].upper() for user in users if user["age"]>=18 and user["active"]}
print(active_adults)