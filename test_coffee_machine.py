# this is basic common unit testing application made for python.
import unittest

# Here we are simply importing entire contents of file called `coffee_machine.py`
# And we will now be able reference all the code on that page with `CoffeeMachine`
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):
    # Since we have a known starting state.
    # We should simply start with creating a simple
    # Test that ensures that the class starts in correct state
    def test_initial_status(self):
        # Here we are creating a new coffee machine instance and saving it
        # to the variable now known as `machine`
        machine = CoffeeMachine()
        self.assertEqual(machine.beans, 10)
        self.assertEqual(machine.water, 100)
        self.assertEqual(machine.cups_made, 0)

    def test_make_coffee_reduces_resources(self):
        machine = CoffeeMachine(beans=0, water=10)
        # so here we are invoking `make_coffee` function found in our class.
        machine.make_coffee()
        self.assertEqual(machine.beans, 9)
        self.assertEqual(machine.water, 80)
        self.assertEqual(machine.cups_made, 1)