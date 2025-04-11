"""
Dictionary Examples in Python
ตัวอย่างการใช้ตัวแปรประเภท Dictionary (พจนานุกรม)
"""

# ตัวอย่างการประกาศตัวแปร Dictionary
print("\n=== ตัวอย่างการประกาศตัวแปร Dictionary ===")
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

print("car =", car)
print("student =", student)
print("menu =", menu)

# ตัวอย่างการเข้าถึงข้อมูลใน Dictionary
print("\n=== ตัวอย่างการเข้าถึงข้อมูลใน Dictionary ===")
print("car['brand'] =", car['brand'])
print("student['name'] =", student['name'])
print("student['grades']['math'] =", student['grades']['math'])
print("menu['อาหาร'] =", menu['อาหาร'])

# ตัวอย่างการเพิ่มและแก้ไขข้อมูล
print("\n=== ตัวอย่างการเพิ่มและแก้ไขข้อมูล ===")
person = {
    "name": "สมชาย",
    "age": 25
}
print("Dictionary ก่อนแก้ไข:", person)

person["city"] = "กรุงเทพ"    # เพิ่มข้อมูลใหม่
print("หลังเพิ่ม city:", person)

person["age"] = 26           # แก้ไขข้อมูลที่มีอยู่
print("หลังแก้ไข age:", person)

# ตัวอย่างการลบข้อมูล
print("\n=== ตัวอย่างการลบข้อมูล ===")
print("Dictionary ก่อนลบ:", person)

del person["age"]            # ลบข้อมูลที่ต้องการ
print("หลังลบ age:", person)

# ตัวอย่างการตรวจสอบข้อมูล
print("\n=== ตัวอย่างการตรวจสอบข้อมูล ===")
print("มี name:", "name" in person)
print("มี phone:", "phone" in person)

# ตัวอย่างการดึงข้อมูลทั้งหมด
print("\n=== ตัวอย่างการดึงข้อมูลทั้งหมด ===")
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# ตัวอย่าง Dictionary ซ้อน Dictionary
print("\n=== ตัวอย่าง Dictionary ซ้อน Dictionary ===")
company = {
    "name": "Tech Corp",
    "departments": {
        "IT": {
            "head": "John",
            "employees": 10
        },
        "HR": {
            "head": "Mary",
            "employees": 5
        }
    }
}

print("Company Name:", company["name"])
print("IT Department Head:", company["departments"]["IT"]["head"])
print("HR Department Employees:", company["departments"]["HR"]["employees"]) 