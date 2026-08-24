from pathlib import Path

import pandas as pd


csv_path = Path(__file__).resolve().parents[2] / "files" / "data.csv"
df = pd.read_csv(csv_path)

df = df.rename(columns={"result": "test_result", "temperature": "temp_c"})
print(df.head())