import re
lst=re.findall(r"\d{10}","test 122 1235675133")
for i in lst:
    print(i)