import unittest

import tekst


class TekstTest(unittest.TestCase):
    def test_zwraca_dwie_litery(self):
        self.assertEqual(len(tekst.inicjaly("Jan", "Kowalski")), 2)

    def test_pierwsza_litera_nazwiska(self):
        self.assertEqual(tekst.inicjaly("Jan", "Kowalski"), "JK")


if __name__ == "__main__":
    unittest.main()
