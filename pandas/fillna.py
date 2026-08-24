import pandas as pd
data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "temperature": [68.5, None, 74.1, 82.5],
    "result": ["PASS", "FAIL", None, "PASS"]
}

df = pd.DataFrame(data)
#แทน missing value
fill_df = df["temperature"] = df["temperature"].fillna(0)

print(fill_df)
# วิธีที่พบบ่อย

avg = df["temperature"].mean()

df["temperature"] = (
    df["temperature"].fillna(avg)
)
print(df)
