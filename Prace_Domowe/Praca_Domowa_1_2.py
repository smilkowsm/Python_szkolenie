# Praca Domowa 1.2

# Zadanie 1
# Użytkownik wpisuje trzy liczby. Znajdź sumę i iloczyn tych liczb. Wyświetl wynik na ekranie.

liczba_1 = int(input("Wpisz pierwsza liczbe: "))
liczba_2 = int(input("Wpisz druga liczbe: "))
liczba_3 = int(input("Wpisz trzecia liczbe: "))
suma = liczba_1 + liczba_2 + liczba_3
iloczyn = liczba_1 * liczba_2 * liczba_3
print("Suma podanych liczb to:", suma)
print("Iloczyn podanych liczb to:", iloczyn)

# Zadanie 2
# Użytkownik wpisuje trzy liczby. Pierwsza liczba to miesięczne wynagrodzenie, druga liczba to kwota miesięcznej raty kredytu, a trzecia to opłata za usługi komunalne.
# Wyświetl kwotę, jaką użytkownik będzie dysponował po dokonaniu wszystkich płatności.

wynagrodzenie = int(input("Wpisz kwote wynagrodzenia: "))
rata = int(input("Wpisz kwote rat: "))
oplata = int(input("Wpisz kwote oplat: "))
reszta = wynagrodzenie - (rata + oplata)
print("Po dokonaniu wszystkich oplat, zostanie ci:", reszta)

# Zadanie 3
# Napisz program obliczający pole powierzchni rombu. Użytkownik wpisuje długość jego dwóch przekątnych.

przekatna_1 = int(input("Podaj dlugosc pierwszej przekatnej: "))
przekatna_2 = int(input("Podaj dlugosc drugiej przekatnej: "))
pole = (przekatna_1 * przekatna_2) / 2
print("Pole powierzchni rombu wynosi:", pole)

# Zadania 4
# Wydrukuj cytat: "Być albo nie być" w różnych wierszach.

print("to be\nor not\nto be")

# Zadanie 5
# Wydrukuj cytat: "Życie jest tym, co dzieje się, gdy jesteś zajęty robieniem innych planów" Johna Lennona w różnych liniach.

print('"Life is what happens\n\twhen\n\t\tyou\'re busy making other plans"\n\t\t\tJohn Lennon.')