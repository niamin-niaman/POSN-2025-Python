"""
Boolean Examples in Python
ตัวอย่างการใช้ตัวแปรประเภท Boolean (ค่าตรรกะ)
"""

# ตัวอย่างการประกาศตัวแปร Boolean
print("\n=== ตัวอย่างการประกาศตัวแปร Boolean ===")
is_raining = False
has_passport = True
is_open = False

print("is_raining =", is_raining)
print("has_passport =", has_passport)
print("is_open =", is_open)

# ตัวอย่างการเปรียบเทียบที่ได้ค่า Boolean
print("\n=== ตัวอย่างการเปรียบเทียบที่ได้ค่า Boolean ===")
x = 5
y = 10

print("x > y:", x > y)    # มากกว่า
print("x < y:", x < y)    # น้อยกว่า
print("x == y:", x == y)  # เท่ากัน
print("x != y:", x != y)  # ไม่เท่ากัน
print("x >= y:", x >= y)  # มากกว่าหรือเท่ากัน
print("x <= y:", x <= y)  # น้อยกว่าหรือเท่ากัน

# ตัวอย่างการใช้ตัวดำเนินการตรรกะ
print("\n=== ตัวอย่างการใช้ตัวดำเนินการตรรกะ ===")
a = True
b = False

print("a and b:", a and b)  # และ
print("a or b:", a or b)    # หรือ
print("not a:", not a)      # ไม่
print("not b:", not b)      # ไม่

# ตัวอย่างการใช้ Boolean ในการตัดสินใจ
print("\n=== ตัวอย่างการใช้ Boolean ในการตัดสินใจ ===")
age = 20
has_ticket = True

print("อายุมากกว่า 18:", age > 18)
print("มีตั๋ว:", has_ticket)
print("สามารถเข้าชมได้:", age > 18 and has_ticket) 