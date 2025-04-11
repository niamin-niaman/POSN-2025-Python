# Division (/) Examples

# Basic division with integers
num1 = 10
num2 = 5
result = num1 / num2
print(f"Basic division: {num1} / {num2} = {result}")  # Output: 2.0

# Division with decimals
decimal1 = 7.5
decimal2 = 2.5
result_decimal = decimal1 / decimal2
print(f"Decimal division: {decimal1} / {decimal2} = {result_decimal}")  # Output: 3.0

# Division with negative numbers
negative = -10
positive = 2
result_negative = negative / positive
print(f"Negative division: {negative} / {positive} = {result_negative}")  # Output: -5.0

# Division that results in decimal
a = 5
b = 2
result_decimal = a / b
print(f"Non-exact division: {a} / {b} = {result_decimal}")  # Output: 2.5

# Division by zero (will raise an error)
try:
    result_error = 10 / 0
    print("This won't be printed")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed") 