b = "Hello, World!"
print(b[2:5])
print(b.upper())
print(b.lower())

a = " Hello, World! "
print(a.strip()) 
print(a.replace ("H", "J"))



a = "Hello"
b = "World"
c = a + " " + "" + b
print(c) 

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."

print( "Hellow\rWorld")

text = "hello world"
result = text.capitalize()
print(result)

text = "HELLOW WORLD"
result = text.casefold()
print(result)


text = "hello"
result = text.center(10)
print(result)

text = "banana"
result = text.count("a")
print(result)

text = "Hello World"
encoded = text.encode()
print(encoded)

text = "hello world"
print(text.endswith("world"))


text = "A\tB\tC"
print(text)
print(text.expandtabs())


text = "Hello, world!"
index = text.find("world")
print(index)


text = "Hello, {}!"
print(text.format("Alice"))


person = {'name': 'Alice', 'age': 25}
text = "My name is {name} and I am {age} years old."
print(text.format_map(person))

text = "Hello, world!"
print(text.index("world"))


text = "Python123"
print(text.isalnum())


text = "Python!"
print(text.isalpha())


txt = "Company10"

x = txt.isalpha()

print(x)

txt = "Company123"

x = txt.isascii()

print(x)


txt = "1234"

x = txt.isdecimal()

print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

txt = "50800"

x = txt.isdigit()

print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

txt = "Demo"

x = txt.isidentifier()

print(x)


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())


txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)


txt = "50"

x = txt.zfill(10)

print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))