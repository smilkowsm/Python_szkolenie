# Praktyka 2.5

# Zadanie 1
# Użytkownik wpisuje dwie liczby. Znajdź sumę i średnią liczb z podanego zakresu.

liczba_1 = int(input("Podaj pierwsza liczbe: "))
liczba_2 = int(input("Podaj druga liczbe: "))
suma = 0
ilosc_liczb = 0
for i in range (liczba_1, liczba_2 + 1):
    suma = suma + i
    ilosc_liczb += 1
srednia = suma / ilosc_liczb
print(f"Suma liczb z podanego zakresu wynosi: {suma}, srednia liczb z podanego zakresu wynosi: {srednia}")

# Zadanie 2
# Użytkownik wpisuje liczbę. Oblicz iloraz liczby. Na przykład, jeśli użytkownik wpisze 3, to iloraz wynosi 1*2*3 = 6.
# Wzór na obliczenie ilorazu: n! = 1*2*3...*n, gdzie n jest liczbą zdefiniowaną przez użytkownika.

liczba = int(input("Podaj liczbe: "))
wynik = 1

for i in range(1, liczba + 1):
    wynik = wynik * i
print(wynik)

# Zadanie 3
# Użytkownik wpisuje długość linii. Wydrukuj poziomą linię składającą się z * o podanej długości.
# Na przykład, jeśli wpisana liczba to 7, wynik będzie następujący: *******.

dlugosc = int(input("Podaj dlugosc linii: "))
while dlugosc:
    print("*", end="")
    dlugosc -= 1

# Zadanie 4
# Użytkownik wpisuje długość linii i symbol, który ma ją wypełnić. Wydrukuj poziomą linię utworzoną z wpisanego symbolu o określonej długości.
# Jeśli wpisana liczba i symbol to 5 i &, wynik będzie następujący: &&&&&.

dlugosc = int(input("Podaj dlugosc linii: "))
symbol = input("Podaj symbol: ")
while dlugosc:
    print(symbol, end="")
    dlugosc -= 1
