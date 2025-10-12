month=input("enter a month")
# if month in ("january",'March','May','July','octomber',"Descember"):
#     print("31 days")
# elif month in ("february"):
#     print(" 28 or 29 days ")
# elif month in ('April','June','August','September'):
#     print(" 30 days ")
# else:
#     print("invalid month")

match month:
    case 'January' | 'March' | 'May' | 'July' | 'octomber' | "Descember":
        print("31 days")
    case 'April' | 'June' | 'August' |'September':
        print("30 days")
    case "February":
        print("28 or 29 days")
    case _ :
        print("invalid input ")