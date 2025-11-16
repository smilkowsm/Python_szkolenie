def nazwa_funkcji():
    pass # Pominie funkcje/warunek itp. i nie wywali bledu podczas odpaleniu kodu, przydaje sie jesli chcemy do czegos wrocic pozniej

if 2 > 3:
    pass # Nie wywali bledu, ze brakuje kodu

def funkcja():
    if 2 < 3:
        pass
    print("Funkcja o nazwie ''funkcja")
    return 

funkcja() # Funkcja zwroci printa, bo pass jest we wcieciu

def funkcja_2():
    if 2 < 3:
        wynik = "2 jest mniejsze od 3"
    print("Funkcja o nazwie ''funkcja")
    return wynik

funkcja_2()
print(funkcja_2()) # W tym wypadku print zwroci to co wskazuje return

def funkcja_3():
    if 2 < 3:
        wynik = "2 jest mniejsze od 3"
        return wynik # return dziala rowniez jak break w trakacie wykonywania funkcji, zamknie cala funkcje
    print("Funkcja o nazwie ''funkcja")
    return "3 jest mniejsze od 2"

funkcja_3()
print(funkcja_3()) 

def dodaj_dwie_liczby(liczba_1, liczba_2):
    print("To jest funkcja o nazwie 'dodaj_dwie_liczby'")
    print(f"Wynik dodawania:\n{liczba_1} + {liczba_2} = {liczba_1 + liczba_2}")

dodaj_dwie_liczby(5, 7)
dodaj_dwie_liczby(125, -25)


liczba_1_uzytkownika = float(input("Podaj pierwsza liczbe: "))
liczba_2_uzytkownika = float(input("Podaj druga liczbe: "))

dodaj_dwie_liczby(liczba_1_uzytkownika, liczba_2_uzytkownika)

def odejmowanie_2_liczb(liczba_1, liczba_2):
    print("To jest funkcja o nazwie odejmowanie_2_liczb")
    return liczba_1 - liczba_2
    print("Ten print nie zostanie wywolany, bo jest return")

wynik_odejmowania = odejmowanie_2_liczb(4, 5)

print("Zmienna wynik_odejmowania:", wynik_odejmowania)
print("Funkcja odejmowanie_2_liczb:", odejmowanie_2_liczb(5,4))
odejmowanie_2_liczb(10, 3)

def nowa_funkcja():
    return "Wiadomosc z funkcji"

def nowa_funkcja(liczba):
    return f"Wiadomosc z funkcji {liczba}"

nowa_funkcja(5) # Funkcja zwrocila nam czesc po returnie (NIE WYSWIETLA)

wartosc_z_funkcji = nowa_funkcja(12)
print(wartosc_z_funkcji)