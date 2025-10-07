# count number of digits
num = int(input("Enter a number: "))
cnt = 0
if num == 0:
    cnt = 1
else:
    while num > 0:
        num = num // 10
        cnt += 1

print("Number of digits:", cnt)
