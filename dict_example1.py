dict1={101: ["dhruv","parimal","ds",23000],
       102: ["romil","c g road","c",26000],
       105: ["dhruti","bhandari","python",19000],
       107: ["dharmistha","parimal","python-java",20000],
       }
for k,v in dict1.items():
         if v[3]>20000:

             print(k)
             for i in v:
                 print(f"\t{i}")


