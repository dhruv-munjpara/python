# import json
# with open('file1.json','r')as file:
#    data=json.load(file)
#    print(data)







import json
data={"rr":12}
with open('file1.json','w')as file:
   json.dump(data,file)
   print("data written succsessfully")