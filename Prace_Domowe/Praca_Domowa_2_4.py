# Praca domowa 2.4 Pętle

# Zadanie 1
# Użytkownik wpisuje dwie liczby (początek i koniec zakresu). Przeanalizuj wszystkie liczby w tym zakresie w następujący sposób: jeśli liczba jest wielokrotnością 7, wypisz ją.

poczatek = int(input("Podaj poczatek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))
for i in range(poczatek, koniec + 1):
    if i % 7 == 0:
        print(f"{i} jest wielokrotnoscia liczby 7")

# Zadanie 2
# Użytkownik wpisuje dwie liczby (punkt początkowy i końcowy zakresu). Przeanalizuj wszystkie liczby w tym zakresie. Wydrukuj następujące wyniki:
# Wszystkie liczby w zakresie;
# Wszystkie liczby w zakresie w porządku malejącym;
# Wszystkie liczby będące wielokrotnościami liczby 7;
# Ile liczb jest wielokrotnością liczby 5.

poczatek_zakresu = int(input("Podaj poczatek zakresu: "))
koniec_zakresu = int(input("Podaj koniec zakresu: "))
zakres = [liczba for liczba in range(poczatek_zakresu, koniec_zakresu + 1)]
wielokrotnosc_5 = 0
wielokrotnosc_7 = []
print(f"Liczby w podanym zakresie: {zakres}")
print(f"Liczby w podanym zakresie w kolejnosci malejacej: {zakres[::-1]}")
for liczba in zakres:
    if liczba % 7 == 0:
        wielokrotnosc_7.append(liczba)
for liczba in range(poczatek_zakresu, koniec_zakresu + 1):
    if liczba % 5 == 0:
        wielokrotnosc_5 += 1
print(f"Liczby w zakresie bedace wielokrotnoscia liczby 7: {wielokrotnosc_7}")
print(f"Ilosc liczb w zakresie bedacych wielokrotnoscia liczby 5: {wielokrotnosc_5}")

# Zadanie 3
# Użytkownik wpisuje dwie liczby (punkt początkowy i końcowy zakresu). Przeanalizuj wszystkie liczby w tym zakresie. Wynik powinien być zgodny z poniższymi regułami.
# Jeśli liczba jest wielokrotnością 3 (podzielna przez 3 bez reszty), wypisz słowo Fizz. Jeśli jest wielokrotnością 5, wypisane zostanie słowo Buzz. Jeśli jest wielokrotnością 3 i 5, zostanie wyświetlone słowo Fizz Buzz. 
# Jeśli liczba nie jest wielokrotnością 3 lub 5, wypisana zostanie sama liczba.

zakres_poczatek = int(input("Podaj poczatek zakresu: "))
zakres_koniec = int(input("Podaj koniec zakresu: "))
zakres_liczb = [liczby for liczby in range(zakres_poczatek, zakres_koniec + 1)]

for liczba in zakres_liczb:
    if liczba % 3 == 0 and liczba % 5 != 0:
        print("Fizz")
    elif liczba % 5 == 0 and liczba % 3 != 0:
        print("Buzz")
    elif liczba % 3 == 0 and liczba % 5 == 0:
        print("Fizz Buzz")
    else:
        print(liczba)