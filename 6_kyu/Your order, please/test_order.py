import unittest
from order import order


class TestOrder(unittest.TestCase):

    def test_order(self):
        s = "is2 Thi1s T4est 3a"
        self.assertEqual(order(s), "Thi1s is2 3a T4est")

        s = "4of Fo1r pe6ople g3ood th5e the2"
        self.assertEqual(order(s), "Fo1r the2 g3ood 4of th5e pe6ople")

        s = "d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"
        result = "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor"
        self.assertEqual(order(s), result)

        self.assertEqual(order(""), "")

        self.assertEqual(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")


if __name__ == '__main__':
    unittest.main()
