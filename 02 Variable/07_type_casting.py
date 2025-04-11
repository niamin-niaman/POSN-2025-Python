"""
Type Casting Examples in Python
ตัวอย่างการแปลงประเภทข้อมูล (Type Casting)
"""

# 1. การแปลงเป็น Integer (int)
print("\n=== การแปลงเป็น Integer ===")
print("float -> int:", int(3.14))      # 3
print("float -> int:", int(3.9))       # 3 (ปัดเศษลงเสมอ)
print("string -> int:", int("123"))     # 123
print("boolean -> int:", int(True))     # 1
print("boolean -> int:", int(False))    # 0

# 2. การแปลงเป็น Float (float)
print("\n=== การแปลงเป็น Float ===")
print("int -> float:", float(42))       # 42.0
print("string -> float:", float("3.14")) # 3.14
print("boolean -> float:", float(True))  # 1.0
print("boolean -> float:", float(False)) # 0.0

# 3. การแปลงเป็น String (str)
print("\n=== การแปลงเป็น String ===")
print("int -> string:", str(42))        # "42"
print("float -> string:", str(3.14))    # "3.14"
print("boolean -> string:", str(True))   # "True"
print("list -> string:", str([1, 2, 3])) # "[1, 2, 3]"

# 4. การแปลงเป็น Boolean (bool)
print("\n=== การแปลงเป็น Boolean ===")
# ค่าที่เป็น False: 0, 0.0, "", [], {}, None
print("int -> bool:", bool(0))          # False
print("int -> bool:", bool(1))          # True
print("float -> bool:", bool(0.0))      # False
print("string -> bool:", bool(""))      # False
print("string -> bool:", bool("hello")) # True
print("list -> bool:", bool([]))        # False
print("list -> bool:", bool([1, 2]))    # True

# 5. การแปลงเป็นระบบเลขฐานต่างๆ
print("\n=== การแปลงเป็นระบบเลขฐานต่างๆ ===")
number = 42
print("เลขฐาน 2 (binary):", bin(number))    # 0b101010
print("เลขฐาน 8 (octal):", oct(number))     # 0o52
print("เลขฐาน 16 (hex):", hex(number))      # 0x2a

# 6. ตัวอย่างการใช้งานจริง
print("\n=== ตัวอย่างการใช้งานจริง ===")
# แปลงข้อมูลจากการรับ input
price = "150.75"
quantity = "3"
total = float(price) * int(quantity)
print(f"ราคารวม: {total} บาท")  # 452.25 บาท

# การแปลงข้อมูลเพื่อแสดงผล
score = 85
max_score = 100
percentage = (score / max_score) * 100
print(f"คะแนน: {str(score)}/{str(max_score)} ({percentage}%)")  # 85/100 (85.0%) 