try:
    temperature = float("abc")
except ValueError:
    print("Invalid temperature")
    
value = input("Temperature: ")
try:
    temperature =float(value)
    print(f"Temperature: = {temperature}")
except ValueError:
    print("Invalid temperature!!!")
    
def failure_rate(fail, total):
    try:
        return fail / total * 100
    except ZeroDivisionError:
        return 0
print(failure_rate(0,3))

try:
    with open("result.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File Not Found")