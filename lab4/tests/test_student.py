import unittest
from io import StringIO
from unittest.mock import patch

from src.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student1 = Student(imie="Jan", nazwisko="Nowak", indeks="389211")
        self.student2 = Student(imie="Paweł", nazwisko="Kowalski", indeks="401498")

    def test_str(self) -> None:
        # Sprawdzamy czy __str__ zwraca string z prawidłowymi danymi
        opis = str(self.student1)
        self.assertIn("Jan", opis)
        self.assertIn("Nowak", opis)
        self.assertIn("389211", opis)

    @patch("sys.stdout", new_callable=StringIO)
    def test_przedstaw_sie(self, mock_stdout: StringIO) -> None:
        # Przechwytujemy print() i sprawdzamy jego zawartość
        self.student2.przedstaw_sie()
        output = mock_stdout.getvalue()
        self.assertIn("Paweł", output)
        self.assertIn("Kowalski", output)
