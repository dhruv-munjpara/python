# - Write a function that accepts a number and returns the sum of its digits.
def sum_of_digit(num):

    sum=0
    for i in str(num):
        sum+=int(i)
    print(sum)

num=int(input("enter a num:"))
sum_of_digit(num)
