def show_drive(num):
    print(f"Drive: {num}")
    
show_drive(50)
show_drive("Test")

def show_result(serial, result):
    print(f"{serial} -> {result}")
    
show_result("A001", "PASS")
show_result("A002", "FAIL")