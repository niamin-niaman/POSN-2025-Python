# Python Variable Types

## Type

- สำหรับ Python ไม่มีการกำหนดประเภทตัวแปร
- เป็นทั้งข้อดีและข้อเสียในเวลาเดียวกัน

### Integer

```python
quantity = 100
year = 2024
temperature = -5
```

### Float

```python
height = 175.5
pi = 3.14159
discount = 0.15
```

### String

```python
name = "สมชาย"
city = "เชียงใหม่"
slogan = 'ทำวันนี้ให้ดีที่สุด'
address = """123 ถนนสุขุมวิท
แขวงคลองเตย เขตคลองเตย
กรุงเทพมหานคร 10110"""
```

### Boolean

```python
is_raining = False
has_passport = True
is_open = False
```

### List

```python
colors = ["แดง", "เขียว", "น้ำเงิน"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "สอง", 3.0, True]
```

### Dictionary

```python
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}
student = {
    "id": "6411234",
    "name": "วิชัย",
    "grades": {"math": 85, "science": 92}
}
menu = {
    "อาหาร": ["ข้าวผัด", "ผัดไทย", "ต้มยำกุ้ง"],
    "เครื่องดื่ม": ["น้ำเปล่า", "ชา", "กาแฟ"]
}
```

## Type Casting (การแปลงประเภทข้อมูล)

### การแปลงเป็น Integer (int)
```python
# แปลงจาก Float
print(int(3.14))      # 3
print(int(3.9))       # 3 (ปัดเศษลงเสมอ)

# แปลงจาก String
print(int("123"))     # 123

# แปลงจาก Boolean
print(int(True))      # 1
print(int(False))     # 0
```

### การแปลงเป็น Float (float)
```python
# แปลงจาก Integer
print(float(42))       # 42.0

# แปลงจาก String
print(float("3.14"))   # 3.14

# แปลงจาก Boolean
print(float(True))     # 1.0
print(float(False))    # 0.0
```

### การแปลงเป็น String (str)
```python
# แปลงจาก Integer/Float
print(str(42))         # "42"
print(str(3.14))       # "3.14"

# แปลงจาก Boolean
print(str(True))       # "True"

# แปลงจาก List
print(str([1, 2, 3]))  # "[1, 2, 3]"
```

### การแปลงเป็น Boolean (bool)
```python
# ค่าที่เป็น False: 0, 0.0, "", [], {}, None
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False
print(bool("hello"))   # True
print(bool([]))        # False
print(bool([1, 2]))    # True
```

### การแปลงเป็นระบบเลขฐานต่างๆ
```python
number = 42
print(bin(number))     # 0b101010 (เลขฐาน 2)
print(oct(number))     # 0o52 (เลขฐาน 8)
print(hex(number))     # 0x2a (เลขฐาน 16)
```

### ตัวอย่างการใช้งานจริง
```python
# การคำนวณราคา
price = "150.75"
quantity = "3"
total = float(price) * int(quantity)
print(f"ราคารวม: {total} บาท")  # 452.25 บาท

# การแสดงผลคะแนน
score = 85
max_score = 100
percentage = (score / max_score) * 100
print(f"คะแนน: {str(score)}/{str(max_score)} ({percentage}%)")  # 85/100 (85.0%)
```

## Input (การรับข้อมูล)

### การรับข้อมูลพื้นฐาน
```python
# รับข้อความจากผู้ใช้
name = input("กรุณาใส่ชื่อของคุณ: ")
print(f"สวัสดี {name}")
```

### การรับข้อมูลและแปลงประเภท
```python
# รับตัวเลขและแปลงเป็น int
age_str = input("กรุณาใส่อายุของคุณ: ")
age = int(age_str)

# รับตัวเลขและแปลงเป็น float
height_str = input("ส่วนสูง (เซนติเมตร): ")
height = float(height_str)
```

### การรับข้อมูลหลายค่า
```python
# รับข้อมูล 2 ค่าในบรรทัดเดียว
x, y = input("ใส่พิกัด x และ y: ").split()

# รับข้อมูลหลายค่าและแปลงเป็นตัวเลข
num1, num2, num3 = map(int, input("ใส่เลข 3 ตัว: ").split())
```

### ข้อควรระวัง
1. `input()` จะรับข้อมูลเป็น string เสมอ
2. ต้องแปลงประเภทข้อมูลก่อนนำไปคำนวณ
3. ควรมีการจัดการข้อผิดพลาด (error handling) เมื่อรับข้อมูล

### ตัวอย่างการใช้งานจริง
```python
# โปรแกรมคำนวณ BMI
height_str = input("ส่วนสูง (เซนติเมตร): ")
weight_str = input("น้ำหนัก (กิโลกรัม): ")

height_m = float(height_str) / 100  # แปลงเซนติเมตรเป็นเมตร
weight = float(weight_str)

bmi = weight / (height_m ** 2)
print(f"ค่า BMI ของคุณคือ: {bmi:.2f}")