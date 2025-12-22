# diff btw re.search() and re.match
import re
text = "Hello, welcome to the world of Python."
match_result=re.match(r"welcome",text)
print(match_result)
search_result=re.search(r"welcome",text)
print(search_result)