print("|___________________|")
print("|       Menu        |")
print("|                   |")
print("|1.Dodaj            |")
print("|2.Odejmij          |")
print("|3.Podziel          |")
print("|4.Losowa           |")
print("|0.Koniec___________|")

import random
import lekcja_12_2_moduly
lekcja_12_2_moduly.pokaz # Jesli importujemy cala lekcje to musimy wywolac funkcje po kropce
print("Funkcja pokaz w pliku 12_1")

from lekcja_12_2_moduly import pokaz
pokaz() # Jesli importujemy konkretna funkcje, to wywolujemy ja bezposrednio

import lekcja_12_2_moduly as l12m # Nadajemy lekcja_12_2_moduly alias o nazwie l12m


wybor = int(input("Jaki jest twoj wybor? "))

while wybor != 0:
    liczba_1 = int(input("Podaj pierwsza liczbe: "))
    liczba_2 = int(input("Podaj druga liczbe: "))
    if wybor == 1:
        suma = liczba_1 + liczba_2
        print(f"Wynik dodawania liczby {liczba_1} i {liczba_2} to {suma}")
        break
    elif wybor == 2:
        roznica = liczba_1 - liczba_2
        print(f"Wynik odejmowania liczby {liczba_1} i {liczba_2} to {roznica}")
        break
    elif wybor == 3:
        iloraz = liczba_1 / liczba_2
        print(f"Wynik dzielenia liczby {liczba_1} i {liczba_2} to {iloraz}")
        break
    elif wybor == 4:
        losowa_liczba = random.randint(int(liczba_1), int(liczba_2))
        print(f"Wylosowana liczba z przedzialu od {liczba_1} do {liczba_2} to {losowa_liczba}")
    else:
        print("Wybierz jedna z dostepnych opcji")
        continue
print("KONIEC")

from random import choice


wybor = None
while wybor != "0":
    lista = ["Kot", "Pies", "List"]
    wybor = input(f"Druga petla {choice(lista)}")
print("KONIEC")


