import matplotlib.pyplot as plt
#ใช้ดูความสัมพันธ์ระหว่าง numeric variables 2 ตัว
speed = [100, 120, 140, 160, 180]
temperature = [60, 64, 70, 75, 82]

plt.scatter(speed, temperature)

plt.xlabel("Speed")
plt.ylabel("Temperature")
plt.title("Speed vs Temperature")

plt.show()