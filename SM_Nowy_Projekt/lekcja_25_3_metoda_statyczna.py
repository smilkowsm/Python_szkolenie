import datetime

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


    @staticmethod
    def czy_dzien_pracujacy(day):
        return day.weekday() not in (5, 6)
    
if __name__ == "__main__":
    print(KlasaPrcownik.czy_dzien_pracujacy(datetime.date(2026, 1, 13)))
    print(datetime.date.today())