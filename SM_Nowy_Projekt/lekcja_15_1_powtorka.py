# napisz program ktory zmieni wprowadzony ciag cyfrowuy na forme tekstowy

liczba = int(input("Podaj liczbe: "))
liczba = str(liczba)

liczby_set = {"0": "zero", "1" : "jeden", "2" : "dwa", "3" : "trzy", "4" : "cztery", "5" : "piec", "6" : "szesc", 
              "7" : "siedem", "8" : "osiem", "9" : "dziewiec"}

wynik = ""

for liczby in liczba:
    wynik += liczby_set[liczby] + " "


print(wynik)

# stworz funkcje ktora bedzie przyjmowala liste liczb calkowitych a zwracala info na ktorej pozycji znajduje sie min


def liczby():
    lista_liczb = [42, 13, 56, 7, 12, 3, 85]
    szukana = (min(lista_liczb))
    wynik = 0

    for i in lista_liczb:
        if i != szukana:
            wynik += 1
    print(wynik - 1)

liczby()

"""
Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza. 
Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna wartość logiczną 
True/False.

Np.

Dla 11 funkcja zwróci True, natomiast dla 12 -> False.
"""


def czy_pierwsza():

    liczba = int(input("Podaj liczbe: "))
    liczby_pierwsze = []
    if liczba > 1:
        liczba_pierwsza = True
        for liczby in range(2, int(liczba ** 0.5) + 1):
            if liczba % liczby == 0:
                liczba_pierwsza = False
                break
        if liczba_pierwsza == True:
            liczby_pierwsze.append(liczba)
    else:
        liczba_pierwsza = False

    print(f"{liczba_pierwsza}")

czy_pierwsza()

"""
Stwórz funkcję, która sprawdzi, czy podany jako argument napis jest palindromem 
(tj. czytany od przodu i wspak jest dokładnie taki sam, np. „kajak”, „Madam”).
"""
def palindrom(slowo):
    
    if slowo == slowo[::-1]:
        print(f"Slowo {slowo} jest palindromem")

palindrom()

"""
Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.

np. dla : “The quick Brown Fox” oczekiwany wynik : Liczba wielkich liter : 3, 
liczba małych liter : 13

Podpowiedź: wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody dla stringa.
"""

def litery(ciag):
    wielkie = 0
    male = 0

    for litera in ciag:
        if litera == litera.upper():
            wielkie += 1
        elif litera == litera.lower():
            male += 1
        else:
            pass
    print(f"Liczba wielkich liter : {wielkie}, liczba małych liter : {male}")

litery("The quick Brown Fox")

