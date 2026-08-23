import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parents[1] / "files" / "data.csv"
df = pd.read_csv(csv_path)

failed = df[df["result"] == "FAIL"]

print(failed)

filtered = df[
    (df["result"] == "FAIL") &
    (df["temperature"] > 75)
]

print(filtered["serial"])