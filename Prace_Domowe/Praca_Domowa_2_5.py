# Praca Domowa 2.5

# Zadanie 1
# Użytkownik wpisuje dwie liczby. Znajdź sumę wszystkich liczb parzystych, nieparzystych i wielokrotności 9 w podanym zakresie, a także średnią arytmetyczną każdej z grup.

liczba_1 = int(input("Wpisz pierwsza liczbe: "))
liczba_2 = int(input("Wpisz druga liczbe: "))
zakres_liczb = []
liczby_parzyste = []
liczby_nieparzyste = []
wielokrotnosci_9 = []
for liczba in range(liczba_1, liczba_2 + 1):
    zakres_liczb.append(liczba)
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)
    if liczba % 9 == 0:
        wielokrotnosci_9.append(liczba)
    if liczba % 2 != 0:
        liczby_nieparzyste.append(liczba)

srednia_parzyste = sum(liczby_parzyste) / len(liczby_parzyste)
srednia_nieparzyste = sum(liczby_nieparzyste) / len(liczby_nieparzyste)

print(f"Liczby z zakresu od {liczba_1} do {liczba_2}: {zakres_liczb}")
print("*" * 50)
print(f"Liczby parzyste z zakresu od {liczba_1} do {liczba_2}: {liczby_parzyste}")
print(f"Suma wszystkich liczb parzystych z wybranego zakresu to: {sum(liczby_parzyste)}")
print(f"Srednia arytmetyczna zakresu liczb parzystych wynosi {srednia_parzyste}")
print("*" * 50)
print(f"Liczby nieparzyste z zakresu od {liczba_1} do {liczba_2}: {liczby_nieparzyste}")
print(f"Suma wszystkich liczb nieparzystych z wybranego zakresu to: {sum(liczby_nieparzyste)}")
print(f"Srednia arytmetyczna zakresu liczb nieparzystych wynosi {srednia_nieparzyste}")
print("*" * 50)
if len(wielokrotnosci_9) != 0:
    srednia_wielokrotnosci = sum(wielokrotnosci_9)/ len(wielokrotnosci_9)
    print(f"Liczby bedace wielokrotnoscia liczby 9 z zakresu od {liczba_1} do {liczba_2}: {wielokrotnosci_9}")
    print(f"Suma wszystkich liczb wielokrotnosci 9 z wybranego zakresu to: {sum(wielokrotnosci_9)}")
    print(f"Srednia arytmetyczna zakresu liczb wielokrotnosci 9 wynosi {srednia_wielokrotnosci}")
    print("*" * 50)
else:
    print("Brak wielokrotnosci liczby 9 w podanym zakresie.")
    print("*" * 50)

# Zadanie 2
# Użytkownik wpisuje długość linii i symbol, który ma ją wypełnić. Wydrukuj pionową linię utworzoną z wpisanego symbolu o określonej długości.
# Na przykład, jeśli wpisana liczba i symbol to 5 i %, wynik będzie następujący:
#%
#%
#%
#%
#%

dlugosc = int(input("Podaj dlugosc linii: "))
symbol = input("Podaj symbol: ")
while dlugosc > 0:
    print(f"{symbol}")
    dlugosc -= 1

# Zadanie 3
# Użytkownik wpisuje liczbę. Jeśli liczba jest większa od 0, wypisywane jest "Twoja liczba jest dodatnia"; jeśli jest mniejsza od zera, wypisywane jest "Twoja liczba jest ujemna"; jeśli jest równa 0, wypisywane jest "Twoja liczba jest równa zero". 
# Gdy użytkownik wpisze 7, program zatrzyma się i wypisze "Good bye!".

while True:
    liczba = int(input("Podaj liczbe: "))
    if liczba == 7:
        print("Good bye!")
        break
    elif liczba > 0 and liczba != 7:
        print("Twoja liczba jest dodatnia")
    elif liczba < 0:
        print("Twoja liczba jest ujemna")
    else:
        print("Twoja liczba jest równa zero")

# Zadanie 4
# Użytkownik wpisuje liczby. Program musi obliczyć ich sumę oraz znaleźć maksimum i minimum. Gdy użytkownik wpisze 7, program zatrzymuje się i wypisuje "Good bye!".

zbior_liczb = []
liczba = int(input("Podaj liczbe: "))
zbior_liczb.append(liczba)
while True:
    if liczba == 7:
        print("Good bye!")
        break
    else:
        kolejna_liczba = int(input("Podaj kolejna liczbe: "))
        if kolejna_liczba == 7:
            print("Good bye!")
            break
        else:
            zbior_liczb.append(kolejna_liczba)
            print(f"Podane liczby: {zbior_liczb}")
            print(f"Suma wszystkich podanych liczb wynosi: {sum(zbior_liczb)}\nNajwyzsza z podanych liczb to: {max(zbior_liczb)}\nNajnizsza z podanych liczb to: {min(zbior_liczb)}")
            print("*" * 50)