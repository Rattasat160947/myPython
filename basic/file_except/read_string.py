import csv

with open("./files/data.csv" , "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        temp = float(row["temperature"])
        if temp > 75:
            print(f"High temp : {row["temperature"]}")
        else:
            print(f"Low temp : {row["temperature"]}")