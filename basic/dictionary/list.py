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

print(drives[0])
#ถ้าอยากได้ serial ของตัวแรก
print(drives[0]["serial"])