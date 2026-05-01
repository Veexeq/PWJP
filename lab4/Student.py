class Student:
    def __init__(self, imie: str, nazwisko: str, indeks: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._indeks = indeks
    
    def przedstaw_sie(self) -> None:
       print(f'Jestem {self._imie} {self._nazwisko} ' 
             f'mój numer indeksu to {self._indeks}.')
    
    def __str__(self) -> str:
        return f'Student {self._imie} {self._nazwisko}, nr indeksu {self._indeks}'
