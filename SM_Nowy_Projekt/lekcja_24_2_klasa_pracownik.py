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



pracownik = KlasaPrcownik("Sebastian", "Milkowski", 10000)
print(pracownik.imie)
print(pracownik.nazwisko)
print(pracownik.pelne_imie())
print(pracownik.email)
print(pracownik.wynagrodzenie_podstawowe)
pracownik.podwyzka()
print(pracownik.wynagrodzenie_podstawowe)
pracownik.podwyzka()
pracownik.podwyzka()
pracownik.podwyzka()
print(pracownik.wynagrodzenie_podstawowe)


kowalski = KlasaPrcownik("Jan", "Kowalski", 5000)
print(kowalski.imie)
print(kowalski.nazwisko)
print(kowalski.pelne_imie())
print(kowalski.email)
print(kowalski.wynagrodzenie_podstawowe)
kowalski.wzrost_wynagrodzenia = 2.0 # Zmieniamy wartosc zmiennej globalnej
kowalski.podwyzka()
print(kowalski.wynagrodzenie_podstawowe)
