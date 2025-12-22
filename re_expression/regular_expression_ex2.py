import re
msg="this is beautigul, today is beautiful morning"
match=re.search(r"\Amorning",msg)
print(match)

# msg1="This is good Morning,good afternoon"
match1=re.search(r"\d+","test 122 123567")
print(match1)

lst=re.findall(r"\d+","test 122 123567")
for i in lst:
    print(i)
lst=re.findall(r"\d+","test 122 123567")