
n = int(input("Enter the value of n: "))

sum_series = 0
factorial = 1
series_str = ""  

for i in range(1, n + 1):
    factorial *= i
    sum_series += 1 / factorial
    
    if i == 1:
        series_str += f"1/{i}!"
    else:
        series_str += f" + 1/{i}!"

print("Series:", series_str)
print("Sum of series:", sum_series)
