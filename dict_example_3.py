dict1 = {101 : ['Dhruv','Parimal','DS',23000],
         102 : ['Romil','C G Road' , 'Python' , 32000],
         205 : ['Dhruti' , 'Bhanagar' , 'python' , 23000],
         207 : ['Dharmishtha' , 'Parimal' , 'python-java-st' , 20000]
         }

for key,val in dict1.items():
    
    if val[3]>20000:
        print(key)
        for i in val:        
            print("\t",i)