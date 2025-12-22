name="Tops technologies pvt ltd"
#split
#join
lst=name.split()
print(lst)
lst1=name.split("t")
print(f"split bt t {lst1}")
Sentence="this is my python class and it will complate by 10"
print(len(Sentence))
#counting number of words from string
lst2=Sentence.split()
print(f"no of words===={len(lst2)}")
lst3=['apple','banana','cherry']
fruits=" ".join(lst3)
print(fruits)
fruits="*".join(lst3)
print(fruits)