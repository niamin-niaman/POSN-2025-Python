"""
ตัวอย่างการใช้ String Operations
"""

# 1. การต่อสตริง (String Concatenation)
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)  # Hello World

# 2. การทำซ้ำสตริง (String Repetition)
str1 = "Ha"
result = str1 * 3
print("Repetition:", result)  # HaHaHa

# 3. การเข้าถึงตัวอักษร (String Indexing)
text = "Hello, World!"
print("First character:", text[0])  # H
print("Last character:", text[-1])  # !
print("Second to last character:", text[-2])  # d

# 4. การตัดสตริง (String Slicing)
text = "Hello, World!"
print("First 5 characters:", text[:5])  # Hello
print("Characters from index 7 to end:", text[7:])  # World!
print("Characters from index 7 to 12:", text[7:12])  # World
print("Every second character:", text[::2])  # Hlo ol!
print("Reverse string:", text[::-1])  # !dlroW ,olleH

# 5. การใช้ in operator
text = "Hello, World!"
print("'World' in text:", "World" in text)  # True
print("'Python' in text:", "Python" in text)  # False

# 6. การใช้ len function
text = "Hello, World!"
print("Length of string:", len(text))  # 13

# 7. การใช้ min และ max functions
text = "Hello, World!"
print("Minimum character:", min(text))  # Space
print("Maximum character:", max(text))  # r

# 8. การใช้ sorted function
text = "Hello, World!"
print("Sorted characters:", sorted(text))  # [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'o', 'o', 'r']

# 9. การใช้ enumerate function
text = "Hello"
for index, character in enumerate(text):
    print(f"Index {index}: {character}")

# 10. การใช้ zip function
text1 = "Hello"
text2 = "World"
for char1, char2 in zip(text1, text2):
    print(f"{char1} - {char2}")

# 11. การใช้ format method
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # My name is John and I am 30 years old.
print("My name is {0} and I am {1} years old.".format(name, age))  # My name is John and I am 30 years old.
print("My name is {n} and I am {a} years old.".format(n=name, a=age))  # My name is John and I am 30 years old.

# 12. การใช้ f-strings (Python 3.6+)
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")  # My name is John and I am 30 years old.
print(f"My name is {name.upper()} and I am {age} years old.")  # My name is JOHN and I am 30 years old.
print(f"My name is {len(name)} characters long.")  # My name is 4 characters long.

# 13. การใช้ % operator (old-style string formatting)
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))  # My name is John and I am 30 years old.
print("My name is %(name)s and I am %(age)d years old." % {"name": name, "age": age})  # My name is John and I am 30 years old.

# 14. การใช้ raw strings
print(r"This is a raw string\nwith a newline character")  # This is a raw string\nwith a newline character

# 15. การใช้ triple quotes
text = """This is a multi-line
string that can span
multiple lines."""
print(text)

# 16. การใช้ string methods
text = "  Hello, World!  "
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Strip:", text.strip())
print("Replace:", text.replace("Hello", "Hi"))

# 17. การใช้ string constants
import string
print("ASCII letters:", string.ascii_letters)
print("ASCII lowercase:", string.ascii_lowercase)
print("ASCII uppercase:", string.ascii_uppercase)
print("Digits:", string.digits)
print("Hex digits:", string.hexdigits)
print("Oct digits:", string.octdigits)
print("Punctuation:", string.punctuation)
print("Whitespace:", string.whitespace)
print("Printable:", string.printable)

# 18. การใช้ string module functions
import string
text = "Hello, World!"
print("Capwords:", string.capwords(text))  # Hello, World!
print("Template:", string.Template("$name is $age years old").substitute(name="John", age=30))  # John is 30 years old

# 19. การใช้ string methods with arguments
text = "Hello, World!"
print("Count 'l':", text.count("l"))  # 3
print("Count 'l' from index 3:", text.count("l", 3))  # 2
print("Count 'l' from index 3 to 7:", text.count("l", 3, 7))  # 1
print("Find 'o':", text.find("o"))  # 4
print("Find 'o' from index 5:", text.find("o", 5))  # 7
print("Find 'o' from index 5 to 10:", text.find("o", 5, 10))  # 7
print("Index 'o':", text.index("o"))  # 4
print("Index 'o' from index 5:", text.index("o", 5))  # 7
print("Index 'o' from index 5 to 10:", text.index("o", 5, 10))  # 7

# 20. การใช้ string methods with regular expressions
import re
text = "Hello, World!"
print("Match 'Hello':", re.match("Hello", text))  # <re.Match object; span=(0, 5), match='Hello'>
print("Search 'World':", re.search("World", text))  # <re.Match object; span=(7, 12), match='World'>
print("Findall 'l':", re.findall("l", text))  # ['l', 'l', 'l']
print("Split ', ':",
      re.split(", ", text))  # ['Hello', 'World!']
print("Sub 'Hello' with 'Hi':", re.sub("Hello", "Hi", text))  # Hi, World! 