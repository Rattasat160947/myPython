drives = [
    {
        "serial": "A001",
        "machine": "M01",
        "temperature": 68.5,
        "result": "PASS"
    },
    {
        "serial": "A002",
        "machine": "M02",
        "temperature": 79.2,
        "result": "FAIL"
    },
    {
        "serial": "A003",
        "machine": "M01",
        "temperature": 74.1,
        "result": "FAIL"
    }
]
#1
print(drives[0]["serial"])
#2
#print(drives[1]["temperature"])
for drive in drives:
    if drive["serial"] == "A002" :
        print(drive["temperature"])
#3
for drive in drives:
    if drive["serial"] == "A003":
        drive["result"] = "PASS"
print(drives)
#4
for drive in drives:
    print(drive["serial"])
#5
drives[2]["result"] = "FAIL"
for drive in drives:
    print(f'{drive["serial"]} -> {drive["result"]}')
#6
for drive in drives:
    if drive["result"] == "FAIL" :
        print(drive["serial"])
#7
total = 0
for drive in drives:
    if drive["result"] == "FAIL" :
        total += 1
print(f"Total FAIL = {total}")
#8
failed_drives = []
for drive in drives:
    if drive["result"] == "FAIL" :
        failed_drives.append(drive)
        
print(failed_drives)