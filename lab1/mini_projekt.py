import sympy as sp
from typing import Callable

# Zadanie:
"""
Przy pomocy w.w. symboli i funkcji zdefiniować:
- cos
- tangens i cotanges
- funkcje hiperboliczne (sin, cos, tan, cotan)
- secans i cosecans
- wszystkie pochodne (pierwszego stopnia) w.w. funkcji
*Opcjonalnie*: użyć biblioteki sympy

Zaproponuj architekturę (ew. obiektową) i logikę wybierania funkcji przez użytkownika w terminalu

Całe rozwiązanie powinno się mieścić w jednym pliku.
Wyświetlać 3 miejsca po przecinku przy pomocy print(f"Wynik: {x}").

"""

def print_choices() -> None:
    print('Dostępne funkcje:')
    print('=== TRYGONOMETRYCZNE ===')
    print('1. y = sin(x)')
    print('2. y = cos(x)')
    print('3. y = tan(x)')
    print('4. y = cot(x)')
    print('5. y = sec(x)')
    print('6. y = csc(x)')
    print('=== HIPERBOLICZNE ===')
    print('7. y = sinh(x)')
    print('8. y = cosh(x)')
    print('9. y = tanh(x)')
    print('10. y = coth(x)')
    print('=== PIERWSZE POCHODNE ===')
    print('Aby wybrać pochodną danej funkcji należy dopisać do identyfikatora \'f\', np. \'4f\' -> y = cot\'(x)')
    print('========================')

def input_control() -> tuple[int, bool, float]:
    while True:
        choice_str = input('Proszę wybrać funkcję lub jej pochodną poprzez jej numer: ').strip()
        if not choice_str:
            continue
            
        chose_derivative = False
        if choice_str[-1].lower() == 'f':
            chose_derivative = True
            choice_str = choice_str[:-1]
            
        if choice_str.isnumeric():
            choice = int(choice_str)
            if 1 <= choice <= 10:
                break
                
        print('Niepoprawny numer. Proszę podać liczbę z zakresu [1, 10] z ewentualnym suffixem \'f\'.')

    while True:
        try:
            x_val = float(input('Podaj argument funkcji: '))
            break
        except ValueError:
            print('Błąd: Oczekiwano liczby. Spróbuj ponownie.')

    return choice, chose_derivative, x_val

def get_function(choice: int, chose_derivative: bool) -> tuple[sp.Expr, Callable[[float], float]]:
    x = sp.Symbol('x')
    math_functions = {
        1:  sp.sin,
        2:  sp.cos,
        3:  sp.tan,
        4:  sp.cot,
        5:  sp.sec,
        6:  sp.csc,
        7:  sp.sinh,
        8:  sp.cosh,
        9:  sp.tanh,
        10: sp.coth
    }

    selected_function = math_functions[choice]
    expression = selected_function(x)
    
    if chose_derivative:
        expression = sp.diff(expression, x)
        
    def evaluate_function(arg_value: float) -> float:
        return float(expression.subs(x, arg_value).evalf())     # type: ignore
        
    return expression, evaluate_function
    
def main() -> None:
    print_choices()
    choice, chose_derivative, arg = input_control()
    expression, function = get_function(choice, chose_derivative)
    res = function(arg)
    
    try:
        print(f'Wybrany wzór matematyczny: y = {expression}')
        print(f'Wynik: {res:.3f}')
    except TypeError:
        print('Niepoprawne wywołanie funkcji, najpewniej dzielenie przez zero.')
    
if __name__ == '__main__':
    main()
    