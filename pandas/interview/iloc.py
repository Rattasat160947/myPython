from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

# .iloc เลือกด้วยตำแหน่ง เริ่มจาก 0
print(df.iloc[0:3, 0:3])
print(df.iloc[0, :])