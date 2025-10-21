lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

wynik = tuple(x * 2 for x in lista if x % 2 == 0) # Lista przeksztalcona na tuple
print(wynik)

wynik = {x * 2 for x in lista if x % 2 == 0} # Lista przeksztalcona na slownik
print(wynik)

ksiazka_telefoniczna = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}

print(ksiazka_telefoniczna.items())

nowy_slownik = {}
# Przerzucamy te itemy zeby klucz byl wartoscia a wartosc kluczem

ksiazka_telefoniczna.items(x, y) == ksiazka_telefoniczna.items(y, x)
print(ksiazka_telefoniczna.items())
