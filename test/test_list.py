#1
serials = ["A001", "A002", "A003"]
print(serials[1])
#2
serials[1] = "B002"
print(serials)
#3
serials = ["A001", "A002"]
serials.append("A003")
print(serials)
#4
serials = ["A001", "A002", "A003"]
serials.remove("A002")
print(serials)
#5
serials = ["A001", "A002", "A003"]
remove = serials.pop(2)
print(remove)
print(serials)
#6
temperatures = [72.5, 65.2, 80.1, 68.4]
temperatures.sort(reverse=True)
print(temperatures) 
#7
results = ["PASS", "FAIL", "PASS", "FAIL", "FAIL"]
for i in results:
    print(i)
#8
results = ["PASS", "FAIL", "PASS", "FAIL", "FAIL","fail"]
total_fail = 0
for i in results:
    if i.upper() == "FAIL" :
        total_fail += 1
print(f"Total FAIL = {total_fail}")