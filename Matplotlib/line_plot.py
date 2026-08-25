import matplotlib.pyplot as plt
#ดูแนวโน้มของข้อมูลตามเวลา / ลำดับ 
serials = ["A001", "A002", "A003", "A004"]
temperatures = [68.5, 79.2, 74.1, 82.5]

plt.plot(serials, temperatures)

plt.xlabel("Serial")
plt.ylabel("Temperature")
plt.title("Drive Temperature")

plt.show()
