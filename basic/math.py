import math

# ----- Operator ทางคณิตศาสตร์พื้นฐาน -----
a = 10
b = 3

print(a + b)    # บวก      -> 13
print(a - b)    # ลบ       -> 7
print(a * b)    # คูณ      -> 30
print(a / b)    # หารปกติ (ได้ float เสมอ) -> 3.333...
print(a // b)   # หารปัดเศษลง (floor division) -> 3
print(a % b)    # หารเอาเศษ (modulo) -> 1
print(a ** b)   # ยกกำลัง (a ยกกำลัง b) -> 1000

# ----- ลำดับการคำนวณ (Operator Precedence) -----
# ** > * / // % > + -
result = 2 + 3 * 4 ** 2   # ทำ ** ก่อน -> คูณ -> บวก
print(result)             # -> 2 + 3*16 = 50

# ----- ฟังก์ชันคณิตศาสตร์พื้นฐานในตัว Python (built-in) -----
print(abs(-7))          # ค่าสัมบูรณ์ -> 7
print(round(3.14159, 2))  # ปัดเศษทศนิยม 2 ตำแหน่ง -> 3.14
print(pow(2, 5))         # ยกกำลัง เหมือน 2 ** 5 -> 32
print(max(3, 7, 1))      # ค่ามากสุด -> 7
print(min(3, 7, 1))      # ค่าน้อยสุด -> 1
print(sum([1, 2, 3, 4]))  # ผลรวม -> 10

# ----- โมดูล math -----
print(math.sqrt(16))     # รากที่สอง -> 4.0
print(math.floor(3.9))   # ปัดลง -> 3
print(math.ceil(3.1))    # ปัดขึ้น -> 4
print(math.pi)           # ค่า pi -> 3.14159...
print(math.factorial(5))  # แฟกทอเรียล 5! -> 120
print(math.gcd(12, 18))  # ห.ร.ม. -> 6

# ----- ตัวดำเนินการเปรียบเทียบ (Comparison) -----
print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True

# ----- ตัวดำเนินการกำหนดค่าแบบย่อ (Compound Assignment) -----
x = 5
x += 1  # เหมือน x = x + 1 -> 6
x -= 1  # เหมือน x = x - 1 -> 5
x *= 2  # เหมือน x = x * 2 -> 10
x /= 2  # เหมือน x = x / 2 -> 5.0
print(x)
