from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

is_failure = df["result"].eq("FAIL")
failure_count = is_failure.sum()
failure_rate = is_failure.mean() * 100

print(f"FAIL count: {failure_count}")
print(f"FAIL Rate: {failure_rate:.2f}%")