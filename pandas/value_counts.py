import pandas as pd

data = {
    "serial": ["A001", "A002", "A003", "A004"],
    "machine": ["M01", "M02", "M01", "M02"],
    "temperature": [68.5, 79.2, 74.1, 82.5],
    "result": ["PASS", "FAIL", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

print(df["result"].value_counts())
print(df["machine"].value_counts())
print(df["result"].value_counts(normalize=True))

percentage = df["result"].value_counts(normalize=True) * 100

print(percentage)