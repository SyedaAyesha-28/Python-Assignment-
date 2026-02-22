# Program: Number Pattern Printer

print("=== NUMBER PATTERN PRINTER ===")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

choice = int(input("Choose pattern (1-4): "))
height = int(input("Enter height: "))

print("\n")

# Pattern 1
if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2
elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3
elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
elif choice == 4:
    for i in range(1, height + 1):
        # Increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()

else:
    print("Invalid choice.")