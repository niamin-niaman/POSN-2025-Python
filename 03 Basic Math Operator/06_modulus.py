# Modulus (%) Examples

# Basic modulus
num1 = 10
num2 = 3
result = num1 % num2
print(f"Basic modulus: {num1} % {num2} = {result}")  # Output: 1

# Modulus with larger numbers
dividend = 17
divisor = 5
result_large = dividend % divisor
print(f"Larger numbers: {dividend} % {divisor} = {result_large}")  # Output: 2

# Modulus with negative numbers
negative = -10
positive = 3
result_negative = negative % positive
print(f"Negative dividend: {negative} % {positive} = {result_negative}")  # Output: 2

# Common use case: checking even/odd
number = 7
is_even = number % 2 == 0
print(f"Is {number} even? {is_even}")  # Output: False

# Modulus for time (hours on 12-hour clock)
hours = 25
hours_on_clock = hours % 12
print(f"{hours} hours on 12-hour clock = {hours_on_clock}")  # Output: 1 