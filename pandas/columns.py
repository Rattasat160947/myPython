import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parents[1] / "files" / "data.csv"
df = pd.read_csv(csv_path)

print(df.columns)