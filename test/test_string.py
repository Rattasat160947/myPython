#1
serial1 = "DRV-A001"
print(serial1[0])
#2
serial2 = "DRV-A001"
print(serial2[4:])
#3
result3 = "   FAIL   "
print(result3.strip())
#4
data = "A001,M02,72.5,PASS"
list_data = data.split(",")
print(list_data)
#5
print(list_data[1])
#6
result6 = "fail"
print(result6.upper())
#7
serial7 = "A001"
temperature = 70.5
print(f"{serial7} temperature = {temperature} C")

#8 
raw = "  A015,M03,74.2,fail  "
data = raw.strip().split(",")
print(data)
print(f"Drive {data[0]} | Machine {data[1]} | temperature {data[2]} | Result {data[3].upper()}")