import unittest
from rental_car_cost import rental_car_cost


class TestRentalCarCost(unittest.TestCase):

    def test_rental_car_cost(self):
        self.assertEqual(rental_car_cost(1), 40)
        self.assertEqual(rental_car_cost(2), 80)
        self.assertEqual(rental_car_cost(3), 100)
        self.assertEqual(rental_car_cost(4), 140)
        self.assertEqual(rental_car_cost(5), 180)
        self.assertEqual(rental_car_cost(6), 220)
        self.assertEqual(rental_car_cost(7), 230)
        self.assertEqual(rental_car_cost(8), 270)
        self.assertEqual(rental_car_cost(9), 310)
        self.assertEqual(rental_car_cost(10), 350)


if __name__ == '__main__':
    unittest.main()
