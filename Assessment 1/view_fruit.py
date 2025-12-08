# fruits={'apple':{'qty':2,'price':120},'banana':{'qty':1,'price':40}}

# def view_fruit():
#     """return the current fruit stock"""
#     return fruits
import json
import os
from datetime import datetime

file = "fruits.json"
log_file="transaction.log"

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


def log_transaction(action: str,details: str):
    """
    Append a timestamped line to transactions.log
    action: short action keyword (BUY, ADD, UPDATE, SAVE, EXIT, etc.)
    details: human readable details about the transaction
    """

    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line=f"[{ts}] {action}:{details}\n"
    with open(log_file,"a")as lf:
        lf.write(line)