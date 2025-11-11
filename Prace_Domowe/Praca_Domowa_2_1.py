# Praca Domowa 2.1

# Zadanie 1
# Użytkownik wpisuje trzy liczby. Program wypisuje sumę lub iloczyn tych liczb w zależności od wyboru użytkownika.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczba_3 = int(input("Podaj trzecia liczbe: "))
suma = liczba_1 + liczba_2 + liczba_3
iloczyn = liczba_1 * liczba_2 * liczba_3
wybor = int(input("Wcisnij 1 aby obliczyc sume, lub 2 aby obliczyc iloczyn: "))
if wybor == 1:
    print(f"Suma liczb wynosi: {suma}")
elif wybor == 2:
    print(f"Iloczyn liczb wynosi: {iloczyn}")
else:
    print("Musisz wybrac 1 lub 2!")

# Zadanie 2
# Użytkownik wpisuje trzy liczby. W zależności od wyboru użytkownika, program wypisuje maksimum z trzech, minimum z trzech lub średnią arytmetyczną z trzech liczb.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
liczba_3 = int(input("Podaj trzecia liczbe: "))
lista = []
lista.append(liczba_1)
lista.append(liczba_2)
lista.append(liczba_3)
najwieksza = max(lista)
najmniejsza = min(lista)
srednia = (liczba_1 + liczba_2 + liczba_3) / 3
wybor_uzytkownika = int(input("Wybierz 1 aby otrzymac maksimum, 2 aby otrzymac minimum, lub 3 aby otrzymac srednia:  "))
if wybor_uzytkownika == 1:
    print(f"Najwieksza liczba to: {najwieksza}")
elif wybor_uzytkownika == 2:
    print(f"Najmniejsza liczba to: {najmniejsza}")
else:
      print(f"Srednia liczb to: {srednia}")

# Zadanie 3
# Użytkownik wpisuje liczbę metrów. W zależności od wyboru użytkownika program przelicza metry na mile, cale lub jardy.

metry = float(input("Podaj liczbe metrow: "))
mile = metry / 1609.344
cale = metry * 39.3701
jardy = metry / 0.9144

print(f"{metry} metrow to:\n{mile} mil\n{cale} cali\n{jardy} jardow")
