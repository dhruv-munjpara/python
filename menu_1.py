while True:
    print ("1. Reverse of Number \n2. Find no of digits \n3. Count total even/odd digits from number \n4. check number is palindrom  \n5. Exit")
    choice=int(input("Please enter your choice :"))

    match choice:
        case 1:
            num=int(input("enter a number:"))
            print(num)
            temp=num
            rev=0
            while temp>0:
                degit=temp%10
                rev=rev*10+degit
                temp=temp//10
                print("Reversed number:", rev)
        case 2:
            num=int(input("enter a num:"))
            temp=num
            cnt=0
            while temp>0:
                cnt+=1
                temp//=10
            print(f"total no of digits{cnt}")
        case 3:
            even_num=0
            odd_num=0
            num=int(input("how many number you want to take"))
            for i in range(0,num+1):
                if i%2==0:
                    even_num+=1
                else:
                    odd_num+=1
            print("even num:",even_num)
            print("odd num:",odd_num)
        case 4:
            num=int(input("enter a number:"))
            temp=num
            rev=0
            while temp>0:
                 degit=temp%10
                 rev=rev*10+degit
                 temp=temp//10

            if num==rev:
                print("its a palindrome")
            else:
                print("its not palindrome")

        case 5:
            break
        case _:
            print("enter valid choice")