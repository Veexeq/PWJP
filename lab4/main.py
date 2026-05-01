class Student:
    def __init__(self, imie: str, nazwisko: str, indeks: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._indeks = indeks
    
    def przedstaw_sie(self) -> None:
       print(f'Jestem {self._imie} {self._nazwisko}' 
             f'mój numer indeksu to {self._indeks}.')
    
    def __str__(self) -> str:
        return f'Student {self._imie} {self._nazwisko}, nr indeksu {self._indeks}'
    
def test_basic() -> None:
    students = [
        Student(imie='Jan', nazwisko='Nowak', indeks='389211'),
        Student(imie='Paweł', nazwisko='Kowalski', indeks='401498'),
    ]
        
    for student in students:
        print(f'przedstaw_sie(): {student.przedstaw_sie()}')
        print(f'__str__(): {student}')

if __name__ == '__main__':
    test_basic()
