import unittest

from src.biblioteka import Biblioteka, BookNotAvailable, Ksiazka, Uzytkownik


class TestSystemuBibliotecznego(unittest.TestCase):
    def setUp(self) -> None:
        """
        Metoda setUp wykonuje się przed każdym pojedynczym testem.
        Przygotowujemy tutaj świeże obiekty, aby testy były od siebie niezależne.
        """
        self.k1 = Ksiazka("Wiedźmin", "Andrzej Sapkowski")
        self.k2 = Ksiazka("Solaris", "Stanisław Lem")

        self.u1 = Uzytkownik("Jan", "Kowalski")
        self.u2 = Uzytkownik("Anna", "Nowak")

        self.biblioteka = Biblioteka()

    # --- TESTY KLASY KSIAZKA ---

    def test_ksiazka_wypozycz_i_zwroc(self):
        self.assertTrue(self.k1.czy_dostepna, "Nowa książka powinna być dostępna")

        self.k1.wypozycz()
        self.assertFalse(
            self.k1.czy_dostepna, "Po wypożyczeniu książka nie jest dostępna"
        )

        self.k1.zwroc()
        self.assertTrue(self.k1.czy_dostepna, "Po zwrocie książka znów jest dostępna")

    def test_ksiazka_porownywanie_eq(self):
        k3 = Ksiazka("Wiedźmin", "Andrzej Sapkowski")
        self.assertEqual(
            self.k1, k3, "Książki o tych samych atrybutach powinny być równe"
        )
        self.assertNotEqual(self.k1, self.k2, "Różne książki nie powinny być równe")

    # --- TESTY KLASY UZYTKOWNIK ---

    def test_uzytkownik_dziedziczenie_z_dataklasy(self):
        self.assertEqual(self.u1.imie, "Jan")
        self.assertEqual(self.u1.nazwisko, "Kowalski")
        self.assertEqual(len(self.u1.lista_wypozyczen), 0)

    def test_uzytkownik_dodaj_i_usun_ksiazke(self):
        self.u1.dodaj_ksiazke(self.k1)
        self.assertIn(self.k1, self.u1.lista_wypozyczen)

        self.u1.usun_ksiazke(self.k1)
        self.assertNotIn(self.k1, self.u1.lista_wypozyczen)

    def test_uzytkownik_wyjatki(self):
        with self.assertRaises(ValueError):
            self.u1.dodaj_ksiazke(None)  # type: ignore

        with self.assertRaises(ValueError):
            self.u1.usun_ksiazke(self.k1)  # Próba usunięcia książki, której nie ma

    def test_uzytkownik_porownywanie_eq(self):
        u3 = Uzytkownik("Jan", "Kowalski")
        self.assertEqual(
            self.u1, u3, "Użytkownicy z tą samą historią i danymi są równi"
        )

        self.u1.dodaj_ksiazke(self.k1)
        self.assertNotEqual(
            self.u1, u3, "Różna lista wypożyczeń sprawia, że użytkownicy nie są równi"
        )

    # --- TESTY KLASY BIBLIOTEKA ---

    def test_biblioteka_dodawanie(self):
        self.biblioteka.add_book(self.k1)
        self.biblioteka.add_user(self.u1)

        self.assertIn(self.k1, self.biblioteka.ksiazki)
        self.assertIn(self.u1, self.biblioteka.uzytkownicy)

    def test_biblioteka_wypozyczenie_sukces(self):
        self.biblioteka.add_book(self.k1)
        self.biblioteka.add_user(self.u1)

        self.biblioteka.borrow_book(self.u1, self.k1)

        self.assertFalse(self.k1.czy_dostepna)
        self.assertIn(self.k1, self.u1.lista_wypozyczen)

    def test_biblioteka_wypozyczenie_wyjatki(self):
        self.biblioteka.add_book(self.k1)
        self.biblioteka.add_user(self.u1)

        # Książka nie znajduje się w bibliotece
        with self.assertRaises(ValueError):
            self.biblioteka.borrow_book(self.u1, self.k2)

        # Użytkownik nie znajduje się w bibliotece
        with self.assertRaises(ValueError):
            self.biblioteka.borrow_book(self.u2, self.k1)

        # Książka jest już wypożyczona
        self.biblioteka.borrow_book(self.u1, self.k1)
        with self.assertRaises(BookNotAvailable):
            self.biblioteka.borrow_book(self.u1, self.k1)

    def test_biblioteka_zwrot_sukces(self):
        self.biblioteka.add_book(self.k1)
        self.biblioteka.add_user(self.u1)
        self.biblioteka.borrow_book(self.u1, self.k1)

        self.biblioteka.return_book(self.u1, self.k1)

        self.assertTrue(self.k1.czy_dostepna)
        self.assertNotIn(self.k1, self.u1.lista_wypozyczen)
