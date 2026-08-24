from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

# สร้าง column จากเงื่อนไข
df["is_failure"] = df["result"] == "FAIL"
df["temperature_level"] = df["temperature"].ge(80).map(
    {True: "HIGH", False: "NORMAL"}
)

print(df)