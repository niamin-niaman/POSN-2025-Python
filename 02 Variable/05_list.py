"""
List Examples in Python
ตัวอย่างการใช้ตัวแปรประเภท List (รายการ)
"""

# ตัวอย่างการประกาศตัวแปร List
print("\n=== ตัวอย่างการประกาศตัวแปร List ===")
colors = ["แดง", "เขียว", "น้ำเงิน"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "สอง", 3.0, True]

print("colors =", colors)
print("numbers =", numbers)
print("mixed =", mixed)

# ตัวอย่างการเข้าถึงข้อมูลใน List
print("\n=== ตัวอย่างการเข้าถึงข้อมูลใน List ===")
print("colors[0] =", colors[0])      # ข้อมูลตัวแรก
print("colors[-1] =", colors[-1])    # ข้อมูลตัวสุดท้าย
print("colors[1:3] =", colors[1:3])  # ข้อมูลตั้งแต่ index 1 ถึง 2

# ตัวอย่างการเพิ่มข้อมูลใน List
print("\n=== ตัวอย่างการเพิ่มข้อมูลใน List ===")
fruits = ["แอปเปิ้ล", "กล้วย"]
print("List ก่อนเพิ่ม:", fruits)

fruits.append("ส้ม")           # เพิ่มต่อท้าย
print("หลัง append:", fruits)

fruits.insert(1, "ทุเรียน")   # เพิ่มที่ตำแหน่งที่ต้องการ
print("หลัง insert:", fruits)

# ตัวอย่างการลบข้อมูลใน List
print("\n=== ตัวอย่างการลบข้อมูลใน List ===")
print("List ก่อนลบ:", fruits)

fruits.remove("กล้วย")        # ลบข้อมูลที่ต้องการ
print("หลัง remove:", fruits)

popped = fruits.pop()         # ลบข้อมูลตัวสุดท้าย
print("หลัง pop:", fruits)
print("ข้อมูลที่ถูก pop:", popped)

# ตัวอย่างการค้นหาและนับข้อมูล
print("\n=== ตัวอย่างการค้นหาและนับข้อมูล ===")
numbers = [1, 2, 2, 3, 2, 4, 5]
print("numbers =", numbers)
print("จำนวนเลข 2:", numbers.count(2))
print("ตำแหน่งเลข 2 ตัวแรก:", numbers.index(2))

# ตัวอย่างการเรียงลำดับ
print("\n=== ตัวอย่างการเรียงลำดับ ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("List ก่อนเรียง:", numbers)

numbers.sort()                # เรียงจากน้อยไปมาก
print("หลังเรียงจากน้อยไปมาก:", numbers)

numbers.reverse()             # เรียงจากมากไปน้อย
print("หลังเรียงจากมากไปน้อย:", numbers) 