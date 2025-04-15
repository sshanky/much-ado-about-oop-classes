class CoffeeMachine:
    def __init__(self, beans=10, water=100):
        self.beans = beans
        self.water = water
        self.cups_made = 0
        print("Beep boop! CoffeeMachine is now online and ready to caffeinate.")

    def status(self):
            print(f"Beans: {self.beans}, Water: {self.water}ml, Cups made: {self.cups_made}")

    def make_coffee(self, style="espresso"):
        if self.beans < 1 or self.water < 20:
            print("ERROR: Insufficient resources! Try feeding me more beans and water, human.")
            return

        print(f"Brewing a nice cup of {style}...")
        self.beans -= 1
        self.water -= 20
        self.cups_made += 1
        print("Your coffee is ready! Go take on the world (or at least check your emails).")

    
    def refill(self, beans=5, water=100):
        self.beans += beans
        self.water += water
        print(f"Refilled! Beans +{beans}, Water +{water}ml.")


# ==== Main Script Usuage ====

if __name__ == "__main__":
    my_coffee_machine = CoffeeMachine()

    print("\n[STATUS CHECK]")
    my_coffee_machine.status()

    print("\n[MAKE COFFEE]")
    my_coffee_machine.make_coffee()

    print("\n[STATUS CHECK]")
    my_coffee_machine.status()

    print("\n[RUNNING OUT OF STUFF!]")
    for i in range(11):  # Run it dry
        my_coffee_machine.make_coffee("doom-fuel")

    print("\n[REFILL TIME]")
    my_coffee_machine.refill(beans=10, water=200)

    print("\n[BACK TO WORK!]")
    my_coffee_machine.make_coffee("victory latte")

    print("\n[FINAL STATUS]")
    my_coffee_machine.status()

