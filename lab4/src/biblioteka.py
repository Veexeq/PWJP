from dataclasses import dataclass
from typing import override


class BookNotAvailable(Exception):
    pass


class Ksiazka:
    def __init__(self, tytul: str, autor: str, czy_dostepna: bool = True) -> None:
        self.__tytul = tytul
        self.__autor = autor
        self.__czy_dostepna = czy_dostepna

    @property
    def tytul(self) -> str:
        return self.__tytul

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def czy_dostepna(self) -> bool:
        return self.__czy_dostepna

    def wypozycz(self) -> None:
        self.__czy_dostepna = False

    def zwroc(self) -> None:
        self.__czy_dostepna = True

    @override
    def __repr__(self) -> str:
        return (
            f"Ksiazka(tytul={self.tytul}, autor={self.autor}, "
            f"czy_dostepna={self.__czy_dostepna}"
        )

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ksiazka):
            return NotImplemented
        return (
            self.autor == other.autor
            and self.tytul == other.tytul
            and self.czy_dostepna == other.czy_dostepna
        )


@dataclass(frozen=True)
class Osoba:
    imie: str
    nazwisko: str


class Uzytkownik(Osoba):
    def __init__(
        self, imie: str, nazwisko: str, lista_wypozyczen: list[Ksiazka] | None = None
    ) -> None:
        super().__init__(imie=imie, nazwisko=nazwisko)
        if lista_wypozyczen is not None:
            self.__lista_wypozyczen = lista_wypozyczen.copy()
        else:
            self.__lista_wypozyczen: list[Ksiazka] = []

    @property
    def lista_wypozyczen(self) -> list[Ksiazka]:
        return self.__lista_wypozyczen

    def dodaj_ksiazke(self, ksiazka: Ksiazka) -> bool:
        if ksiazka is None:
            raise ValueError("Podano None zamiast książki")
        self.__lista_wypozyczen.append(ksiazka)
        return True

    def usun_ksiazke(self, ksiazka: Ksiazka) -> bool:
        if ksiazka is None:
            raise ValueError("Podano None zamiast książki")
        if ksiazka not in self.lista_wypozyczen:
            raise ValueError(f"Użytkownik {self} nie wypożyczał książki {ksiazka}")
        self.__lista_wypozyczen.remove(ksiazka)
        return True

    @override
    def __repr__(self) -> str:
        return (
            f"Uzytkownik(imie={self.imie}, nazwisko={self.nazwisko}, "
            f"lista_wypozyczen={self.__lista_wypozyczen})"
        )

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Uzytkownik):
            return NotImplemented
        return (
            self.imie == other.imie
            and self.nazwisko == other.nazwisko
            and self.lista_wypozyczen == other.lista_wypozyczen
        )


class Biblioteka:
    def __init__(
        self,
        ksiazki: list[Ksiazka] | None = None,
        uzytkownicy: list[Uzytkownik] | None = None,
    ) -> None:
        if ksiazki is not None:
            self.__ksiazki = ksiazki.copy()
        else:
            self.__ksiazki: list[Ksiazka] = []
        if uzytkownicy is not None:
            self.__uzytkownicy = uzytkownicy.copy()
        else:
            self.__uzytkownicy: list[Uzytkownik] = []

    @property
    def ksiazki(self) -> list[Ksiazka]:
        return self.__ksiazki

    @property
    def uzytkownicy(self) -> list[Uzytkownik]:
        return self.__uzytkownicy

    def add_book(self, nowa_ksiazka: Ksiazka) -> None:
        if nowa_ksiazka is None:
            raise ValueError("Nie można dodać pustego obiektu (None) jako książki")
        self.__ksiazki.append(nowa_ksiazka)

    def borrow_book(self, uzytkownik: Uzytkownik, ksiazka: Ksiazka) -> None:
        if uzytkownik is None:
            raise ValueError("Podano None zamiast użytkownika")
        if ksiazka is None:
            raise ValueError("Podano None zamiast książki")
        if uzytkownik not in self.__uzytkownicy:
            raise ValueError(
                f"Użytkownik {uzytkownik} nie znajduje się na liście "
                f"użytkowników tej biblioteki"
            )
        if ksiazka not in self.__ksiazki:
            raise ValueError(
                f"Książka {ksiazka} nie znajduje się na liście książek tej biblioteki"
            )
        if not ksiazka.czy_dostepna:
            raise BookNotAvailable(
                f"Książka {ksiazka} jest już wypożyczona, nie można wypożyczyć"
            )

        ksiazka.wypozycz()
        uzytkownik.dodaj_ksiazke(ksiazka=ksiazka)

    def return_book(self, uzytkownik: Uzytkownik, ksiazka: Ksiazka) -> None:
        if uzytkownik is None:
            raise ValueError("Podano None zamiast użytkownika")
        if ksiazka is None:
            raise ValueError("Podano None zamiast książki")
        if uzytkownik not in self.__uzytkownicy:
            raise ValueError(
                f"Użytkownik {uzytkownik} nie znajduje się na liście "
                f"użytkowników tej biblioteki"
            )
        if ksiazka not in self.__ksiazki:
            raise ValueError(
                f"Książka {ksiazka} nie znajduje się na liście książek tej biblioteki"
            )
        if ksiazka not in uzytkownik.lista_wypozyczen:
            raise ValueError(
                f"Użytkownik {uzytkownik} nie wypożyczał książki {ksiazka}"
            )

        ksiazka.zwroc()
        uzytkownik.usun_ksiazke(ksiazka=ksiazka)

    def add_user(self, nowy_uzytkownik: Uzytkownik) -> None:
        if nowy_uzytkownik is None:
            raise ValueError("Nie można dodać None jako nowego użytkownika")
        self.__uzytkownicy.append(nowy_uzytkownik)

    @override
    def __repr__(self) -> str:
        return f"Biblioteka(ksiazki={self.__ksiazki}, uzytkownicy={self.__uzytkownicy})"
