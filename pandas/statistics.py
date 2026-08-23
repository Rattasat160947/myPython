import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parents[1] / "files" / "data.csv"
df = pd.read_csv(csv_path)

print(df["temperature"])
print(df["temperature"].mean())
print(df["temperature"].max())
print(df["temperature"].min())
print(df["temperature"].sum())
print(df["temperature"].count())

avg = df["temperature"].mean()
print(f"Average temp: {avg:.2f}")

failed = df[df["result"] == "FAIL"]
total_fail = len(failed)

print(total_fail)
total_fail = (df["result"] == "FAIL").sum()
print(total_fail)