"""
ตัวอย่างการจัดรูปแบบข้อความ
"""

# ใช้ % operator
name = "สมชาย"
age = 15
score = 85.5
print("ชื่อ: %s, อายุ: %d" % (name, age))
print("คะแนน: %.1f" % score)

# ใช้ format() method
print("ชื่อ: {}, อายุ: {}".format(name, age))
print("คะแนน: {:.1f}".format(score))

# ใช้ f-string (Python 3.6+)
print(f"ชื่อ: {name}, อายุ: {age}")
print(f"คะแนน: {score:.1f}")

# ตัวอย่างการจัดรูปแบบตาราง
print("\n=== ข้อมูลนักเรียน ===")
print("ชื่อ\t\tอายุ\tคะแนน")
print("-" * 30)
print(f"{name}\t\t{age}\t{score}")
print("สมหญิง\t\t16\t90.0")

# ตัวอย่างการจัดรูปแบบกรอบ
print("\n+----------------+")
print("|    สวัสดี     |")
print("+----------------+") 