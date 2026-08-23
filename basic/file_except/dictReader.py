import csv

with open("./files/data.csv" , "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
with open("./files/data.csv" , "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["serial"])
with open("./files/data.csv" , "r") as file:
    reader = csv.DictReader(file)
         
    for row in reader: 
        if row["result"] == "FAIL":
            print(row["serial"])