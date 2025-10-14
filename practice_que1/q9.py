#  "Count frequency of list items and write in into dictionary :input List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
#     output : {1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2}"

List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
freq_dict={}
for i in List1:
    if i in freq_dict:
        freq_dict[i]+=1
    else:
        freq_dict[i]=1
print(freq_dict)