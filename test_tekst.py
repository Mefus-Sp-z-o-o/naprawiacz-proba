import unittest

import tekst


class TekstTest(unittest.TestCase):
    def test_zwraca_dwie_litery(self):
        self.assertEqual(len(tekst.inicjaly("Jan", "Kowalski")), 2)


if __name__ == "__main__":
    unittest.main()
