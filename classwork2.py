# List Methods
# Append 
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)


#Python List clear() Method
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#Python List copy() Method
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(x)


#Python List count() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#Python List extend() Method
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

#Python List index() Method
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#Python List insert() Metho
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#Python List pop() Method
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Python List remove() Method
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#Python List reverse() Method
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#Python List sort() Method
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)