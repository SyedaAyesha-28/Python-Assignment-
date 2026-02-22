# Program: Movie Ticket Pricing System


# Taking input
age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Number of tickets: "))

# Determine base price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Calculate total base amount
total_base = base_price * tickets

# Check for weekend discount
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * total_base
else:
    discount = 0

# Final amount after discount
final_amount = total_base - discount

# Display results
print("\n=== TICKET BILL ===")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Total before discount: ₹", total_base)
print("Discount: ₹", round(discount, 2))
print("Final Amount: ₹", round(final_amount, 2))