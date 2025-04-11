"""
Float Examples in Python
ตัวอย่างการใช้ตัวแปรประเภท Float (ทศนิยม)
"""

# ตัวอย่างการประกาศตัวแปร Float
print("\n=== ตัวอย่างการประกาศตัวแปร Float ===")
height = 175.5
pi = 3.14159
discount = 0.15

print("height =", height)
print("pi =", pi)
print("discount =", discount)

# ตัวอย่างการคำนวณพื้นฐาน
print("\n=== ตัวอย่างการคำนวณพื้นฐาน ===")
a = 10.5
b = 3.2

print("a + b =", a + b)  # บวก
print("a - b =", a - b)  # ลบ
print("a * b =", a * b)  # คูณ
print("a / b =", a / b)  # หาร
print("a // b =", a // b)  # หารปัดเศษลง
print("a % b =", a % b)  # เศษ
print("a ** b =", a ** b)  # ยกกำลัง

# ตัวอย่างการปัดเศษ
print("\n=== ตัวอย่างการปัดเศษ ===")
number = 3.14159

print("ปัดเศษทศนิยม 2 ตำแหน่ง:", round(number, 2))
print("ปัดเศษขึ้น:", round(number + 0.5))
print("ปัดเศษลง:", round(number - 0.5))

# ตัวอย่างการแปลงประเภทข้อมูล
print("\n=== ตัวอย่างการแปลงประเภทข้อมูล ===")
number = 42.7

print("แปลงเป็นข้อความ:", str(number))
print("แปลงเป็นจำนวนเต็ม:", int(number))
print("แปลงเป็นจำนวนเต็มแบบปัดเศษ:", round(number)) 