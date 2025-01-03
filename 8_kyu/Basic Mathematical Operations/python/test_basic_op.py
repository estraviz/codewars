import unittest
from basic_op import basic_op


class TestBasicOp(unittest.TestCase):

    def test_basic_op(self):
        self.assertEqual(basic_op('+', 4, 7), 11)
        self.assertEqual(basic_op('-', 15, 18), -3)
        self.assertEqual(basic_op('*', 5, 5), 25)
        self.assertEqual(basic_op('/', 49, 7), 7)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError) as exc:
            basic_op('/', 1, 0)
        self.assertEqual("division by zero", str(exc.exception))


if __name__ == '__main__':
    unittest.main()
