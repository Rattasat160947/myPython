from pathlib import Path

import pandas as pd


project_root = Path(__file__).resolve().parents[2]
csv_path = project_root / "files" / "data.csv"
output_path = project_root / "files" / "interview_machine_summary.csv"
df = pd.read_csv(csv_path)

summary = df.groupby("machine", as_index=False)["temperature"].mean()
summary = summary.rename(columns={"temperature": "average_temperature"})
summary.to_csv(output_path, index=False)

print(f"Saved: {output_path}")