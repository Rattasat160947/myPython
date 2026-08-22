def show_drive(drive):
    print(f"{drive['serial']} -> {drive['result']}")
    
drive = {
    "serial": "A001",
    "result": "FAIL"
}

show_drive(drive)

def is_failed(drive):
    return drive["result"] == "FAIL"
drive = {
    "serial": "A001",
    "result": "FAIL"
}

print(is_failed(drive))