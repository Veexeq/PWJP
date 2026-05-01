import unittest


def run_all_tests() -> None:
    print("Uruchamiam wszystkie testy dla laboratorium 4")

    # 1. Tworzymy obiekt wyszukujący testy (TestLoader)
    loader = unittest.TestLoader()

    # 2. Wskazujemy folder startowy ('tests') i wzorzec nazw plików ('test_*.py')
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    # 3. Konfigurujemy 'uruchamiacza' (TextTestRunner)
    # verbosity=2 sprawia, że w konsoli zobaczysz nazwę każdego testu
    runner = unittest.TextTestRunner(verbosity=2)

    # 4. Uruchamiamy zebrane testy
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()
