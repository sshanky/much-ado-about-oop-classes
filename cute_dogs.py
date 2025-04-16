# # The CuteDog class is our *base class* or *parent class*
# All other dog classes will inherit from this one,
# meaning they get its attributes and methods for free.
class CuteDog:

    # This is the constructor method.
    # It runs automatically when you create a new CuteDog instance.
    def __init__(self, name, color, size_lbs):
        # These are instance variables, unique to each dog object.
        self.name = name
        self.color = color
        self.size_lbs = size_lbs

    # A general method that all CuteDog instances will share.
    def speak(self):
        return f"{self.name} yips adorably. 🐾"

    # Another shared method that describes the dog’s appearance.
    def describe(self):
        return f"{self.name} is a {self.color} dog weighing {self.size_lbs}lbs."

# ------------------------------------------------------------------------------ #

# Fiona is a *child class* that inherits from CuteDog
# It gets all of CuteDog's methods, but can also add or override them
class Fiona(CuteDog):
    def __init__(self):
        # Here we call the parent constructor using `super()`
        # You can read about super() via python docs: https://docs.python.org/3.9/library/functions.html#super
        # Notice that I used 3.9 version of docs. Make sure to use the right docs for the version of python your using.

        # This allows us to set Fiona’s name, color, and size without rewriting all the logic
        super().__init__(name="Fiona", color="blondish, dyed like a tiger 🐯", size_lbs=10)

    # Fiona has a custom bark (overriding the speak method from CuteDog)
    def speak(self):
        return f"{self.name} gives you the tiniest, sweetest bark. She’s fierce... like a tiger! 🐅"

    # Fiona also has her own special method: cuddle
    def cuddle(self):
        return f"{self.name} is snuggling into your lap like the sweetheart she is. 💕"

# ------------------------------------------------------------------------------ #

# Ellie is another child class of CuteDog
class Ellie(CuteDog):
    def __init__(self):
        super().__init__(name="Ellie", color="jet black", size_lbs=8)

    # Ellie overrides speak to reflect her role as a therapy dog
    def speak(self):
        return f"{self.name} offers comforting gestures. Therapy mode activated. ✈️🐕‍🦺"

    # She has her own unique method too!
    def volunteer(self):
        return f"{self.name} is volunteering at the airport, giving travelers peace and tiny tail wags. 🧳"

# ------------------------------------------------------------------------------ #

# Jovie is a very special dog—he has inherited CuteDog traits and added his own chaotic energy
class Jovie(CuteDog):
    def __init__(self):
        super().__init__(name="Jovie", color="white and shaggy", size_lbs=20)

    # Jovie's speak is overridden with a fun, goofy description
    def speak(self):
        return f"{self.name} barks with buck-toothed confidence while doing a synchronized potty dance. 💩🐾"

    # Unique method describing Jovie’s... unique potty style
    def potty_style(self):
        return f"{self.name} pees and poops *at the same time*, right leg up. It's... majestic."