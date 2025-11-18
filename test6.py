# create a tuple of 5 favorite foods
foods = ("Beans", "Rice", "Eba", "Fufu", "Stew")

# print the first, middle, and last items
print("First food:", foods[0])
print("Middle food:", foods[len(foods)//2])
print("Last food:", foods[-1])

# convert tuple to a list
foods_list = list(foods)

# change one food (example: change "tacos" to "burger")
foods_list[2] = "Yam"

# convert back to a tuple
updated_foods = tuple(foods_list)

print("Updated tuple:", updated_foods)
