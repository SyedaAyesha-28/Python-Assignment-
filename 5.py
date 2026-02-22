# Program: Bill Splitter

# Taking input from user
total_bill = float(input("Enter total bill: "))
num_people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

# Calculations
subtotal = total_bill

tax_amount = (tax_percent / 100) * subtotal
bill_after_tax = subtotal + tax_amount

tip_amount = (tip_percent / 100) * bill_after_tax
total_amount = bill_after_tax + tip_amount

amount_per_person = total_amount / num_people

# Display results
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal:     ₹{subtotal:.2f}")
print(f"Tax ({tax_percent}%):   ₹{tax_amount:.2f}")
print(f"After tax:    ₹{bill_after_tax:.2f}")
print(f"Tip ({tip_percent}%):   ₹{tip_amount:.2f}")
print(f"Total:        ₹{total_amount:.2f}")
print(f"Per person:   ₹{amount_per_person:.2f}")