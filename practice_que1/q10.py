#  "Find the total income from sales, considering only items that sold more than 100 units sales_data = [
#     {""product"": ""Pen"", ""price"": 10, ""units_sold"": 150},
#     {""product"": ""Notebook"", ""price"": 50, ""units_sold"": 90},
#     {""product"": ""Pencil"", ""price"": 5, ""units_sold"": 300},
#     ]"


details=[ {"product": "Pen", "price": 10, "units_sold": 150},
        {"product": "Notebook", "price": 50, "units_sold": 90},
        {"product": "Pencil", "price": 5, "units_sold": 300}
         ]
total_income=0
for item in details:
        if item["units_sold"]>100:
            total_income+=item["price"]*item["units_sold"]

print("total income",total_income)

