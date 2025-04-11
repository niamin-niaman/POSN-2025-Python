"""
ตัวอย่างการใช้ String Methods
"""

# 1. การแปลงตัวอักษร
text = "Hello, World!"
print("Original:", text)
print("Uppercase:", text.upper())  # แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด
print("Lowercase:", text.lower())  # แปลงเป็นตัวพิมพ์เล็กทั้งหมด
print("Capitalize:", text.capitalize())  # ตัวอักษรตัวแรกเป็นตัวพิมพ์ใหญ่
print("Title:", text.title())  # ตัวอักษรตัวแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่
print("Swapcase:", text.swapcase())  # สลับตัวพิมพ์ใหญ่และตัวพิมพ์เล็ก

# 2. การค้นหาและนับ
text = "Hello, Hello, Hello!"
print("Count 'Hello':", text.count("Hello"))  # นับจำนวนครั้งที่พบคำ
print("Find 'Hello':", text.find("Hello"))  # หาตำแหน่งแรกที่พบคำ
print("Find 'Hello' from index 6:", text.find("Hello", 6))  # หาตำแหน่งแรกที่พบคำหลังจาก index 6
print("RFind 'Hello':", text.rfind("Hello"))  # หาตำแหน่งสุดท้ายที่พบคำ
print("Index 'Hello':", text.index("Hello"))  # หาตำแหน่งแรกที่พบคำ (จะเกิด error ถ้าไม่พบ)
print("RIndex 'Hello':", text.rindex("Hello"))  # หาตำแหน่งสุดท้ายที่พบคำ (จะเกิด error ถ้าไม่พบ)

# 3. การตรวจสอบ
text = "Hello123"
print("Is Alpha:", text.isalpha())  # ตรวจสอบว่าเป็นตัวอักษรทั้งหมดหรือไม่
print("Is Alnum:", text.isalnum())  # ตรวจสอบว่าเป็นตัวอักษรหรือตัวเลขทั้งหมดหรือไม่
print("Is Digit:", text.isdigit())  # ตรวจสอบว่าเป็นตัวเลขทั้งหมดหรือไม่
print("Is Numeric:", text.isnumeric())  # ตรวจสอบว่าเป็นตัวเลขทั้งหมดหรือไม่
print("Is Decimal:", text.isdecimal())  # ตรวจสอบว่าเป็นตัวเลขทศนิยมทั้งหมดหรือไม่
print("Is Space:", text.isspace())  # ตรวจสอบว่าเป็นช่องว่างทั้งหมดหรือไม่
print("Is Title:", text.istitle())  # ตรวจสอบว่าเป็นรูปแบบ title หรือไม่
print("Is Upper:", text.isupper())  # ตรวจสอบว่าเป็นตัวพิมพ์ใหญ่ทั้งหมดหรือไม่
print("Is Lower:", text.islower())  # ตรวจสอบว่าเป็นตัวพิมพ์เล็กทั้งหมดหรือไม่

# 4. การแทนที่และลบ
text = "  Hello, World!  "
print("Original:", text)
print("Strip:", text.strip())  # ลบช่องว่างด้านหน้าและด้านหลัง
print("LStrip:", text.lstrip())  # ลบช่องว่างด้านซ้าย
print("RStrip:", text.rstrip())  # ลบช่องว่างด้านขวา
print("Replace 'Hello' with 'Hi':", text.replace("Hello", "Hi"))  # แทนที่คำ

# 5. การแบ่งและรวม
text = "Hello, World, Python"
print("Original:", text)
print("Split:", text.split(","))  # แบ่งข้อความเป็น list ตามเครื่องหมาย
print("Split with maxsplit=1:", text.split(",", 1))  # แบ่งข้อความเป็น list ตามเครื่องหมาย 1 ครั้ง
print("RSplit with maxsplit=1:", text.rsplit(",", 1))  # แบ่งข้อความเป็น list ตามเครื่องหมาย 1 ครั้งจากด้านขวา
print("Splitlines:", "Hello\nWorld\nPython".splitlines())  # แบ่งข้อความเป็น list ตามบรรทัดใหม่
print("Join:", "-".join(["Hello", "World", "Python"]))  # รวม list เป็นข้อความ

# 6. การจัดรูปแบบ
text = "Hello"
print("Original:", text)
print("Center:", text.center(10, "*"))  # จัดให้อยู่กึ่งกลาง
print("LJust:", text.ljust(10, "*"))  # จัดให้ชิดซ้าย
print("RJust:", text.rjust(10, "*"))  # จัดให้ชิดขวา
print("ZFill:", text.zfill(10))  # เติม 0 ด้านหน้า

# 7. การเข้ารหัสและถอดรหัส
text = "Hello, 世界"
print("Original:", text)
print("Encode UTF-8:", text.encode("utf-8"))  # เข้ารหัสเป็น bytes
print("Decode UTF-8:", text.encode("utf-8").decode("utf-8"))  # ถอดรหัสจาก bytes

# 8. การใช้ partition และ rpartition
text = "Hello, World, Python"
print("Original:", text)
print("Partition:", text.partition(","))  # แบ่งข้อความเป็น tuple 3 ส่วน
print("RPartition:", text.rpartition(","))  # แบ่งข้อความเป็น tuple 3 ส่วนจากด้านขวา

# 9. การใช้ expandtabs
text = "Hello\tWorld\tPython"
print("Original:", text)
print("Expandtabs:", text.expandtabs(4))  # แทนที่ tab ด้วยช่องว่าง 4 ตัว

# 10. การใช้ maketrans และ translate
text = "Hello, World!"
trans = str.maketrans("o", "0")  # สร้างตารางการแปลง
print("Original:", text)
print("Translate:", text.translate(trans))  # แปลงตัวอักษรตามตาราง 