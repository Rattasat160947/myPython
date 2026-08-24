from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

# .loc เลือกด้วยชื่อ column หรือเงื่อนไข
print(df.loc[df["result"] == "FAIL", ["serial", "machine"]])
print(df.loc[df["temperature"] > 80, "serial"])