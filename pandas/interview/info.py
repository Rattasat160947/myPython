from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

# ดูจำนวนแถว, column, dtype และค่าที่ไม่ว่าง
df.info()