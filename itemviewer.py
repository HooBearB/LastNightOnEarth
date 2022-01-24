import json
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/items.json'))
items = json.load(open(filename, "r"))

while 1 == 1:
    item = input("\nItem?\n")
    print(items[item]["1"])
    print(items[item]["2"])
    print(items[item]["3"])
    print(items[item]["4"])
    print(items[item]["5"])