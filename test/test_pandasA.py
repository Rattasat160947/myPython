import pandas as pd

data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "machine": ["M01", "M02", "M01", "M02"],
    "temperature": [68.5, 79.2, 74.1, 82.5],
    "result": ["PASS", "FAIL", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

#1
print(df.head(3))
#2
print(df[["serial" , "temperature"]])
#3
failed = df[df["result"] == "FAIL"]
print(failed)
#4
filter = df[(df["result"] == "FAIL") & (df["temperature"] > 75)]
print(filter)
#5
avg = df["temperature"].mean()
print(avg)
#6
max_temp = df["temperature"].max()
print(max_temp)
#7
drive = df[
    (df["machine"] == "M02") & (df["temperature"] > 80)
]
print(drive[["serial" ,"result"]])