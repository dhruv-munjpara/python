month=input("enter a month:")

if month in ["january","march","may","july","august","octomber","december"]:
    print("31 days")
elif month in ["april","june","september","november"]:
    print("30 days")
elif month=="february":
    print("28 or 29 days")
else:
    print("invalid month")