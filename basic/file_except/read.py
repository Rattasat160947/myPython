#read() อ่านทุกบรรทัด
with open("./files/result.txt", "r") as file:
    data = file.read()
    
print(type(data))

#readline() อ่านบรรทัดเดียว
with open("./files/result.txt" , "r") as file :
    line = file.readline()
    
print(line)

#readlines() อ่านทุกบรรทัดเป็น List

with open("./files/result.txt" , "r") as file:
    lines = file.readlines()
    
print(lines)

with open("./files/result.txt" , "r") as file:
    for line in file:
        data = line.strip().split(",")
        
        serial = data[0]
        result = data[1]
        
        print(f"{serial} -> {result}")