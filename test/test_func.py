#1
def show_serial(serial) :
    print(f"Serial: {serial}")
    
show_serial("A001")

#2
def add(a,b) :
    return a + b
num1, num2 = map(int, input("Input your number1 and number2 : ").split())

print(f"Sum {num1} + {num2} : {add(num1,num2)}")
#3
def failure_rate(fail, total):
    return fail / total * 100

print(failure_rate(3,100))
#4
def normalize_result(result):
    return result.strip().upper()

print(normalize_result("  fail "))
#5
def is_failed(drive):
    return drive["result"] == "FAIL"

drive = {
    "serial": "A001",
    "result": "FAIL"
}
    
print(is_failed(drive))
#6

drives = [
    {"serial": "A001", "result": "PASS"},
    {"serial": "A002", "result": "FAIL"},
    {"serial": "A003", "result": "FAIL"}
]

def count_fail(drives):
    total = 0
    for drive in drives:
        if drive["result"] == "FAIL":
            total += 1
    return total
    
total = count_fail(drives)

print(f"Total FAIL = {total}")