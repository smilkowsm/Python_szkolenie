pusty_slownik = {}
print(f"pusty_slownik:\nzawartosc - {pusty_slownik}\n\tTyp - {type(pusty_slownik)} ")

ksiazka_telefoniczna = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}
print(ksiazka_telefoniczna)
print(ksiazka_telefoniczna["Pizzeria"]) # Wywolujemy wartosc za pomoca klucza w []

ksiazka_telefoniczna["Pizzeria"] = 987654321 # Zmiana wartosci dla klucza
print(ksiazka_telefoniczna["Pizzeria"])

ksiazka_telefoniczna["Mama"] = 3255 # Dodawanie wpisow do slownika
print(ksiazka_telefoniczna)

print("*"*50)
print(f"Zawartosc ksiazka_telefoniczna: {ksiazka_telefoniczna}")


print("*"*50)
if "Tata" in ksiazka_telefoniczna:
    print(f"Wartosc klucza 'Tata' w  ksiazka_telefoniczna: {ksiazka_telefoniczna}")
else:
    print("Nie ma takiego klucza!")

print(f"Wartosc klucza 'Tata' w  ksiazka_telefoniczna: {ksiazka_telefoniczna.get("Tata")}") # Wyciaga wartosc bez wywolywania bledu, jesli wartosci nie ma - swraca None


for klucz in ksiazka_telefoniczna: # ksiazka_telefoniczna to samo co ksiazka_telefoniczna.keys()
    print(f"Klucze z ksiazka_telefoniczna: {klucz}")
print("*"*50)

for wartosc in ksiazka_telefoniczna.values():
    print(f"Wartosc z ksiazka_telefoniczna: {wartosc}")
print("*"*50)

for pary_klucz_wartosc in ksiazka_telefoniczna.items():
    print(f"pary_klucz_wartosc z ksiazka_telefoniczna: {pary_klucz_wartosc}")
print("*"*50)

for klucz, wartosc in ksiazka_telefoniczna.items():
    print(f"\t- {klucz}: {wartosc}")