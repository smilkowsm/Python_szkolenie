class KlasaPrcownik:
    """Klasa Pracownik"""
    wzrost_wynagrodzenia = 1.04

    def __init__(self, imie, nazwisko, wynagrodzenie_podstawowe):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_podstawowe = wynagrodzenie_podstawowe
        self.email = f"{imie}.{nazwisko}@praca.com"

    def pelne_imie(self):
        return f"{self.imie} {self.nazwisko}"

    def podwyzka(self):
        self.wynagrodzenie_podstawowe = int(self.wynagrodzenie_podstawowe * self.wzrost_wynagrodzenia)

    @classmethod
    def ustaw_warost_wynagrodzenia(cls, nowy_wzrost_wynagrodzenia):
        cls.wzrost_wynagrodzenia = nowy_wzrost_wynagrodzenia

if __name__ == "__main__":
    pracownik = KlasaPrcownik("Sebastian", "Milkowski", 10000)
    kowalski = KlasaPrcownik("Jan", "Kowalski", 5000)

    print("Wysokosc podwyzek pracownikow:", KlasaPrcownik.wzrost_wynagrodzenia)

    print("Milkowski:", pracownik.wzrost_wynagrodzenia)
    print("Kowalski:", kowalski.wzrost_wynagrodzenia)

    KlasaPrcownik.ustaw_warost_wynagrodzenia(1.05)

    print("Wysokosc podwyzek pracownikow:", KlasaPrcownik.wzrost_wynagrodzenia)

    print("Milkowski:", pracownik.wzrost_wynagrodzenia)
    print("Kowalski:", kowalski.wzrost_wynagrodzenia)

    