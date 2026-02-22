# Program: Simple Bio Card


# Storing personal details in variables
name = "Syeda Ayesha"
age = "20"
course = "Python Programming"
college = "Navodaya Institute of Technology"
hobby = "Traveling, Sports"
gmail = "ay3shaa28@gmail.com"
portfolio = "syedaayesha-28.github.io/Portfolio"

# Printing the formatted bio card
print("\n" + "╔" + "═"*60 + "╗")
print("║                 MY BIO CARD                 ║")
print("╠" + "═"*60 + "╣")

print(f"║  Name      : {name:<42}║")
print(f"║  Age       : {age:<42}║")
print(f"║  Course    : {course:<42}║")
print(f"║  College   : {college:<42}║")
print(f"║  Hobby     : {hobby:<42}║")
print(f"║  Gmail     : {gmail:<42}║")
print(f"║  Portfolio : {portfolio:<42}║")

print("╚" + "═"*60 + "╝")