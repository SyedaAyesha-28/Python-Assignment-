# Program: Calculator Using Functions

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b

# Function for modulus
def modulus(a, b):
    return a % b

# Function for power
def power(a, b):
    return a ** b


# Main calculator function
def calculator():
    while True:
        print("\n=== SIMPLE CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator...")
            break

        # Take numbers input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Call appropriate function
        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        elif choice == "5":
            print("Result:", modulus(num1, num2))

        elif choice == "6":
            print("Result:", power(num1, num2))

        else:
            print("Invalid choice. Please select 1-7.")


# Run the calculator
calculator()