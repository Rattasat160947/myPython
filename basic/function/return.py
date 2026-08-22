def failure_rate(fail, total):
    return fail / total * 100

rate = failure_rate(5, 100)
if rate > 3:
    print(f"High rate {rate}")