class MoreComplexCoffeeMachine:
    def __init__(
            self,
            beans=20, 
            water=150,
            item_name="BrewMaster Pro",
            make="CafeCraft",
            model="CC-2025",
            category="expresso machine"
    ):
        self.beans = beans
        self.water = water 
        self.cups_made = 0
        
        self.item_name = item_name
        self.make = make
        self.model = model
        self.category = category

        # Interpolation 
        print(f"☕ {self.item_name} ({self.make} {self.model}) is now online and ready to brew!")

