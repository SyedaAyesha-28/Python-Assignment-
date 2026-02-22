# Program: Age Calculator (Exact Date)


from datetime import datetime

# Taking full birth date input
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

# Create birth date object
birth_date = datetime(year, month, day)

# Get current date
current_date = datetime.now()

# Calculate difference
age_difference = current_date - birth_date

# Convert difference into values
age_years = age_difference.days // 365
age_months = age_years * 12
age_days = age_difference.days
age_hours = age_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Display results
print("\n----- Exact Age Details -----")
print("Current Age:", age_years, "years")
print("Age in Months:", age_months)
print("Age in Days:", age_days)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", years_to_100)