def read_file():
    file_name=input("enter a file name to read")
    with open(file_name,'r')as file:
        data=file.read()
        print(data)


def write_file():
    file_name=input("enter a file name to write")
    with open('b.txt','w')as file:
        data=input("enter the data to write in file")
        file.write(data)

def copy_file():
    File_name=input("enter a file name to read and copy")
    new_file=input("enter a file name to print in this file")
    f1=open(File_name,'r')
    f2=open(new_file,'w')
    f2.write(f1.read())       # copy data
    f1.close()
    f2.close()
    print("coppid!")

def append_file():
     file_name=input("enter a file name to write")
     with open(file_name,'a')as file:
            data=input("enter the data to write in file")
            file.write(data)
            print("append success!")

while True:
    print("1. read \n2. write \n3. copyFile \n4. append \n5. Exit")
    choice = int(input("Please enter your choice : "))
    match choice:
        case 1:read_file()
        case 2:write_file()
        case 3:copy_file()
        case 4:append_file()
        case 5:
            break
        case _:
            print("enter a valid choice:")
