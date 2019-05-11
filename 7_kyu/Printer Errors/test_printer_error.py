import unittest
from printer_error import printer_error


class TestPrinterError(unittest.TestCase):

    def test_printer_error(self):
        s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        self.assertEqual(printer_error(s), "3/56")

        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        self.assertEqual(printer_error(s), "6/60")

        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        self.assertEqual(printer_error(s), "11/65")


if __name__ == '__main__':
    unittest.main()
