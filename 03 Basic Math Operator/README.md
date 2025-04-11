# ตัวดำเนินการทางคณิตศาสตร์พื้นฐานใน Python

### การบวก (+)
ใช้สำหรับการบวกตัวเลขหรือต่อข้อความ

```python
# การบวกตัวเลข
num1 = 10
num2 = 5
result = num1 + num2
print(result)  # Output: 15

# การต่อข้อความ
text1 = "Hello"
text2 = "World"
result = text1 + " " + text2
print(result)  # Output: Hello World
```

### การลบ (-)
ใช้สำหรับการลบตัวเลข

```python
num1 = 10
num2 = 3
result = num1 - num2
print(result)  # Output: 7

# การลบกับเลขติดลบ
negative = -5
positive = 10
result = positive - negative  # 10 - (-5) = 10 + 5
print(result)  # Output: 15
```

### การคูณ (*)
ใช้สำหรับการคูณตัวเลขหรือทำซ้ำข้อความ

```python
# การคูณตัวเลข
num1 = 5
num2 = 3
result = num1 * num2
print(result)  # Output: 15

# การทำซ้ำข้อความ
text = "Ha"
result = text * 3
print(result)  # Output: HaHaHa
```

### การหาร (/)
ใช้สำหรับการหารตัวเลข (ผลลัพธ์เป็นทศนิยม)

```python
num1 = 10
num2 = 4
result = num1 / num2
print(result)  # Output: 2.5

# ระวัง! การหารด้วยศูนย์จะเกิด error
# result = 10 / 0  # ZeroDivisionError
```

### การยกกำลัง (**)
ใช้สำหรับการยกกำลังตัวเลข

```python
base = 2
power = 3
result = base ** power  # 2 * 2 * 2
print(result)  # Output: 8

# การใช้เลขยกกำลังติดลบ
result = 2 ** -2  # 1 / (2 * 2)
print(result)  # Output: 0.25
```

### การหารเอาเศษ (%)
ใช้สำหรับหาเศษจากการหาร

```python
num1 = 17
num2 = 5
result = num1 % num2  # 17 หารด้วย 5 เหลือเศษ 2
print(result)  # Output: 2

# ใช้ตรวจสอบเลขคู่/คี่
number = 7
is_even = number % 2 == 0
print(f"Is {number} even? {is_even}")  # Output: False
```

### ตัวอย่างการใช้งานร่วมกัน

```python
# การคำนวณพื้นที่วงกลม
radius = 5
pi = 3.14
area = pi * (radius ** 2)
print(f"พื้นที่วงกลม = {area}")  # Output: 78.5

# การแปลงชั่วโมงเป็นนาฬิกา 12 ชั่วโมง
hours = 25
hours_12 = hours % 12 or 12  # ถ้าหารเหลือ 0 ให้แสดงเป็น 12
print(f"{hours} ชั่วโมง = {hours_12} นาฬิกา")  # Output: 25 ชั่วโมง = 1 นาฬิกา
``` 