import pandas as pd
data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "temperature": [68.5, None, 74.1, 82.5],
    "result": ["PASS", "FAIL", None, "PASS"]
}

df = pd.DataFrame(data)
# ตรวจค่าว่าง
print(df.isna())
#ตรวจว่ามี column หายกี่ตัว
print(df.isna().sum())