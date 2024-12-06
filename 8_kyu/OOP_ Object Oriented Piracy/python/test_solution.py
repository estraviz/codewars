import unittest

from solution import Ship


class TestShip(unittest.TestCase):

    def test_empty_ship(self):
        empty_ship = Ship(0, 0)
        self.assertEqual(empty_ship.is_worth_it(), False)

    def test_boat(self):
        boat = Ship(15, 20)
        self.assertEqual(boat.is_worth_it(), False)

    def test_worthy_ship(self):
        worthy_ship = Ship(100, 20)
        self.assertEqual(worthy_ship.is_worth_it(), True)

    def test_big_boat(self):
        big_boat = Ship(35, 20)
        self.assertEqual(big_boat.is_worth_it(), False)
