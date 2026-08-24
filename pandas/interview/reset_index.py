from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

summary = df.groupby("machine")["temperature"].mean()
print("ก่อน reset_index:")
print(summary)

summary = summary.reset_index()
print("หลัง reset_index:")
print(summary)