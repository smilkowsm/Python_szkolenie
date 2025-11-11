# Praca Domowa 1.3

# Zadanie 1
# Użytkownik wpisuje trzy cyfry. Utwórz liczbę zawierającą te cyfry. Jeśli wpisane cyfry to 1, 5, 7, utworzona liczba powinna wynosić 157.

liczba_1 = int(input("Wpisz pierwsza cyfre: "))
liczba_2 = int(input("Wpisz druga cyfre: "))
liczba_3 = int(input("Wpisz trzecia cyfre: "))
utworzona_liczba = str(liczba_1) + str(liczba_2) + str(liczba_3)
print(utworzona_liczba)

# Zadanie 2
# Użytkownik wpisuje czterocyfrową liczbę. Znajdź iloczyn tych cyfr. Jeśli wpisana liczba to 1324, wynik będzie następujący: 1*3*2*4 = 24.

while True:
    liczba = int(input("Podaj 4 cyfrowa liczbe: "))
    liczba = str(liczba)
    if len(liczba) == 4:
        lista = []
        for i in liczba:
            lista.append(int(i))
        iloczyn = lista[0] * lista[1] * lista[2] * lista[3]
        print(f"Iloczyn cyfr to {iloczyn}")
        break
    else:
        print("Liczba musi miec 4 cyfry!")
        continue

# Zadanie 3
# Użytkownik wpisuje liczbę metrów. Przelicz metry na centymetry, decymetry, milimetry, mile i wyświetl wynik.

metry = int(input("Podaj liczbe metrow: "))
centymetry = metry * 100
decymetry = metry * 10
milimetry = metry * 1000
mile = metry / 1609,344
print(f"{metry} metrow to:\n{centymetry} centymetrow\n{decymetry} decymetrow\n{milimetry} milimetrow\n{mile} mil")

# Zadanie 4
# Napisz program obliczający pole trójkąta. Użytkownik wpisuje podstawę i wysokość trójkąta.

podstawa = float(input("Podaj podstawe trojkata: "))
wysokosc = float(input("Podaj wysokosc trojkata: "))
pole = podstawa * wysokosc / 2
print(f"Pole trojkata wynosi {pole}")

# Zadanie 5
# Użytkownik wpisuje czterocyfrową liczbę. Odwróć liczbę i wydrukuj wynik. Jeśli wpisana liczba to 4512, wynikiem będzie 2154.

while True:
    liczba_4 = int(input("Podaj 4 cyfrowa liczbe: "))
    liczba_4 = str(liczba_4)
    if len(liczba_4) == 4:
        print(liczba_4[::-1])
        break
    else:
        print("Liczba musi miec 4 cyfry!")
        continue
