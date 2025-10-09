# 17.Write a python program using function to find the sum of odd series andevenseries
# Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n


n=int(input("enter a number:"))
odd_sum=0
odd_serise=""
for i in range(1,n+1,2):
    fact=1
    for j in range(1,i+1):
        fact*=j
    term=((i*10)+2)/fact
    odd_sum+=term
    odd_serise +=f"{(i*10)+2}/{i}!"
    if i+2<=n:
        odd_serise+="+"


even_sum=0
even_series=""
for i in range(2,n+1,2):
    fact=1
    for j in range(1,i+1):
        fact*=j
    term=((i*10)+2)/fact
    even_sum+=term
    even_series += f"{(i*10)+2}/{i}!"
    if i+2<=n:
        even_series+="+"

# print("sum of odd serise=",odd_sum)
# print("sum of even serise=",even_sum)

print("Odd Series : ", odd_serise , "=", odd_sum)
print("Even Series: ", even_series, "=", even_sum)