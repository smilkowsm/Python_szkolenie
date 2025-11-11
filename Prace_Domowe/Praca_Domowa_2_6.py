# Praca Domowa 2.6

# Zadanie 1
# Napisz program, który żąda dwóch liczb całkowitych x i y, a następnie oblicza i wypisuje wartość x podniesioną do potęgi y.

liczba_x = int(input("Podaj liczbe x: "))
liczba_y = int(input("Podaj liczbe y: "))
potega = 1
for liczba in range(liczba_y):
    potega *= liczba_x

print(f"{liczba_x} do potegi {liczba_y} wynosi: {potega}")


# Zadanie 2
# Policz liczbę liczb całkowitych z zakresu od 100 do 999, które mają dwie identyczne cyfry.

zakres = [liczba for liczba in range(100, 1000)]
nowy_zakres = []
zakres_dwie_cyfry = set()
for element in zakres:
    element = str(element)
    nowy_zakres.append(element)

# Ponizszy przyklad wyswietli liczby, ktore maja TYLKO 2 identyczne cyfry:
for element in nowy_zakres:
    if element[0] == element[1] and element[0] != element[2] or element[0] == element[2] and element[0] != element[1] or element[1] == element[2] and element[1] != element[0]:
        zakres_dwie_cyfry.add(element)
print(f"W zakresie od 100 do 999 jest {len(zakres_dwie_cyfry)} liczb, ktore maja dokladnie dwie identyczne cyfry.")


# Zadanie 3
# Policz liczbę liczb całkowitych z zakresu od 100 do 9999, które mają różne cyfry.

zakres = [liczba for liczba in range(100, 10000)]
nowy_zakres = []
zakres_rozne = []
for element in zakres:
    element = str(element)
    nowy_zakres.append(element)
for element in nowy_zakres:
    if len(element) == 3 and element[0] != element[1] and element[0] != element[2] and element[1] != element[2]:
        zakres_rozne.append(element)
    if len(element) == 4 and element[0] != element[1] and element[0] != element[2] and element[0] != element[3] and element[1] != element[2] and element[1] != element[3] and element[2] != element[3]:
        zakres_rozne.append(element)
print(f"W zakresie od 100 do 9999 jest {len(zakres_rozne)} liczb, ktore maja dokladnie dwie identyczne cyfry.")


# Zadanie 4
# Użytkownik wpisuje wartość całkowitą. Usuń wszystkie 3 i 6 z tej liczby całkowitej i wypisz ją.

liczba = int(input("Wpisz liczbe: "))
liczba = str(liczba)
wartosc = ""
for element in liczba:
    if element != "3" and element != "6":
        wartosc += element
print(wartosc)
