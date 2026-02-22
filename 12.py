# Program: Multiplication Table Generator


# Taking input
number = int(input("Enter number: "))
end_range = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

# Loop to generate table
for i in range(1, end_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")