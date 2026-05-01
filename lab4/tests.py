import util
from Student import Student


def test_basic() -> None:
    util.print_header(text='POZIOM PODSTAWOWY')
    
    students = [
        Student(imie='Jan', nazwisko='Nowak', indeks='389211'),
        Student(imie='Paweł', nazwisko='Kowalski', indeks='401498'),
    ]
    
    for idx, student in enumerate(students, start=1):
        print(f'{idx}. Student:')
        print('przedstaw_sie():', end=' ')
        student.przedstaw_sie()
        print(f'__str__(): {student}\n')
