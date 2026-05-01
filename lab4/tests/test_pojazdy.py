import unittest

from src.pojazdy import Motocykl, Pojazd, Samochod


class TestPojazdy(unittest.TestCase):
    def setUp(self) -> None:
        self.auto = Samochod(
            marka="Toyota", model="Corolla", rok="2020", liczba_drzwi=5
        )
        self.moto = Motocykl(marka="Yamaha", model="MT-07", rok="2022", typ="Naked")

    def test_opis_polimorfizm(self) -> None:
        # Każda klasa powinna zwracać odpowiedni string
        self.assertIn("Toyota", self.auto.opis())
        self.assertIn("Yamaha", self.moto.opis())

    def test_utworz_domyslny_metoda_klasowa(self) -> None:
        auto_domyslne = Samochod.utworz_domyslny()
        moto_domyslne = Motocykl.utworz_domyslny()

        self.assertIsInstance(auto_domyslne, Samochod)
        self.assertIsInstance(moto_domyslne, Motocykl)

    def test_czy_poprawny_rok_metoda_statyczna(self) -> None:
        # Lata poprawne (zakładając, że logika akceptuje np. 1886-2024)
        self.assertTrue(Pojazd.czy_poprawny_rok(1995))
        self.assertTrue(Pojazd.czy_poprawny_rok(2024))

        # Lata niepoprawne
        self.assertFalse(Pojazd.czy_poprawny_rok(1800))
        self.assertFalse(
            Pojazd.czy_poprawny_rok(2030)
        )  # Jeśli akceptuje w przyszłość, zmień na assertTrue
