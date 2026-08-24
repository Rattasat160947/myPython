import pandas as pd
data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "temperature": [68.5, None, 74.1, 82.5],
    "result": ["PASS", "FAIL", None, "PASS"]
}

df = pd.DataFrame(data)
#ลบเเถวที่มีข้อมูลว่าง
clean_df = df.dropna()
print(clean_df)
#ถ้าเราแคร์เฉพาะ temperature
clean_df = df.dropna(
    subset=["temperature"]
)
print(clean_df)