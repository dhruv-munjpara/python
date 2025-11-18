# they give a when is give error on this line
import traceback
try:
    no=input("enter a number:")
    no1=int(no)
    print(f"value is{no}")


    ans=no1/0
    print(ans)
except ZeroDivisionError:
    print("there is an zerodivision")
    traceback.print_exc()
except ValueError:
    print("there is a value error")


finally:
    print("have a grate day!!")

    