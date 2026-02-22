# Ask user how many numbers they want to enter
count = int(input("How many numbers? "))

total_sum = 0          # To store sum
maximum = None         # To store maximum value
minimum = None         # To store minimum value

# Loop to take input numbers
for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    
    # Add number to total sum
    total_sum += number
    
    # Set first number as initial max and min
    if i == 1:
        maximum = number
        minimum = number
    else:
        # Check for maximum
        if number > maximum:
            maximum = number
        
        # Check for minimum
        if number < minimum:
            minimum = number

# Calculate average
average = total_sum / count

# Display results
print("\nResults:")
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)