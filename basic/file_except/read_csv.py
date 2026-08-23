import csv

with open("./files/data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)