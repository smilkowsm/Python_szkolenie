from lekcja_25_3_metoda_statyczna import KlasaPrcownik

class Programista(KlasaPrcownik):
    wzrost_wynagrodzenia = 1.10

    def __init__(self, imie, nazwisko, wynagrodzenie_podstawowe, jezyk_programowania):
        super().__init__(imie, nazwisko, wynagrodzenie_podstawowe)
        self.jezyk_programowania = jezyk_programowania

    