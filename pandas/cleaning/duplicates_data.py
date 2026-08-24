import pandas as pd
data = {
    "serial": [
        "A001",
        "A002",
        "A002",
        "A003"
    ]
}

df = pd.DataFrame(data)

#ข้อมูลจริงอาจมี drive ซ้ำ

print(df.duplicated())

print(df.duplicated().sum())

df = df.drop_duplicates()
print(df)
#บางครั้งทั้ง row ไม่เหมือนกัน แต่ serial ซ้ำ
df = df.drop_duplicates(
    subset=["serial"]
)

print(df)