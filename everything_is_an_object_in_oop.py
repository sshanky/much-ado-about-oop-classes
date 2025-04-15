from coffee_machine import CoffeeMachine

# Part 1: Understanding That Everything is an Object
# Even primitive types like: int, str, list are objects

# In python, every value is actually *an instance of a class*, even something a simple as number
the_coolest_number = 42
print("What type is the_coolest_number ? ", type(the_coolest_number))  # <class 'int'>
print("what's the length of the the_coolest_number: ", the_coolest_number.lenthg()) # Objects have methods! 
# This returns how many bits needed to represent 42 (expect: 2)
# Here, the_coolest_number is an object of class int, and it has methods like .bit_length() 
# — so clearly, it's not just a raw number, it's a full object with behaviors.

# Same goes for strings:
greeting = "hello"
print(type(greeting)) # <class 'str'>
print(greeting.upper()) # Returns "HELLO"
print(greeting.startswith("h")) # returns True

# Part 2: User-defined objects are just like built-in ones
## When you create a class like CoffeeMachine, you're making your own data type — just like int or str.

gaggia = CoffeeMachine("Gaggia", "Classic Evo Pro", (500, 600))
print(type(gaggia))  # <class '__main__.EspressoMachine'>
print(gaggia.describe())  # Custom method we created
# So your gaggia object is a real Python object — just like a string or number.