def count_fail(drives):
    total = 0

    for drive in drives:
        if drive["result"] == "FAIL":
            total += 1

    return total
drives = [
    {
    "serial": "A001",
    "result": "FAIL",
    },
    {
    "serial": "A002",
    "result": "FAIL"
    }
]

fail_count = count_fail(drives)

print(fail_count)