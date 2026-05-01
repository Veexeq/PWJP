import util
from KontoBankowe import KontoBankowe
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

def test_intermediate() -> None:
    util.print_header(text='POZIOM ŚREDNIOZAAWANSOWANY')
    
    bank_account = KontoBankowe()
    
    # Dostęp do prywatnego atrybutu przez getter, oraz
    # użycie `pokaz_saldo()`
    print(f'Saldo przez getter: {bank_account.saldo}')
    bank_account.pokaz_saldo()
    
    # Akceptowalna wpłata
    good_deposit = 100.05
    bank_account.wplac(kwota=good_deposit)
    print(f'Saldo po dobrej wpłacie: {bank_account.saldo}')
    
    # Akceptowalna wypłata
    good_withdrawal = 44.86
    bank_account.wyplac(kwota=good_withdrawal)
    print(f'Saldo po dobrej wypłacie: {bank_account.saldo}')
    
    # Nieakceptowalna wpłata (ujemna kwota)
    try:
        bad_deposit = -5.2
        bank_account.wplac(kwota=bad_deposit)
    except ValueError as e:
        print(f'EXCEPTION: {e}')
    except Exception as e:
        print(f'Wystąpił nieoczekiwany błąd [{type(e).__name__}]: {e}')
    
    # Nieakceptowalna wypłata (zbyt duża)
    try:
        bad_withdrawal = bank_account.saldo * 2
        bank_account.wyplac(kwota=bad_withdrawal)
    except ValueError as e:
        print(f'EXCEPTION: {e}')
    except Exception as e:
        print(f'Wystąpił nieoczekiwany błąd [{type(e).__name__}]: {e}')
    
    # Nieakcpetowalna wypłata (ujemna kwota)
    try:
        bad_withdrawal = -1.78
        bank_account.wyplac(kwota=bad_withdrawal)
    except ValueError as e:
        print(f'EXCEPTION: {e}')
    except Exception as e:
        print(f'Wystąpił nieoczekiwany błąd [{type(e).__name__}]: {e}')
    
def test_advanced() -> None:
    ...

def run_all_tests() -> None:
    test_basic()
    test_intermediate()
