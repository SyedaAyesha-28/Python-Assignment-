# Program: Grade Calculator

# Taking marks input from user
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Display marks
print("\nMarks Entered:")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = (total / 500) * 100

# Determine Grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Determine Pass/Fail
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

# Display Results
print("\n----- Final Result -----")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)