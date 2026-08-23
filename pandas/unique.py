import pandas as pd

data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "machine": ["M01", "M02", "M01", "M02"],
    "temperature": [68.5, 79.2, 74.1, 82.5],
    "result": ["PASS", "FAIL", "FAIL", "PASS"]
}

df = pd.DataFrame(data)
#ค่าไม่ซ้ำมีอะไรบ้าง
print(df["machine"].unique())
#มีกี่ค่าไม่ซ้ำ
print(df["machine"].nunique())