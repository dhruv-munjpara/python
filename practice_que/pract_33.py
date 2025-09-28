# orint half string in uppercase
string=input("enter a string:")
total=len(string)
half_string=total//2
print(half_string)
first_part=string[:half_string]
last_part=string[half_string:]
string1=first_part+last_part
print(string1)
half_part=first_part=string[:half_string].upper()
string2=half_part+last_part
print(string2)