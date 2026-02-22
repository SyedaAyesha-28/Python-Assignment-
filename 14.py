# ------------------------------------
# Program: Factorial Calculator
# ------------------------------------

# Taking input
number = int(input("Enter a number: "))

# Check for negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

# Factorial of 0 is 1
elif number == 0:
    print("0! = 1")

else:
    factorial = 1
    steps = ""   # To store step-by-step calculation
    
    # Loop from number down to 1
    for i in range(number, 0, -1):
        factorial *= i
        steps += str(i)
        
        if i != 1:
            steps += " × "
    
    # Display result
    print(f"{number}! = {steps} = {factorial}")