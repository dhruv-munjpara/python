# fruits={'apple':{'qty':2,'price':120},'banana':{'qty':1,'price':40}}

# def view_fruit():
#     """return the current fruit stock"""
#     return fruits
import json
import os

file = "fruits.json"

def load_fruits():
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    else:
        return {
            "apple": {"qty": 2, "price": 120},
            "banana": {"qty": 1, "price": 40}
        }

def save_fruits(fruits):
    with open(file, "w") as f:
        json.dump(fruits, f, indent=4)

# load fruits every time program starts
fruits = load_fruits()
