# file=open("textfile.txt","w")
# file.write("hello my name id dhruv \n")
# file.write("how are you?")


# with input
# file=open("textfile.txt","w")
# data=input("enter string to write")
# file.write(data)
# print("data wrritten succsessfully")



# data should be entered upto "end" and also insertes in to file
# file=open("textfile.txt","w")
# while True:
#     data=input("enter string to write")
#     if data.lower()== 'exit':
#         break
#     file.write(data + '\n')
#     print("data wrritten succsessfully")
# file.close()




# with open('textfile.txt','r') as file:
#     data=file.read()
#     print(data)




# lab task
# file=open("textfile.txt","w")
# list1=[]
# while True:
#     data=input("enter string to write to file (type 'exit' to stop)")
#     if data.lower()== 'exit':
#         break
#     list1.append(data +'\n')
# file.writelines(list1)
# print("data wrritten succsessfully")
# file.close()


f1 = open("textfile.txt", "r")   # file to read
f2 = open("b.txt", "w")   # file to write

f2.write(f1.read())       # copy data

f1.close()
f2.close()

print("Copied!")