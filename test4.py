# print(thislist[-1])
motors = ["Lexus", "Toyota", "Camry", "Benz"]
motors[0]  = "GLK"
motors[2]  = "Lexus"
print(motors)



motors = ["Lexus", "Toyota", "Camry", "Benz"]
motors.sort()
print(motors)


motors = ["Lexus", "Toyota", "Camry", "Benz"]
motors.sort(reverse=True)
print(motors)

thislist = ["apple", "banana", "cherry"]
print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

motors = ["Lexus", "Toyota", "Camry", "Benz"]
print(motors[3])

motors = []
motors.append("Lexus")
motors.append("Toyota")
motors.append("Camry")
motors.append("Benz")
motors.append("Matrix")
motors.append("Honda")
print(motors)



fruits = ["apple", "apple", "banana", "cherry"]
fruits.remove("apple")
fruits.remove("apple")
print(fruits)

fruits = ["apple", "apple", "banana", "cherry"]
fruits.pop(3)
fruits.remove("apple")
print(fruits)


