# Funkcja input() pobiera dane od uzytkowika, mozna je przypisac do zmiennej
imie = input("Podaj sowje imie: ")
print("Witaj, ", imie)

#input traktuje wszystkie wpisane wartosci domyslnie jako string - trzeba zmieniac typ danych jesli chcemy uzyskac inny

wynik = "niedowaga"
wynik_2 = "nadwaga"

waga = float(input("Wpisz swoja wage (kg): "))
wzrost = float(input("Wpisz swoj wzrost (m): "))
print("Typ zmiennej waga:", type(waga))
bmi = waga / wzrost ** 2

# Jesli warunek if sie spelni, reszta nie bedzie sprawdzana
if bmi < 18.5:
    print(wynik)
elif bmi > 25.5:
    print(wynik_2)
else:
    print("Jest ok")

print("Do zobaczenia!")

# Uzywanie if'ow jest dobre jesli chcemy aby zostaly wykonane wiecej niz 1 porownanie
# Kazde z ponizszych zostanie wykonane, nawet jesli 1 warunek sie spelni
if bmi < 18.5:
    wynik_3 = "niedowaga"
    print(wynik_3)
if bmi >= 18.5 and bmi < 25: # mozemy zapisac jako: 18.5 <= bmi < 25:
    wynik_3 = "w normie"
    print(wynik_3)
if bmi >= 25:
    wynik_3 = "nadwaga"
    print(wynik_3)

# SHIFT + TAB - przesuwa zaznaczony tekst do lewej

# Lepiej nie powtarzc wszedie printa
if bmi < 18.5:
    wynik = "niedowaga"
elif bmi == 25.5:
    wynik = "nadwaga"
else:
    wynik = "w normie"
    if imie == "Adam":
        print("Hej, ", imie)
print(wynik)

