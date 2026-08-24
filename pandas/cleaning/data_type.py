import pandas as pd

data = {
    "temperature": [
        "68.5",
        "79.2",
        "error",
        "82.5"
    ]
}

df = pd.DataFrame(data)

df["temperature"] = pd.to_numeric(
    df["temperature"],
    errors="coerce"
)

print(df.isna().sum())

df = df.dropna(
    subset=["temperature"]
)

df["temperature"] = (
    df["temperature"].astype(float)
)

print(df)