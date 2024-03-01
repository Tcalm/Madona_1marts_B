import json
import csv

formats = input("Enter the file format (json, txt, or csv): ")
files = input("Enter the file name: ")

if formats == "json":
    with open(files, 'r') as f:
        data = json.load(f)
        print("JSON file contents:")
        print(data)

elif formats == "csv":
    with open(files, 'r') as f:
        data = csv.load(f)
        print("CSV file contents:")
        print(data)

with open(files, "r", encoding="utf-8") as file:
    data = file
    print("CSV file contents:")
    print(data)