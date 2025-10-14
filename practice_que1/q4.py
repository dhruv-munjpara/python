# Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers
lst=[1,2,3,4,5,-1,-2,-3,-4,-5]
sum_of_p=0
sum_of_n=0
for i in lst:
    if i>0:
        sum_of_p=sum_of_p+i
    else:
        sum_of_n=sum_of_n+i
result=(sum_of_p,sum_of_n)
print(result)
