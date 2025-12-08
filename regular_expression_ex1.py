import re
msg="this is beautiful 2345 morning"
match=re.search(r"this",msg)
print(match)
match=re.search(r"\d",msg)
print(match)
match1=re.match(r"\d",msg)
print(match1)

if match:
    print(f"{match.start()}--{match.end()}--{match.span()}")