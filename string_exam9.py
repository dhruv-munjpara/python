#strip
#sort
name=" Tops Technologies"
print(len(name))
name=name.strip()
print(len(name))

print(sorted(name))
#word to be sorted from sentence
sentence="This is Tuesday "
lst=sentence.split()
sort_lst=sorted(lst)
print(f"original list{lst} and sorted list {sort_lst}")

sort_lst_len=sorted(lst,key=len)
print(f"original list{lst} and sorted list{sort_lst_len}")