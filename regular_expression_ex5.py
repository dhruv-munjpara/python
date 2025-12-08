import re
msg = "This is IND, This is NZD"
match=re.search(r"[D-Z]$",msg)
print(match)
match=re.search(r"NZD$",msg)
print(match)