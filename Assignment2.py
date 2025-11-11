# PYTHON ASSIGNMENT
# Topic: Strings and Their Operations
# Instructor: CHIOKE PROMISE CHICHETARAM

# Section A – String Basics (question 1)

word1 = 'Hello'  
word2 = "Welcome"  
word3 = """to Python class"""  
print(word1, word2, word3)


# Section A – String Basics (Question 2)

sentence = "Python is fun to learn!"
print(sentence)

# Section A – String Basics (Question 3)

message = """Python is powerful.
It is easy to learn.
It is loved by developers."""
print(message)


# Section B – Strings as Arrays (Question 4)

text = "PYTHON"

print("First character:", text[0])
print("Third character:", text[2])
print("Last character:", text[5])


# Section B – Strings as Arrays (Question 5)

language = "Python"
for letter in language:
    print(letter)


    # Section C – String Length and Checking (Question 6)

fruit = "Banana"
length = len(fruit)
print("The length of the word 'Banana' is:", length)



# Section C – String Length and Checking (Question 7)

word = "Learning Python is cool"
if "Python" in word:
    print("Yes, 'Python' is found!")
else:
    print("No, 'Python' is not found.")



# Section C – String Length and Checking (Question 8)

word = "Learning Python is cool"
if "Java" not in word:
    print("'Java' is not found in the sentence.")
else:
    print("'Java' is found in the sentence.")




# Question 9 – Bonus Task

message = "Coding is fun"
count = 0
for char in message:
    if char == "n":
        count += 1
print("The letter 'n' appears", count, "times in the message.")




# Question 10 – Multiline String and Uppercase

poem = """I like Python because it is simple.
It helps me solve problems quickly.
Learning Python makes coding enjoyable."""
print(poem.upper())