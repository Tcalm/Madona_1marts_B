import csv

filename = "tests.csv"

with open(filename, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)