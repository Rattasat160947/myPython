import pandas as pd

data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "machine": ["M01", "M02", "M01", "M02"],
    "temperature": [68.5, 79.2, 74.1, 82.5],
    "result": ["PASS", "FAIL", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

print(df.sort_values("temperature"))
#เรียงน้อย → มาก
sorted_df = df.sort_values(
    "temperature",
    ascending=False
)

print(sorted_df)
#มาก → น้อย ascending=False = descending

sorted_df = df.sort_values(
    "temperature",
    ascending=False
)

print(sorted_df.head(1))

print(
    sorted_df[
        ["serial", "temperature"]
    ].head(1)
)
#เรียง machine ก่อน แล้ว temperature มาก → น้อย

print(df.sort_values(
    ["machine", "temperature"],
    ascending=[True, False]
))