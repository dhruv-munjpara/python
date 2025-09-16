#1. Write a python program to sum of the first n positive integers.
n=int(input("enter a positive integer:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum of first",n,"positive integers is:",sum)

