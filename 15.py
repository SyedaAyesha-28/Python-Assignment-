# Program: Prime Number Checker

# Part 1: Single Number

number = int(input("Enter a number: "))

if number < 2:
    print(number, "is NOT a prime number.")
elif number == 2:
    print("2 is a PRIME number.")
else:
    is_prime = True
    
    # Check divisibility from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, "is a PRIME number.")
    else:
        print(number, "is NOT a prime number.")


# Part 2: Prime Numbers in Range

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start, end + 1):
    if num >= 2:
        is_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=", ")