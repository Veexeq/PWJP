import unittest

from src.konto_bankowe import KontoBankowe


class TestKontoBankowe(unittest.TestCase):
    def setUp(self) -> None:
        self.konto = KontoBankowe()

    def test_saldo_poczatkowe(self) -> None:
        # Zakładam, że początkowe saldo to 0.0
        self.assertEqual(self.konto.saldo, 0.0)

    def test_poprawna_wplata(self) -> None:
        self.konto.wplac(100.05)
        self.assertAlmostEqual(self.konto.saldo, 100.05)

    def test_poprawna_wyplata(self) -> None:
        self.konto.wplac(100.00)
        self.konto.wyplac(44.86)
        # Używamy assertAlmostEqual ze względu na specyfikę floatów w Pythonie
        self.assertAlmostEqual(self.konto.saldo, 55.14)

    def test_wplata_ujemna_kwota_rzuca_wyjatek(self) -> None:
        with self.assertRaises(ValueError):
            self.konto.wplac(-5.2)

    def test_wyplata_za_duza_kwota_rzuca_wyjatek(self) -> None:
        self.konto.wplac(50.0)
        with self.assertRaises(ValueError):
            self.konto.wyplac(100.0)

    def test_wyplata_ujemna_kwota_rzuca_wyjatek(self) -> None:
        with self.assertRaises(ValueError):
            self.konto.wyplac(-1.78)
