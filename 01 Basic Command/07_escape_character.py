"""
ตัวอย่างการใช้ Escape Character
"""

# \n - ขึ้นบรรทัดใหม่
print("บรรทัดที่ 1\nบรรทัดที่ 2")

# \t - Tab
print("คอลัมน์1\tคอลัมน์2\tคอลัมน์3")

# \\ - แสดงเครื่องหมาย \
print("เส้นทาง: C:\\Users\\Documents")

# \" - แสดงเครื่องหมาย "
print('เขาพูดว่า "สวัสดี"')

# \' - แสดงเครื่องหมาย '
print("It's a beautiful day")

# \r - กลับไปต้นบรรทัด
print("Loading...\rDone!")

# \b - Backspace
print("Hello\bWorld")  # จะแสดงเป็น HellWorld

# \a - Bell sound (อาจไม่ทำงานในบาง terminal)
print("\a")

# Raw string (r prefix)
print(r"C:\new\text.txt")  # จะแสดง \n และ \t ตามปกติ

# ตัวอย่างการใช้งานหลาย escape character
print("ชื่อ:\tJohn\nนามสกุล:\tDoe\nอายุ:\t25") 