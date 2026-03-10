import csv
import json

data = []

with open("supermarket.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for r in reader:
        data.append(r)

with open("supermarket.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent = 4)