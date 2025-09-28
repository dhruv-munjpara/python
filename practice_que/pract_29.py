# factoral serise
n=int(input("enter a number:"))
fact=1
sum_series=1

print("1/0!=1")

for i in range(1,n+1):
    fact*=i
    term=1/fact
    sum_series+=term
    print(f"1/{i}!={term}")

print(f"\n sum of fact series upto 1/{n}! is:{sum_series}")