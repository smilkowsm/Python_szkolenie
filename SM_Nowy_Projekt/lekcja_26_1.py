from lekcja_25_3_metoda_statyczna import Pracownik
from lekcja_25_4_klasa_programista import Programista


class Menadzer(Pracownik):

    def __init__(self, imie, nazwisko, wyplata, pracownicy=None):
        super().__init__(imie, nazwisko, wyplata)
        if pracownicy:
            self.pracownicy = pracownicy
        else:
            self.pracownicy = set()

    def dodaj_pracownika(self, pracownik):
        self.pracownicy.add(pracownik)

    def usun_pracownika(self, pracownik):
        if pracownik in self.pracownicy:
            self.pracownicy.remove(pracownik)
        else:
            print(f"{pracownik.pelne_imie()} nie jest podwładnym {self.pelne_imie()}")

    def drukuj_pracownikow(self):
        print(f"Pracownik {self.pelne_imie()}:")
        for pracownik in self.pracownicy:
            print(f"\t- {pracownik.pelne_imie()}")


if __name__ == '__main__':
    arek = Menadzer("Arkadiusz", "Binder", 4000)
    roman = Pracownik("Roman", "Romanowski", 4000)
    wisniewksa = Programista("Anna", "Wisniewska", 6000, "Pyhon")
    kowalski = Pracownik("Jan", "Kowalski", 4000)

    arek.dodaj_pracownika(roman)
    arek.dodaj_pracownika(wisniewksa)
    print("Pracownicy arka: ", arek.pracownicy)
    arek.drukuj_pracownikow()

    arek.usun_pracownika(wisniewksa)
    arek.drukuj_pracownikow()

    arek.usun_pracownika(kowalski)

    wisniewksa.zwieksz_wynagrodzenie()
    print(wisniewksa.wyplata)
