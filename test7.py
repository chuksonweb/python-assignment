#Python Operators
print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1,sum2,sum3)

#Python Arithmetic Operators
#Here is an example using different arithmetic operators:
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Division in Python
#Python has two division operators:
#/ - Division (returns a float)
#// - Floor division (returns an integer)

x = 12
y = 5
print(x / y)
print(x // y)

#Python Assignment Operators
#Assignment operators are used to assign values to variables:
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)


x = 5
x%=3
print(x)

x = 5
x//=3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)


x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)

print(x := 3)

#The Walrus Operator
#ython 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 4:
    print(f"List has {count} elements")

    #Python Comparison Operators
    #Comparison operators return True or False based on the comparison:
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(6 < x < 10)
print(1 < x and x < 10)

#Python Logical Operators
#Logical operators are used to combine conditional statements:
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

#Difference Between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Python Membership Operators
#Membership operators are used to test if a sequence is presented in an object:

#Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#Membership in Strings
#The membership operators also work with strings:
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:
#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(6 & 3)

#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3)

#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)

#Python Operator Precedence
#Operator precedence describes the order in which operations are performed.
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

print(100 + 5 * 3)

#Left-to-Right Evaluation
#If two operators have the same precedence, the expression is evaluated from left to right.

#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

#Precedence Order
#The precedence order is described in the table below, starting with the highest precedence at the top:
print((6 + 3) - (6 + 3))
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 - 3 ** 3)

"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""

print(100 + ~3)

"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print(100 - 5 * 3)

"""
Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
The calculation above reads 100 - 15 = 85
"""

print(8 >> 4 - 2)

"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(6 & 2 + 1)

"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2

More explanation:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 2 + 1)

"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5

More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 2 + 1)

"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7

More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(5 == 4 + 1)

"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""

print(not 5 == 5)

"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""

print(1 or 2 and 3)

"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""

print(4 or 5 + 10 or 8)

"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""

