# Praktyka 1.2 Wprowadzenie do Pythona

# Zadanie 1
# Wydrukuj cytat "Nic nie zadziała, dopóki tego nie zrobisz" w różnych wierszach.
print("Nothing\nwill work\nunless you do")

# Zadanie 2
# Wydrukuj cytat "Każdy, kto przestaje się uczyć, jest stary, czy to w wieku dwudziestu, czy osiemdziesięciu lat" Henry'ego Forda w różnych wierszach.
print('"Anyone who\n\tstops\n\t\tlearning is old,\n\t\t\twhether at twenty or eighty"\n\t\t\t\tHenry Ford')

# Zadanie 3
# Użytkownik wpisuje dwie liczby. Znajdź sumę, różnicę i iloczyn tych liczb. Wyświetl wynik na ekranie.
liczba_1 = int(input("Wpisz pierwsza liczbe: "))
liczba_2 = int(input("Wpisz druga liczbe: "))
suma = liczba_1 + liczba_2
roznica = liczba_1 - liczba_2
iloczyn = liczba_1 * liczba_2
print(f"Wynik dodawania liczb to {suma}, odejmowania to {roznica}, a mnozenia to {iloczyn}.")

# Zadanie 4
# Użytkownik wpisuje dwie liczby. Pierwsza liczba jest wartością, a druga jest procentem do obliczenia. Załóżmy, że wpisaliśmy 50 i 10. Wyświetlona liczba powinna wynosić 10% z 50. Wynik: 5.
num_1 = int(input("Wpisz pierwsza liczbe: "))
num_2 = int(input("Wpisz druga liczbe: "))
wynik = num_2 * num_1 / 100
print(f"{num_2}% z {num_1} to {wynik}")

# Zadanie 5
# Napisz program obliczający pole prostokąta. Użytkownik wpisuje szerokość i wysokość prostokąta.
szerokosc = int(input("Podaj szerokosc prostokata: "))
wysokosc = int(input("Podaj wysokosc prostokata: "))
pole = szerokosc * wysokosc
print(f"Pole prostokata wynosi {pole}")
