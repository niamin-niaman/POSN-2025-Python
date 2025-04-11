"""
String Examples in Python
ตัวอย่างการใช้ตัวแปรประเภท String (ข้อความ)
"""

# ตัวอย่างการประกาศตัวแปร String
print("\n=== ตัวอย่างการประกาศตัวแปร String ===")
name = "สมชาย"
city = "เชียงใหม่"
slogan = 'ทำวันนี้ให้ดีที่สุด'

print("name =", name)
print("city =", city)
print("slogan =", slogan)

# ตัวอย่างการใช้ String แบบหลายบรรทัด
print("\n=== ตัวอย่างการใช้ String แบบหลายบรรทัด ===")
address = """123 ถนนสุขุมวิท
แขวงคลองเตย เขตคลองเตย
กรุงเทพมหานคร 10110"""

print("address =")
print(address)

# ตัวอย่างการต่อ String
print("\n=== ตัวอย่างการต่อ String ===")
first_name = "สมชาย"
last_name = "ใจดี"
full_name = first_name + " " + last_name

print("full_name =", full_name)

# ตัวอย่างการทำซ้ำ String
print("\n=== ตัวอย่างการทำซ้ำ String ===")
line = "-" * 20
print(line)

# ตัวอย่างการเข้าถึงตัวอักษร
print("\n=== ตัวอย่างการเข้าถึงตัวอักษร ===")
text = "Python"
print("ตัวอักษรตัวแรก:", text[0])
print("ตัวอักษรตัวสุดท้าย:", text[-1])
print("ตัวอักษร 3 ตัวแรก:", text[:3])
print("ตัวอักษร 3 ตัวหลัง:", text[-3:])

# ตัวอย่างการใช้เมธอดพื้นฐาน
print("\n=== ตัวอย่างการใช้เมธอดพื้นฐาน ===")
message = "  Hello, Python!  "
print("ความยาวข้อความ:", len(message))
print("แปลงเป็นตัวพิมพ์ใหญ่:", message.upper())
print("แปลงเป็นตัวพิมพ์เล็ก:", message.lower())
print("ลบช่องว่างหัวท้าย:", message.strip())
print("นับจำนวนตัวอักษร 'o':", message.count('o')) 