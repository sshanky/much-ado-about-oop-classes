# We’re importing the CuteDog class from another file called 'cute_dog.py'.
# This lets us reuse the CuteDog blueprint here without rewriting it.
# Think of it like borrowing a recipe from a cookbook you wrote earlier.
# Now we can make as many CuteDog objects as we want in this file!
from cute_dog import CuteDog

# Part 1: Understanding That Everything is an Object
# Even primitive types like: int, str, list are objects

# In python, every value is actually *an instance of a class*, even something a simple as a number
the_coolest_number = 42
print("What type is the_coolest_number ? ", type(the_coolest_number))  # <class 'int'>

# As a python type int - it means that it comes with a bunch of built in methods()
# For example, intergers apparently have a method called, `.bit_length()`
# read about it here: https://docs.python.org/3/library/stdtypes.html#int.bit_length
# bit_length(): Returns the number of bits necessary to represent an integer in binary, 
# excluding the sign and leading zeros
print("What's the bit length of 42 (int)? ", the_coolest_number.bit_length()) # Expect: 6

# Since 42, is an int. (integer) In order to get length - I needed to convert it to a string first.
# Here, the_coolest_number is an object of class int. In order to obtain length of this int. I must convert
# it to a string, so that I can use the string method .len()
print("What's the length of the_coolest_number as a string: ", len(str(the_coolest_number))) # Objects have methods! # expect: 2

# — so clearly, it's not just a raw number, it's a full object with behaviors.
# Read about python ints[here](https://docs.python.org/3/library/functions.html#int)
# Read about python .len() method on a strings [here](https://docs.python.org/3/library/functions.html#len)

# Same goes for strings:
greeting = "hello"
print(type(greeting)) # <class 'str'>
print(greeting.upper()) # Returns "HELLO"
print(greeting.startswith("h")) # returns True

# Part 2: User-defined objects are just like built-in ones
## When you create a class like CuteDog, you're making your own data type — just like int or str.

olivia = CuteDog("Olivia", "albino tiger light", 17)
print("What type is the variable Olivia? ", type(olivia)) # <class 'cute_dogs.CuteDog'>
print("olvia.describe() ", olivia.describe()) # Olivia is a albino tiger light dog weighing 17lbs
print("olivia.speak() ", olivia.speak()) # Olivia yips adorably. 🐾

# So our Olivia object is a real Python object — just like a string or number.

def everything_is_an_object_demo():
    examples = [
        42,                    # Integer
        "coffee",              # String
        [1, 2, 3],             # List
        {"a": 1},              # Dict
        lambda x: x + 1,       # Function (yes, functions are objects!)
        CuteDog("Pepper", "curly gray hair", 9)  # Another custom CuteDog Object
    ]

    for item in examples:
        print(f"Type: {type(item)} | Is object? {'Yes' if isinstance(item, object) else 'No'}")
        print(f"  Can I call methods? Example: {dir(item)[:3]}...\n")  # Show just a few methods

print("---Print the results of running everything_is_an_object_demo()----")
everything_is_an_object_demo()