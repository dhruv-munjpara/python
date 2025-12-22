salse_data={"pen":{"product_discription":"pentoinc pen","price":10,"unit_sold":100},
            "notbook":{"product_discription":"dbms book","price":50,"unit_sold":190},
            "pencil":{"product_discription":"doms pencil","price":11,"unit_sold":30}
            }
for k,v in salse_data.items():
    if v["unit_sold"]>=100:
        print(k,v)