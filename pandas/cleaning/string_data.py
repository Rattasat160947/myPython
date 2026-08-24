import pandas as pd

data = {
    "result": [
        " pass ",
        "FAIL  ",
        "faIL",
        "pass",
        "Pass "
    ]
}

df = pd.DataFrame(data)

df["result"] = (
    df["result"].str.strip().str.upper()
)

print(df)