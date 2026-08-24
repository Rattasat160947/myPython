from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

# apply เรียก function กับค่าทีละแถวใน column
df["temperature_level"] = df["temperature"].apply(
    lambda value: "HIGH" if value >= 80 else "NORMAL"
)

print(df[["serial", "temperature", "temperature_level"]])