import matplotlib.pyplot as plt
#ใช้เปรียบเทียบ category
machines = ["M01", "M02"]
avg_temp = [71.3, 80.85]

plt.bar(machines, avg_temp)

plt.xlabel("Machine")
plt.ylabel("Average Temperature")
plt.title("Average Temperature by Machine")

plt.show()