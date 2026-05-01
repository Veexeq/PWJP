class Student:
    def __init__(self, imie: str, nazwisko: str, indeks: str) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__indeks = indeks
    
    def przedstaw_sie(self) -> None:
       print(f'Jestem {self.__imie} {self.__nazwisko} ' 
             f'mój numer indeksu to {self.__indeks}.')
    
    def __str__(self) -> str:
        return f'Student {self.__imie} {self.__nazwisko}, nr indeksu {self.__indeks}'
