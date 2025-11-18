#Question 1
# Salary Calculator

# Input from user
salary = float(input("Enter your basic salary: "))
bonus = float(input("Enter your bonus amount: "))
tax_rate = float(input("Enter tax rate (in %): "))

# Calculations
gross = salary + bonus
tax = (tax_rate / 100) * gross
net = gross - tax

# Output
print("\n--- Salary Details ---")
print(f"Gross Salary : {gross:.2f}")

print(f"Tax Amount   : {tax:.2f}")
print(f"Net Salary   : {net:.2f}")


#QUESTION 2
# Login System with 3 Attempts

correct_username = "promise"
correct_password = "12345"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome back")
        break
    else:
        attempts -= 1
        print(f"Wrong credentials. Attempts left: {attempts}")

        if attempts == 0:
            print("Account locked")


#Question 3

# Student Grade Analyzer

# Input 4 scores
scores = []
for i in range(1, 5):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)

# Calculations
average = sum(scores) / 4
highest = max(scores)
lowest = min(scores)

# Grade determination
if 70 <= average <= 100:
    grade = "A"
elif 60 <= average <= 69:
    grade = "B"
elif 50 <= average <= 59:
    grade = "C"
else:
    grade = "F"

# Output
print("\n--- Student Grade Report ---")
print(f"Scores: {scores}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score : {lowest}")
print(f"Final Grade  : {grade}")


#Question 4
# ATM Withdrawal Simulation

balance = 5000

amount = float(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient funds")
elif amount <= 0:
    print("Invalid amount")
else:
    balance -= amount
    print(f"Withdrawal successful! New balance: {balance}")



#Question 5
# Membership Login

members = ("Favor", "Blessing", "Joy")
correct_password = "abc123"

name = input("Enter your name: ")
password = input("Enter your password: ")

if name in members and password == correct_password:
    print("Access granted")
elif name in members and password != correct_password:
    print("Password incorrect")
else:
    print("Not registered")



#Question 6
# Phone Network Checker

number = input("Enter phone number: ")

if number.startswith("070") or number.startswith("080"):
    print("MTN")
elif number.startswith("081"):
    print("Airtel")
elif number.startswith("090"):
    print("Glo")
else:
    print("Unknown network")



#Question 7
# Two-Number Comparison

# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare numbers
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal")

# Check if sum is even or odd
sum_value = num1 + num2

if sum_value % 2 == 0:
    print("The sum is even")
else:
    print("The sum is odd")


#Question 8
# Shopping Discount Program

# Input
price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))

# Calculate total cost
total = price * quantity

# Discount check
if total >= 20000:
    discount = 0.10 * total
else:
    discount = 0

# Final amount
final_amount = total - discount

# Output breakdown
print("\n--- Shopping Summary ---")
print(f"Price per item : {price}")
print(f"Quantity       : {quantity}")
print(f"Total cost     : {total}")
print(f"Discount       : {discount}")
print(f"Amount to pay  : {final_amount}")


#Question 9
# Bus Fare System

age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()

# Determine fare category
if student == "yes":
    print("Fare: Half price")
else:
    if age < 10:
        print("Fare: Free")
    elif 10 <= age <= 17:
        print("Fare: Half price")
    else:
        print("Fare: Full price")


#Question 10
# Electricity Bill Calculator

units = int(input("Enter units used: "))

# Determine rate
if 0 <= units <= 100:
    rate = 25
elif 101 <= units <= 200:
    rate = 35
else:
    rate = 45

# Calculate bill
bill = units * rate

# Output
print("\n--- Electricity Bill ---")
print(f"Units used : {units}")
print(f"Rate/unit  : ₦{rate}")
print(f"Total Bill : ₦{bill}")
