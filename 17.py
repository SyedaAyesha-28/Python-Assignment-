# ------------------------------------
# Program: Palindrome Checker
# ------------------------------------

# Taking input
user_input = input("Enter word/number: ")

# Store original value
original = user_input

# Convert to lowercase (to ignore case difference)
processed = user_input.lower()

# Reverse the processed string
reversed_value = processed[::-1]

# Display step-by-step
print("\nOriginal:", original)
print("Reversed:", original[::-1])

# Check palindrome
if processed == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")