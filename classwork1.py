print("hello world")

class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# print(obj.__private_var)   # ✗ AttributeError
print(obj.show_private())    # ✓ Access through method

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print("The number you have entered for a is ", a)
print("The number you have entered for b is ", b)


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

# Direct access will fail
try:
    account.__balance += 500  # ✗ AttributeError
except AttributeError:
    print("Direct access to private variable failed!!!")

# Access using methods
print("Your account balance is: ", account.get_balance())   # ✓ 1000

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())  # ✓ 1500


# Program to calculate the average of 4 numbers

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Calculating the average
average = (num1 + num2 + num3 + num4) / 4

# Displaying the result
print("The average of the four numbers is:", average)
