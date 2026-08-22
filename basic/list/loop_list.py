results = ["PASS", "FAIL", "PASS", "FAIL"]

fail_count = 0

for result in results:
    if result == "FAIL":
        fail_count = fail_count + 1

print(fail_count)