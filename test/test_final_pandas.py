import pandas as pd

data = {
    "serial": [
        " A001 ",
        "A002",
        "A003",
        "A004",
        "A005",
        "A006"
    ],

    "machine": [
        "M01",
        "M02",
        "M01",
        "M02",
        "M01",
        "M02"
    ],

    "temperature": [
        "68.5",
        "79.2",
        "error",
        "82.5",
        "76.1",
        None
    ],

    "result": [
        " pass ",
        "FAIL",
        "fail",
        "PASS",
        "FAIL",
        "PASS"
    ]
}

df = pd.DataFrame(data)
#1
print(df.head(5))
print("===========================")
#2
print(df.shape)
print("===========================")
#3
print(df.dtypes)
print("===========================")
#4
print(df.isna())
print("===========================")
#5
df["serial"] = df["serial"].str.strip()
print(df)
print("===========================")
#6
df["result"] = df["result"].str.strip().str.upper()
print(df)
print("===========================")
#7
df["temperature"] = pd.to_numeric(
    df["temperature"],
    errors="coerce"
)

df["temperature"] = (
    df["temperature"].astype(float)
)

print(df)
print("===========================")
#8
print(df.isna().sum())
print("===========================")
#9
clean_df = df.dropna(subset=["temperature"])
print(clean_df)
print("===========================")
#10
fail_df = df[df["result"] == "FAIL"]
print(fail_df)
print("===========================")
#11
filter_df = df[
    (df["result"] == "FAIL") & (df["temperature"] > 75)
]
print(filter_df)
print("===========================")
#12
avg = df["temperature"].mean()
print(avg)
print("===========================")
#13
max_temp = df["temperature"].max()
print(max_temp)
print("===========================")
#14
count_result = df["result"].value_counts()

print(count_result)
print("===========================")
#15
avg_temp = df.groupby("machine")["temperature"].mean()
print(avg_temp)
print("===========================")
#16
print(df.sort_values("temperature" ,ascending=False))
print("===========================")
#17
print(
    df[
        ["serial", "machine", "temperature", "result"]
    ]
)
print("===========================")
#18
df.to_csv("clean_result.csv" ,index=False)
new_df = pd.read_csv("clean_result.csv") #มันติดอะไรไม่รู้ดึงไม่ได้เเต่สร้างอะไรละ
print(new_df)
print("===========================")
