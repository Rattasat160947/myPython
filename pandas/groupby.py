import pandas as pd

data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "machine": ["M01", "M02", "M01", "M02"],
    "temperature": [68.5, 79.2, 74.1, 82.5],
    "result": ["PASS", "FAIL", "FAIL", "PASS"]
}

df = pd.DataFrame(data)
#แบ่งข้อมูลตาม machine
print(df.groupby("machine")["temperature"].max())
print(df.groupby("machine")["temperature"].min())
print(df.groupby("machine")["temperature"].count())

#agg() สรุปค่าในครั้งเดียว

summary = df.groupby("machine")["temperature"].agg(
    ["mean","min","max"]
)

print(summary)

#สมมุติอยากแยก: machine + result

summary2 = df.groupby(
    ["machine" ,"result"]
)["temperature"].mean()

print(summary2)