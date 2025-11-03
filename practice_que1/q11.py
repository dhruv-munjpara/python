    # "Write a prgram to extract unique values from List in dictionary (With Dict/Set comprehension) 
    # input 
    # dict_city_list = {'cityList1': ['Ahmedabad','Baroda', 'Bhopal', 'Mumbai'], 
    #   'cityList2': ['Baroda', 'Mumbai','Delhi', 'Chochi'], 
    #   'cityList3': [""Bhopal"",""Banglore"", ""Pune"", ""Mumbai""], 
    #   'cityList4': [""Delhi"",""Ahmedabad"", ""Pune"",""Chochi""]}
    # Output {'Banglore', 'Delhi', 'Pune', 'Ahmedabad', 'Mumbai', 'Bhopal', 'Baroda', 'Chochi'}


dict_city_list = {'cityList1': ['Ahmedabad','Baroda', 'Bhopal', 'Mumbai'], 
      'cityList2': ['Baroda', 'Mumbai','Delhi', 'Chochi'], 
      'cityList3': ["Bhopal","Banglore", "Pune", "Mumbai"], 
      'cityList4': ["Delhi","Ahmedabad", "Pune","Chochi"]}

unique_cities={city for cities in dict_city_list.values() for city in cities}
print(unique_cities)