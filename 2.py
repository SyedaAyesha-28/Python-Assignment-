# Simple Calculator in Python
# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")

# Addition
addition = num1 + num2
print(f"{num1} + {num2} = {addition}")

# Subtraction
subtraction = num1 - num2
print(f"{num1} - {num2} = {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"{num1} * {num2} = {multiplication}")

# Division
if num2 != 0:
    division = num1 / num2
    print(f"{num1} / {num2} = {round(division, 2)}")
else:
    print("Division by zero is not allowed")

# Modulus
if num2 != 0:
    modulus = num1 % num2
    print(f"{num1} % {num2} = {modulus}")
else:
    print("Modulus by zero is not allowed")

# Exponentiation
exponent = num1 ** num2
print(f"{num1} ^ {num2} = {exponent}")