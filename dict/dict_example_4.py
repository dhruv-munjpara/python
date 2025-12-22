# find a total
dict1 = {101 : ['Dhruv','Parimal','DS',90,80,70],
         102 : ['Romil','C G Road' , 'Python' , 70,80,90],
         205 : ['Dhruti' , 'Bhanagar' , 'python' , 50,60,70],
         207 : ['Dharmishtha' , 'Parimal' , 'python-java-st' , 90.70,60]
         }
result=[]
for k ,v in dict1.items():
    marks=v[3:]
    total=sum(marks)
    avg=total/3
    result.append((k,total,avg))

result=tuple(result)
print(result)