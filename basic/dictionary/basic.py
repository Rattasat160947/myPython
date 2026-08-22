drive = {
    "serial": "A001",
    "machine": "M02",
    "temperature": 68.5,
    "result": "FAIL"
}

print(drive["result"])
print(drive["temperature"])
drive["result"] = "PASS"
print(drive)
drive["result"] = "PASS"       # key มีอยู่ → แก้
drive["operator"] = "John"     # key ไม่มี → เพิ่ม
print(drive)
drive["operator"] = "John" #ซ้ำไม่เพิ่ม
print(drive)
