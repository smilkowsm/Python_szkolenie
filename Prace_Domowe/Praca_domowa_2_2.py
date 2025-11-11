# Praca domowa 2.2 Rozgałęzienia

# Zadanie 1
# Użytkownik wpisuje liczbę od 1 do 7 reprezentującą dzień tygodnia. Wypisz jego nazwę. Na przykład, jeśli liczba wynosi 1, należy wyświetlić "poniedziałek"; jeśli 2, należy wyświetlić "wtorek" itd.

while True:
    dzien = int(input("Podaj liczbe od 1 do 7: "))
    if dzien == 1:
        print("Poniedzialek")
        break
    elif dzien == 2:
        print("Wtorek")
        break
    elif dzien == 3:
        print("Sroda")
        break
    elif dzien == 4:
        print("Czwartek")
        break
    elif dzien == 5:
        print("Piatek")
        break
    elif dzien == 6:
        print("Sobota")
        break
    elif dzien == 7:
        print("Niedziela")
        break
    else:
        print("Wpisz liczbe z zakresu od 1 do 7!")
        continue


# Zadanie 2
# Użytkownik wpisuje liczbę od 1 do 12, która reprezentuje miesiąc. Wydrukuj jego nazwę. Na przykład, jeśli liczba wynosi 1, należy wyświetlić "styczeń"; jeśli 2, należy wyświetlić "luty" itd.

while True:
    miesiac = int(input("Podaj liczbe od 1 do 12: "))
    miesiace = {1 : "Styczen", 2 : "Luty", 3 : "Marzec", 4 : "Kwiecien", 5 : "Maj", 6 : "Czerwiec", 7 : "Lipiec", 8 : "Sierpien", 9 : "Wrzesien", 10 : "Pazdziernik", 11 : "Listopad", 12 : "Grudzien"}
    if miesiac >= 1 and miesiac <= 12:
        print(miesiace[miesiac])
        break
    else:
        print("Wybierz liczbe z wlasciwego zakresu!")
        continue

# Zadanie 3
# Użytkownik wpisuje liczbę. Jeśli liczba jest większa od 0, wypisz "Your number is positive"; jeśli jest mniejsza od zera, wypisz "Your number is negative"; jeśli jest równa 0, wypisz "Your number is equal to zero".

number = float(input("Type a number: "))
if number > 0:
    print("Your number is positive")
elif number < 0:
    print("Your number is negative")
else:
    print("Your number is equal to zero")

# Zadanie 4
# Użytkownik wpisuje dwie liczby. Sprawdź, czy liczby te są równe. Jeśli nie, wypisz je w kolejności rosnącej.

liczba_1 = int(input("Wpisz pierwsza liczbe: "))
liczba_2 = int(input("Wpisz druga liczbe: "))
if liczba_1 == liczba_2:
    print("Liczby sa rowne")
elif liczba_1 > liczba_2:
    print(liczba_2, liczba_1)
else:
    print(liczba_1, liczba_2)