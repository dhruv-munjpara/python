# check mobaile is valid or invalid
import re
lst_co_no=['+1-1234567890','+91-9284093800','+33-45656513']
for i in lst_co_no:
    match=re.search(r'\+\d{1,2}-\d{10}',i)
    if match:
        print(f'{i} valid')
    else:
        print(f'{i} invalid')