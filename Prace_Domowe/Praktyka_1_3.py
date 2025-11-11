# Praktyka 1.3

# Zadanie 1
# Użytkownik wpisuje dwucyfrową liczbę. Na przykład 26. Wyświetl wartość pierwszej i drugiej cyfry w różnych wierszach.

while True:
    liczba = int(input("Wpisz dwucyfrowa liczbe: "))
    if len(liczba) != 2:
        print("Liczba musi miec DWIE cyfry!")
        continue
    else:
        liczba = str(liczba)
        print(f"{liczba[0]}\n{liczba[1]}")
        break


# Zadanie 2
# Użytkownik wpisuje trzycyfrową liczbę. Na przykład 891. Wypisz wartość pierwszej, drugiej i trzeciej cyfry w nowym wierszu. Wypisz również sumę tych liczb w nowym wierszu.

while True:
    liczba = int(input("Wpisz trzycyfrowa liczbe: "))
    if liczba < 100 or liczba > 999:
        print("Liczba musi miec TRZY cyfry!")
        continue
    else:
        break
liczba = str(liczba)
print(f"{liczba[0]}\n{liczba[1]}\n{liczba[2]}")
print(int(liczba[0]) + int(liczba[1]) + int(liczba[2]))


# Zadanie 3
# Użytkownik wpisuje dwie cyfry. Utwórz liczbę zawierającą te cyfry. Jeśli wpisane cyfry to 9 i 7, utworzoną liczbą będzie 97.

liczba_1 = input("Wpisz pierwsza liczbe: ")
liczba_2 = input("Wpisz druga liczbe: ")
nowa_liczba = liczba_1 + liczba_2
nowa_liczba = int(nowa_liczba)
print(f"Nowo utworzona liczba to: {nowa_liczba}")

# Zadanie 4
# Użytkownik wpisuje temperaturę w stopniach Celsjusza. Przelicz ją na Fahrenheita i wyświetl wynik na ekranie.

Celsjusz = float(input("Wpisz temperature w stopniach C: "))
Farenheit = Celsjusz * 1.8 + 32
print(f"{Celsjusz} stopni Celsjusza jest rowne {Farenheit} stopniom w skali Farenheita.")
