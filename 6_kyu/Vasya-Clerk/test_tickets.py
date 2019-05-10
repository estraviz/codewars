import unittest
from tickets import tickets


class TestTickets(unittest.TestCase):

    def test_tickets(self):
        bills = [25, 25, 50]
        self.assertEqual(tickets(bills), "YES")

        bills = [25, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
        self.assertEqual(tickets(bills), "YES")

        bills = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        self.assertEqual(tickets(bills), "NO")

        bills = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 25, 25, 50, 100, 50]
        self.assertEqual(tickets(bills), "YES")

        bills = [50, 100, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 50, 50, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 50, 50]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 25, 25, 100]
        self.assertEqual(tickets(bills), "YES")

        bills = [25, 50, 25, 100]
        self.assertEqual(tickets(bills), "YES")

        bills = [25, 25, 25, 25, 25, 100, 100]
        self.assertEqual(tickets(bills), "NO")

        bills = [25, 50, 25, 100, 25, 25, 50, 100, 25, 25, 25, 100, 25, 25, 50,
                 100, 25, 50, 25, 100, 25, 50, 50, 50]
        self.assertEqual(tickets(bills),  "NO")

        bills = [25, 25, 25, 100, 25, 25, 25, 100, 25, 25, 50, 100, 25, 25, 50,
                 100, 50, 50]
        self.assertEqual(tickets(bills),  "NO")

        bills = [25, 50, 25, 100, 25, 25, 50, 100, 25, 50, 25, 100, 50, 25]
        self.assertEqual(tickets(bills),  "NO")


if __name__ == '__main__':
    unittest.main()
