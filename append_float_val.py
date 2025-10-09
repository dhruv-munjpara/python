# 7.add float numbers from list and list iteam were add from user.
# lst1=[]
# lst2=[12.3,42.2,71.2]
# # lst3=float(input("enter a floating val:"))
# for i in lst2:
#    print(lst1.append(lst2))

float_list = []

n = int(input("How many float numbers do you want to add? "))

for i in range(n):
    num = float(input(f"Enter float number {i+1}: "))
    float_list.append(num)

print("List of float numbers:", float_list)


