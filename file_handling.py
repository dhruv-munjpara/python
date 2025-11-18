# its give all over file
# file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
# data=file.read(50)
# print(data)

# \ is taken as a character ,so for the path we use \\



# # its give only one line in file
# file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
# data1=file.readline()
# print(data1)



# if you want to allover file with readline()
# file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
# while True:
#     data1=file.readline()
#     if not data1:
#         break
#     print(data1)


# if you want all over line in list so you can use readlines()
# file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
# data1=file.readlines()
# print(data1)


# if you want to line of text you will use tell()
# file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
# print(f"before read {file.tell()}")
# data1=file.readlines()
# print(data1)
# print(f"after read {file.tell()}")




file=open("C:\\Users\\dhruv\\Downloads\\Code_Snippet.txt","r")
file.seek(100)
data1=file.readlines()
print(data1)