# This is the *parent* cute dog class 
class CuteDog:
    def __init__(self, name, color, size_lbs):
        self.name = name
        self.color = color
        self.size_lbs = size_lbs

    def speak(self):
        return f"{self.name} yips adorably. 🐾"

    def describe(self):
        return f"{self.name} is a {self.color} dog weighing {self.size_lbs}lbs."

class Fiona(CuteDog):
    def __init__(self):
        super().__init__(name="Fiona", color="blondish, dyed like a tiger 🐯", size_lbs=10)

    def speak(self):
        return f"{self.name} gives you the tiniest, sweetest bark. She’s fierce... like a tiger! 🐅"

    def cuddle(self):
        return f"{self.name} is snuggling into your lap like the sweetheart she is. 💕"
    
class Ellie(CuteDog):
    def __init__(self):
        super().__init__(name="Ellie", color="jet black", size_lbs=8)

    def speak(self):
        return f"{self.name} offers comforting eye contact. Therapy mode activated. ✈️🐕‍🦺"

    def volunteer(self):
        return f"{self.name} is volunteering at the airport, giving travelers peace and tiny tail wags. 🧳"
    
class Jovie(CuteDog):
    def __init__(self):
        super().__init__(name="Jovie", color="unknown (but full of chaotic love)", size_lbs=12)

    def speak(self):
        return f"{self.name} barks with buck-toothed confidence while doing a synchronized potty dance. 💩🐾"

    def potty_style(self):
        return f"{self.name} pees and poops *at the same time*, right leg up. It's... majestic."