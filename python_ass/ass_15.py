'''15.Given a number n, write a python program to make and print the list of Fibonacci
series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13'''

num=int(input("enter a number:"))
next=1
prev=0
sum=0
for i in range(num+1):
    if i==0:
        sum=0
    else:
        prev=next
        next=sum
        sum=prev+next
    print(sum)



# num = int(input("Enter num: "))

# a, b = 0, 1
# sum = 0

# while sum < num:
#     print(a, end=" ")
#     a, b = b, a + b
#     sum += 1