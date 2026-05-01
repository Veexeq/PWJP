from datetime import date
from typing import Self, override


class Pojazd:
    def __init__(self, marka: str, model: str, rok: str) -> None:
        self.marka = marka
        self.model = model
        self.rok = rok

    def opis(self) -> str:
        desc = f"Pojazd(marka={self.marka}, model={self.model}, rok={self.rok})"
        return desc

    @classmethod
    def utworz_domyslny(cls) -> Self:
        default_object = cls(marka="BMW", model="E39", rok="1995")
        return default_object

    @staticmethod
    def czy_poprawny_rok(rok: int) -> bool:
        curr_year = date.today().year
        return 1885 <= rok <= curr_year


class Samochod(Pojazd):
    def __init__(self, marka: str, model: str, rok: str, liczba_drzwi: int) -> None:
        super().__init__(marka=marka, model=model, rok=rok)
        self.liczba_drzwi = liczba_drzwi

    @override
    def opis(self) -> str:
        desc = (
            f"Samochod(marka={self.marka}, model={self.model}, "
            f"rok={self.rok}, liczba_drzwi={self.liczba_drzwi})"
        )

        return desc

    @override
    @classmethod
    def utworz_domyslny(cls) -> Self:
        default_object = cls(
            marka="Volkswagen", model="Golf", rok="2008", liczba_drzwi=5
        )
        return default_object


class Motocykl(Pojazd):
    def __init__(self, marka: str, model: str, rok: str, typ: str) -> None:
        super().__init__(marka=marka, model=model, rok=rok)
        self.typ = typ

    @override
    def opis(self) -> str:
        desc = (
            f"Motocykl(marka={self.marka}, model={self.model}, "
            f"rok={self.rok}, typ={self.typ})"
        )

        return desc

    @override
    @classmethod
    def utworz_domyslny(cls) -> Self:
        default_object = cls(marka="Honda", model="NX500", rok="2024", typ="Crossover")
        return default_object
