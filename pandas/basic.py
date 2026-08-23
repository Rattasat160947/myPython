rows = [
    {"serial": "A001", "temperature": 68.5, "result": "PASS"},
    {"serial": "A002", "temperature": 79.2, "result": "FAIL"},
    {"serial": "A003", "temperature": 74.1, "result": "FAIL"}
]
#DataFrame = ตารางข้อมูลของ Pandas
import pandas as pd

df = pd.DataFrame(rows)

print(df)