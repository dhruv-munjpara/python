# email validation
import re
lst_email=['ndkjn@gmail.com','123@fjjjej.in','123@yahoo.com','234e.sfd@gmail.com','dhqdhdu0','wdsfv12@gmail.com']
for i in lst_email:
    match=re.search(r'\w+@[a-z]+\.(com|in)$',i)
    if match:
        print(f'{i} valid mail')
    else:
        print(f'{i} invalid mail')