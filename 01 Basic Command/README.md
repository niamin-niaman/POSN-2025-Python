# Python Basic Command Examples

รวมตัวอย่างการใช้งาน Python พื้นฐาน สำหรับการแสดงผลข้อความในรูปแบบต่างๆ

### 1. การแสดงผลข้อความพื้นฐาน (`01_basic_print.py`)
การใช้คำสั่ง print() เพื่อแสดงผลข้อความพื้นฐาน
```python
print("Hello, World!")
print("สวัสดีชาวโลก")
```

### 2. การแสดงผลข้อความหลายบรรทัด (`02_multiline_print.py`)
การแสดงผลข้อความหลายบรรทัดด้วยวิธีต่างๆ
```python
# วิธีที่ 1: ใช้ \n
print("บรรทัดที่ 1\nบรรทัดที่ 2")

# วิธีที่ 2: ใช้ triple quotes
print("""
บรรทัดที่ 1
บรรทัดที่ 2
บรรทัดที่ 3
""")
```

### 3. การแสดงผลตัวเลข (`03_number_print.py`)
การแสดงผลตัวเลขในรูปแบบต่างๆ
```python
# ตัวเลขจำนวนเต็มและทศนิยม
print(42)
print(3.14)

# การคำนวณพื้นฐาน
print(10 + 5)
print(10 * 5)
```

### 4. การแสดงผลตัวแปร (`04_variable_print.py`)
การแสดงผลค่าจากตัวแปรในรูปแบบต่างๆ
```python
name = "สมชาย"
age = 25
print("ชื่อ:", name)
print("อายุ:", age, "ปี")
```

### 5. การจัดรูปแบบการแสดงผล (`05_format_print.py`)
การจัดรูปแบบการแสดงผลด้วย format() และ f-string
```python
name = "สมชาย"
age = 25
# แบบ format()
print("ชื่อ: {}, อายุ: {} ปี".format(name, age))
# แบบ f-string
print(f"ชื่อ: {name}, อายุ: {age} ปี")
```

### 6. การทำซ้ำข้อความ (`06_repeat_print.py`)
การแสดงผลข้อความซ้ำๆ ด้วยเครื่องหมาย *
```python
print("-" * 20)  # แสดง - ซ้ำ 20 ครั้ง
print("Python " * 3)  # แสดงคำว่า Python ซ้ำ 3 ครั้ง
```

### 7. การใช้ Escape Characters (`07_escape_character.py`)
การใช้อักขระพิเศษในการจัดรูปแบบข้อความ
```python
print("บรรทัดที่ 1\tย่อหน้า")  # \t สำหรับเว้นวรรค (tab)
print("บรรทัด\nใหม่")  # \n สำหรับขึ้นบรรทัดใหม่
```

### 8. อักขระพิเศษ (`08_special_characters.py`)
การใช้งานอักขระพิเศษและการ escape
```python
print("การใช้ \"quotes\" ในข้อความ")
print('She\'s a programmer')
print("Path: C:\\Python\\Scripts")
```

### 9. การจัดรูปแบบข้อความขั้นสูง (`09_string_formatting.py`)
การจัดรูปแบบข้อความขั้นสูงด้วยวิธีต่างๆ
```python
name = "John"
age = 30
# แบบเก่า %
print("My name is %s and I am %d years old." % (name, age))
# แบบ format()
print("My name is {n} and I am {a} years old.".format(n=name, a=age))
# แบบ f-string
print(f"My name is {name} and I am {age} years old.")
```

### 10. เมธอดของข้อความ (`10_string_methods.py`)
การใช้งานเมธอดต่างๆ ของ String
```python
text = "Hello, Python!"
print(text.upper())  # แปลงเป็นตัวพิมพ์ใหญ่
print(text.lower())  # แปลงเป็นตัวพิมพ์เล็ก
print(text.replace("Hello", "Hi"))  # แทนที่ข้อความ
```

### 11. การดำเนินการกับข้อความ (`11_string_operations.py`)
การดำเนินการพื้นฐานกับข้อความ
```python
# การต่อข้อความ
first = "Hello"
second = "World"
print(first + " " + second)

# การตัดข้อความ
text = "Python Programming"
print(text[0:6])  # ตัดคำว่า Python
print(text[-11:])  # ตัดคำว่า Programming
```