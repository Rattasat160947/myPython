drives = [
    {
        "serial": "A001",
        "temperature": 68.5,
        "result": "PASS"
    },
    {
        "serial": "A002",
        "temperature": 79.2,
        "result": "FAIL"
    },
    {
        "serial": "A003",
        "temperature": 70.1,
        "result": "PASS"
    }
]

for drive in drives:
    print(f'{drive["serial"]} = {drive["result"]}')
    
#Filter หา Drive ที่ FAIL
for drive in drives:
    if drive["result"] == "FAIL":
        print(drive["serial"])
        
        failed_drives = []
#เก็บ Drive ที่ FAIL
for drive in drives:
    if drive["result"] == "FAIL":
        failed_drives.append(drive)

print(failed_drives)