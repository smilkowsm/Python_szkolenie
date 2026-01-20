from lekcja_25_3_metoda_statyczna import KlasaPrcownik

class Menadzer(KlasaPrcownik):

    def __init__(self, imie, nazwisko, wynagrodzenie_podstawowe, pracownicy=None):
        super().__init__(imie, nazwisko, wynagrodzenie_podstawowe)
        if pracownicy:
            self.pracownicy = pracownicy
        else:
            self.pracownicy = set()