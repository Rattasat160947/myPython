import pandas as pd
import matplotlib.pyplot as plt

data = {
    "serial": ["A001", "A002", "A003", "A004", "A005"],
    "machine": ["M01", "M02", "M01", "M02", "M01"],
    "temperature": [68.5, 79.2, 74.1, 82.5, 76.1],
    "result": ["PASS", "FAIL", "FAIL", "PASS", "FAIL"]
}

df = pd.DataFrame(data)

# Line
plt.plot(
    df["serial"],
    df["temperature"]
)

plt.xlabel("Serial")
plt.ylabel("Temperature")
plt.title("Temperature by Drive")

plt.show()

# Bar

result_count = df["result"].value_counts()

plt.bar(
    result_count.index,
    result_count.values
)

plt.xlabel("Result")
plt.ylabel("Count")
plt.title("Test Results")

plt.show()

#Scatter

df["speed"] = [
    100, 120, 110, 140, 125
]

plt.scatter(
    df["speed"],
    df["temperature"]
)

plt.xlabel("Speed")
plt.ylabel("Temperature")

plt.show()

#Histogram

plt.hist(
    df["temperature"],
    bins=5
)

plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.show()