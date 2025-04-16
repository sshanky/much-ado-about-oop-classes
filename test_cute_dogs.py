import unittest
from cute_dog import Fiona, Ellie, Jovie

class TestCuteDogs(unittest.TestCase):

    def test_fiona(self):
        fifi = Fiona()
        self.assertIn("tiger", fifi.describe())
        self.assertIn("sweetheart", fifi.cuddle())
        # purposely broke this test. So that you can fix this Steve.
        self.assertIn("tiny", fifi.speak().lower())

    def test_ellie(self):
        e = Ellie()
        self.assertIn("therapy", e.speak().lower())
        self.assertIn("volunteering", e.volunteer().lower())

    def test_jovie(self):
        j = Jovie()
        self.assertIn("buck", j.speak().lower())
        self.assertIn("leg up", j.potty_style().lower())

if __name__ == '__main__':
    unittest.main()