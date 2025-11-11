# Praktyka 2.4

# Zadanie 1
# Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby z podanego zakresu.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
print("Liczby z podanego zakresu:")
for liczba in range(liczba_1, liczba_2 + 1):
    print(liczba, end = " ")

# Zadanie 2
# Użytkownik wpisuje dwie liczby. Wydrukuj wszystkie liczby nieparzyste z podanego zakresu.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczby_nieparzyste = []
for liczba in range(liczba_1, liczba_2 + 1):
    if liczba % 2 != 0:
        liczby_nieparzyste.append(liczba)
print(f"Liczby nieparzyste z podanego zakresu: {liczby_nieparzyste}")

# Zadanie 3
# Użytkownik wpisuje dwie liczby. Wydrukuj wszystkie liczby parzyste z podanego zakresu.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczby_parzyste = []
for liczba in range(liczba_1, liczba_2 + 1):
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)
print(f"Liczby nieparzyste z podanego zakresu: {liczby_parzyste}")

# Zadanie 4
# Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby z podanego zakresu w kolejności malejącej.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczby = []
for liczba in range(liczba_1, liczba_2 + 1):
    liczby.append(liczba)
print(f"Liczby z podanego zakresu w kolejnosci malejacej: {liczby[::-1]}")

# Zadanie 5
# Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby nieparzyste z podanego zakresu. Jeśli punkty końcowe i początkowe zakresu są nieprawidłowe, znormalizuj je. 
# Załóżmy, że użytkownik wpisał 33 i 13, normalizacja przypisze 13 do początku i 33 do końca zakresu.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczby_nieparzyste = []
if liczba_1 < liczba_2:
    for liczba in range(liczba_1, liczba_2 + 1):
        if liczba % 2 != 0:
            liczby_nieparzyste.append(liczba)
else:
    for liczba in range(liczba_2, liczba_1 + 1):
        if liczba % 2 != 0:
            liczby_nieparzyste.append(liczba)
print(f"Liczby nieparzyste z podanego zakresu: {liczby_nieparzyste}")