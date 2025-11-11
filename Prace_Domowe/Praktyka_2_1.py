# Praktyka 2.1

# Zadanie 1
# Użytkownik wpisuje liczbę. Sprawdź czy jest ona parzysta czy nieparzysta. 
# Jeśli liczba jest parzysta, wypisz liczbę i tekst "Liczba parzysta". Jeśli liczba jest nieparzysta, wypisz liczbę i tekst "Liczba nieparzysta".

liczba = int(input("Podaj liczbe: "))
if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta.")
else:
    print(f"Liczba {liczba} jest nieparzysta.")

# Zadanie 2
# Użytkownik wpisuje liczbę. Sprawdź, czy jest ona wielokrotnością liczby 7. Jeśli tak, wypisz liczbę i tekst "Twoja liczba jest wielokrotnością liczby 7". 
# Jeśli nie, wypisz liczbę i tekst "Twoja liczba nie jest wielokrotnością 7".

liczba = int(input("Podaj liczbe: "))
if liczba % 7 == 0:
    print(f"{liczba}\tTwoja liczba jest wielokrotnością liczby 7")
else:
    print(f"{liczba}\tTwoja liczba nie jest wielokrotnością liczby 7")

# Zadanie 3
# Użytkownik wpisuje dwie liczby. Znajdź maksimum z dwóch liczb i wypisz je.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
if liczba_1 > liczba_2:
    print(f"Najwyzsza z podanych liczb to {liczba_1}")
else:
    print(f"Najwyzsza z podanych liczb to {liczba_2}")


# Zadanie 4
# Użytkownik wpisuje dwie liczby. Znajdź minimum z dwóch liczb i wypisz je.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
if liczba_1 < liczba_2:
    print(f"Najnizsza z podanych liczb to {liczba_1}")
else:
    print(f"Najnizsza z podanych liczb to {liczba_2}")


# Zadanie 5
# Użytkownik wpisuje dwie liczby. Na podstawie wyboru użytkownika wypisz wynik sumy, różnicy, iloczynu tych liczb lub ich średnią arytmetyczną.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
suma = liczba_1 + liczba_2
roznica = liczba_1 - liczba_2
iloczyn = liczba_1 * liczba_2
srednia = (liczba_1 + liczba_2) / 2
wybor = int(input("Jakie dzialanie chcesz przeprowadzic?\n1 - SUMA\n2 - ROZNICA\n3 - ILOCZYN\n4 - SREDNIA\nWybor: "))
if wybor == 1:
    print(f"Suma liczb {liczba_1} i {liczba_2} wynosi: {suma}")
elif wybor == 2:
    print(f"Roznica liczb {liczba_1} i {liczba_2} wynosi: {roznica}")
elif wybor == 3:
    print(f"Iloczyn liczb {liczba_1} i {liczba_2} wynosi: {iloczyn}")
elif wybor == 4:
    print(f"Srednia liczb {liczba_1} i {liczba_2} wynosi: {srednia}")
else:
    print("Nie ma takiej opcji, wybierz dzialanie z zakresu 1-4.")