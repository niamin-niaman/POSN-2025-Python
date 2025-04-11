"""
ตัวอย่างการพิมพ์ข้อความซ้ำ
"""

# ใช้ * operator
print("=" * 20)
print("สวัสดี" * 3)
print("-" * 30)

# ใช้ loop # ยังไม่เรียน แต่ดูไว้ก่อน
for i in range(3):
    print("Hello")

# ใช้ loop พร้อมตัวเลข
for i in range(1, 4):
    print(f"ข้อความที่ {i}")

# ใช้ loop พร้อมการเยื้อง
for i in range(1, 4):
    print("\t" * i + "ยินดีที่ได้รู้จัก")

# ใช้ loop สร้างกรอบ
print("+" + "-" * 10 + "+")
for i in range(3):
    print("|" + " " * 10 + "|")
print("+" + "-" * 10 + "+") 