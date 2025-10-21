lista = ["to", "jest", "przykladowy", "tekst", 5, 10, 15, 25, 30]
print("To jest zawartosc zmiennej lista:", lista)
print("To jest element z listy o indeksie 1:", lista[1]) # Mozemy wyciagac z listy poszczegolne elementy, liczenie zawsze zaczyna sie od 0
print("To jest ostatni element z listy o indeksie -1:", lista[-1])

lista[2] = "ala ma kota"
print("Element z listy po zmianie. Indeks 2:", lista[2])

print("To sa 2 srodkowe elementy z listy:", lista[1:3]) # mozemy podac zakres ktory chcemy wyciagnac, 1:3, a nie 1:2 bo ostatnia podana liczba sie nie wlicza
print("To jest co 2 element listy:", lista[1:-2:2]) # wyswietli co 2gi element (poczatek zakresu:koniec zakresu ktory sie nie wlicza:co ile)
print("Elementy listy od tylu:", lista[::-1])
print("co 2 element listy od tylu:", lista[::-2])
print("\nCala lista:", lista[::])
print("Lista bez ostatniego elementu:", lista[0:-1]) # To samo co nizej
print("Lista bez ostatniego elementu:", lista[:-1]) # To samo co wyzej
print("Lista bez pierwszego elelmentu", lista[1:])

print("\nIlosc elementow w liscie:", len(lista)) # len liczy elementy
print(len("Python"))
print("Python", "Kolejny " + "tekst", sep = "++", end = "||" ) # sep i end (parametry nazwane) zawsze stawiamy na koncu default: sep=" " | end="\n"
# sep to separator, end to zakonczenie
print("Kolejny print")
print("Nowy", "tekst", sep = "\n"*3)

