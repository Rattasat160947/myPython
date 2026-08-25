import matplotlib.pyplot as plt
# ใช้ดูการกระจาย
temperatures = [
    68.5, 69.2, 70.1,
    72.4, 74.5, 75.2,
    75.6, 78.1, 79.2,
    80.5, 82.5
]

plt.hist(
    temperatures,
    bins=5
)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")

plt.show()