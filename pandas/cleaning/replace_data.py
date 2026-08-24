import pandas as pd

data = {
    "result": [
        "FAIL",
        "FAILED",
        "FAIL",
        "FAILED",
        "PASS"
    ]
}

df = pd.DataFrame(data)

df["result"] = df["result"].replace(
    "FAILED","FAIL"
)

print(df)

