from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)
df["is_failure"] = df["result"].eq("FAIL")

summary = df.groupby("machine", as_index=False).agg(
    total_count=("serial", "count"),
    fail_count=("is_failure", "sum"),
    failure_rate=("is_failure", "mean"),
)
summary["failure_rate"] = (summary["failure_rate"] * 100).round(2)

print(summary)