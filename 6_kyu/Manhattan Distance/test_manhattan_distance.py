import unittest
from manhattan_distance import manhattan_distance


class TestManhattanDistance(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(manhattan_distance([1, 1], [1, 1]), 0)
        self.assertEqual(manhattan_distance([5, 4], [3, 2]), 4)
        self.assertEqual(manhattan_distance([1, 1], [0, 3]), 3)


if __name__ == '__main__':
    unittest.main()
