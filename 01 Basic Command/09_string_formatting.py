"""
ตัวอย่างการจัดรูปแบบข้อความ (String Formatting)
"""

# 1. การใช้ % operator (Old Style)
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))

# 2. การใช้ str.format() method
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# 3. การใช้ f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# 4. การจัดรูปแบบตัวเลข
pi = 3.14159
print("Pi value: {:.2f}".format(pi))  # แสดงทศนิยม 2 ตำแหน่ง
print(f"Pi value: {pi:.2f}")

# 5. การจัดรูปแบบเปอร์เซ็นต์
percentage = 0.75
print("Percentage: {:.0%}".format(percentage))  # แสดงเป็นเปอร์เซ็นต์
print(f"Percentage: {percentage:.0%}")

# 6. การจัดรูปแบบตัวเลขให้มีเครื่องหมายคั่นหลักพัน
number = 1000000
print("Number: {:,}".format(number))  # เพิ่มเครื่องหมายคั่นหลักพัน
print(f"Number: {number:,}")

# 7. การจัดรูปแบบตัวเลขให้มีเครื่องหมาย + หรือ -
positive = 42
negative = -42
print("Positive: {:+d}".format(positive))  # แสดงเครื่องหมาย +
print("Negative: {:+d}".format(negative))  # แสดงเครื่องหมาย -
print(f"Positive: {positive:+d}")
print(f"Negative: {negative:+d}")

# 8. การจัดรูปแบบตัวเลขให้มีเลขนำหน้า 0
number = 42
print("Number: {:05d}".format(number))  # เพิ่มเลข 0 นำหน้า
print(f"Number: {number:05d}")

# 9. การจัดรูปแบบข้อความให้ชิดซ้าย/ขวา/กึ่งกลาง
text = "Hello"
print("Left: {:<10}".format(text))  # ชิดซ้าย
print("Right: {:>10}".format(text))  # ชิดขวา
print("Center: {:^10}".format(text))  # กึ่งกลาง
print(f"Left: {text:<10}")
print(f"Right: {text:>10}")
print(f"Center: {text:^10}")

# 10. การใช้ f-string กับ expression
x = 10
y = 20
print(f"Sum: {x + y}")  # คำนวณผลรวม
print(f"Product: {x * y}")  # คำนวณผลคูณ

# 11. การใช้ f-string กับ function
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))

# 12. การใช้ f-string กับ conditional expression
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# 13. การใช้ f-string กับ dictionary
person = {"name": "John", "age": 30}
print(f"Name: {person['name']}, Age: {person['age']}")

# 14. การใช้ f-string กับ list
numbers = [1, 2, 3, 4, 5]
print(f"First number: {numbers[0]}, Last number: {numbers[-1]}")

# 15. การใช้ f-string กับ multiple lines
message = f"""
Name: {name}
Age: {age}
Status: {status}
"""
print(message) 