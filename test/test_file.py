#1
with open("./files/result.txt" ,"r") as file:
    try:
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print("Invalid File")
#2
line = "A002,FAIL"
data = line.strip().split(",")
serial = data[0]
result = data[1]
print(f"Serial: {serial}\nResult: {result}")
#3
temperature = "79.2"

temp = float(temperature)
if temp > 75:
    print("High Temperature")
#4
value = "abc"
try :
    temperature = float(value)
    print(f"Value: {temperature}")
except ValueError:
    print("Invalid Float")
#5
rows = [
    {"serial": "A001", "temperature": "68.5", "result": "PASS"},
    {"serial": "A002", "temperature": "79.2", "result": "FAIL"},
    {"serial": "A003", "temperature": "74.1", "result": "FAIL"}
]
for r in rows:
    try:
        if r["result"] == "FAIL" and float(r["temperature"]) > 75 :
            print(r["serial"])
    except ValueError:
        print("Invalid temperature")