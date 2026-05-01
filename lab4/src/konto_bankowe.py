class KontoBankowe:
    def __init__(self, startowe_saldo: float = 0.0) -> None:
        self.__saldo: float = startowe_saldo
    
    @property
    def saldo(self) -> float:
        return self.__saldo

    def wplac(self, kwota: float) -> None:
        if kwota <= 0:
            raise ValueError('Kwota wpłaty musi być liczbą większą od zera')
        
        self.__saldo += kwota

    def wyplac(self, kwota: float) -> None:
        if kwota <= 0:
            raise ValueError('Kwota wypłaty musi być liczbą większą od zera')
        if kwota > self.__saldo:
            raise ValueError('Kwota wypłaty musi być mniejsza od aktualnego salda')
        
        self.__saldo -= kwota
    
    def pokaz_saldo(self) -> None:
        print(f'Aktualne saldo: {self.__saldo:.2f} zł')
