# ------------------------------------
# Program: Leap Year Checker
# ------------------------------------

# Taking year input
year = int(input("Enter a year: "))

# Check leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"\n{year} is a Leap Year.")
    
    # Explain the reason
    if year % 400 == 0:
        print("Reason: It is divisible by 400.")
    elif year % 100 == 0:
        print("Reason: It is divisible by 100 but not by 400.")
    else:
        print("Reason: It is divisible by 4 but not by 100.")
else:
    print(f"\n{year} is NOT a Leap Year.")
    
    # Explain why not
    if year % 4 != 0:
        print("Reason: It is not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: It is divisible by 100 but not by 400.")