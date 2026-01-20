# Praca domowa 2.3 Rozgałęzienia

# Zadanie 1
# Użytkownik wpisuje liczbę z zakresu od 1 do 100. Jeśli liczba jest wielokrotnością 3 (podzielna przez 3 bez reszty), wypisz słowo Fizz. 
# Jeśli liczba jest wielokrotnością 5, wypisane zostanie słowo Buzz. Jeśli słowo jest wielokrotnością 3 i 5, wypisane zostanie słowo Fizz Buzz. 
# Jeśli słowo nie jest wielokrotnością 3 i 5, wypisana zostanie liczba.
# Jeśli użytkownik wpisał liczbę spoza zakresu, wypisany zostanie komunikat o błędzie.

while True:
    number = int(input("Podaj liczbe z zakresu od 1 do 100: "))
    if number >= 1 and number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
            break
        elif number % 3 != 0 and  number % 5 == 0:
            print("Buzz")
            break
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")
            break
        else:
            break
    else:
        print("Podana liczba nie miesci sie w zakresie od 1 do 100!")
        continue
    
# Zadanie 2
# Napisz program, który na polecenie użytkownika podniesie wpisaną liczbę do potęgi od 0 do 7.

liczba = int(input("Wpisz liczbe: "))
potega = int(input("Do ktorej potegi (od 0 do 7) chcesz podniesc liczbe? "))
if potega >= 0 and potega <= 7:
    wynik = liczba ** potega
    print(f"Liczba {liczba} podniesiona do {potega} potegi wynosi {wynik}")
else:
    print("Wybrales niepoprawny zakres!")

# Zadanie 3
# Napisz program obliczający koszt połączenia dla różnych operatorów telefonii komórkowej. 
# Użytkownik wpisuje czas połączenia i wybiera operatorów dla połączeń wychodzących i przychodzących. Wydrukuj koszt.

while True:
    czas_polaczenia = float(input("Wpisz czas polaczenia(min): "))
    operator = input("Wybierz operatora(PLAY | PLUS | ORANGE): ")
    operator = operator.upper()
    play = 0.19
    plus = 0.49
    orange = 0.79

    if operator == "PLAY":
        print(f"Koszt za minute polaczenia w sieci PLAY to {play}, za polaczenie dlugosci {czas_polaczenia} min zaplacisz {czas_polaczenia * play} zl")
        break
    elif operator == "PLUS":
        print(f"Koszt za minute polaczenia w sieci PLUS to {plus}, za polaczenie dlugosci {czas_polaczenia} min zaplacisz {czas_polaczenia * plus} zl")
        break
    elif operator == "ORANGE":
        print(f"Koszt za minute polaczenia w sieci ORANGE to {orange}, za polaczenie dlugosci {czas_polaczenia} min zaplacisz {czas_polaczenia * orange} zl")
        break
    else:
        print("Nie ma takiego operatora!")
        continue

# Zadanie 4
# Pensja sprzedawcy wynosi 200 USD + procent od sprzedaży w następujący sposób: do 500 USD - 3%, od 500 do 1000 - 5%, powyżej 1000 - 8%. 
# Użytkownik wpisuje wartość sprzedaży dla trzech sprzedawców. Określ ich wynagrodzenie, wybierz najlepszego sprzedawcę, przyznaj mu premię w wysokości 200 USD i wydrukuj wynik.

pensja = 200
sprzedaz_mala = 0.03
sprzedaz_srednia = 0.05
sprzedaz_duza = 0.08
sprzedaz_1 = float(input("Wprowadz wartosc sprzedazy dla 1 sprzedawcy: "))
sprzedaz_2 = float(input("Wprowadz wartosc sprzedazy dla 2 sprzedawcy: "))
sprzedaz_3 = float(input("Wprowadz wartosc sprzedazy dla 3 sprzedawcy: "))
lista_sprzedawcow = {"sprzedawca_1": sprzedaz_1, "sprzedawca_2" : sprzedaz_2, "sprzedawca_3" : sprzedaz_3}
for sprzedawca in lista_sprzedawcow:
    if sprzedawca <= 500:
        print(f"{sprzedawca} zrobil wynik {pensja + sprzedawca * sprzedaz_mala}")
    elif sprzedawca > 500 and sprzedawca <= 1000:
        print(f"{sprzedawca} zrobil wynik {pensja + sprzedawca * sprzedaz_srednia}")
    elif sprzedawca > 1000:
        print(f"{sprzedawca} zrobil wynik {pensja + sprzedawca * sprzedaz_duza}")
