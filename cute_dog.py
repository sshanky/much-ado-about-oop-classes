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
    
# ------------------------------------------------------------------------------ #
# 🐶 LET’S MEET OUR DOGGY CAST!
# This section will help you understand how we *instantiate* each class (i.e., make actual dog objects from them)
# Just uncomment lines as you go to explore step by step!

# 🐾 Fiona is a class that INHERITS from CuteDog.
# When you create an instance of Fiona, you're calling her custom constructor
# which uses `super()` to fill in name, color, and size from the parent class.

# We're creating a Fiona object from the Fiona class
# fiona = Fiona()

# Let Fiona speak
# print(fiona.speak())       # Should say: Fiona gives you the tiniest, sweetest bark...

# Fiona has a special cuddle method!
# This is a method that ONLY exists in the Fiona class
# print(fiona.cuddle())      # Should say: Fiona is snuggling into your lap...

# Fiona also uses a shared method from the CuteDog class
# print(fiona.describe())    # Should describe her color and weight

# ------------------------------------------------------------------------------ #
# 🐾 Ellie is also a subclass of CuteDog.
# She overrides the speak method with her own gentle version, and adds her own method: volunteer().
# --- Ellie: the therapy pro 🐕‍🦺 ---

# Create an instance of Ellie
# ellie = Ellie()

# Ellie has a calm, comforting bark
# print(ellie.speak())       # Should say: Ellie offers comforting gestures...

# Ellie volunteers at the airport 🧳
# print(ellie.volunteer())   # Should say: Ellie is volunteering...

# Shared method from CuteDog
# print(ellie.describe())    # Should describe her color and weight

# ------------------------------------------------------------------------------ #
# 🐾 Jovie is a wild child — another subclass of CuteDog with chaos energy.
# He overrides speak and adds his own special method, potty_style().

# Create an instance of Jovie
# jovie = Jovie()

# Jovie’s speak method is wild and hilarious
# print(jovie.speak())       # Should say: Jovie barks with buck-toothed confidence...

# Jovie has a *very special* potty style
# print(jovie.potty_style()) # Should say: Jovie pees and poops *at the same time*...

# You guessed it—he can describe himself too
# print(jovie.describe())    # Should describe his color and weight

# ------------------------------------------------------------------------------ #

# 🧠 BONUS TIPS:
# - Try calling other methods that *aren’t* defined in the child class to see what’s inherited.
# - Can you guess what would happen if you removed or changed one of the `speak()` methods?
# - Or create your own dog class below using `class MyDog(CuteDog):`