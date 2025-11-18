import traceback
try:
    no=int(input("enter number:"))
    print(no)
except:
    print("value error")
    traceback.print_exc()
else:
    print("in else")
finally:
    print("finally")
