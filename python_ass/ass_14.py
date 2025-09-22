# 14.Write a Python program to find the highest 3 values in a dictionary.
data={'a':5,'b':3,'c':9,'d':10,'e':7}

sorted_items=sorted(data.items(),key=lambda x:x[1],reverse=True)

top3=sorted_items[:3]

print("top 3 higgest values:")
for key,Value in top3:
    print(f"{key}:{Value}")