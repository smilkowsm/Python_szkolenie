# Praca Domowa 3.2


# Zadanie 1
# Użytkownik wpisuje wyrażenie arytmetyczne. Na przykład 23+12.
# Wydrukuj jego wynik. W naszym przykładzie wynikiem jest 35. Wyrażenie arytmetyczne może składać się tylko z trzech części: liczba, operacja, liczba. 
# Możliwe operacje: +, -, *, /.

dopuszczalne = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", " "]
wyrazenie = input("Wpisz wyrazenie arytmetyczne (Możliwe operacje: +, -, *, /):\n ") # input uzytkownika jako string
mozliwe_operacje = ["+", "-", "*", "/"] # Lista dopuszczalnych operacji
znak = ""  
znak_ilosc = 0
operacja = 0
czy_dzialanie = True

for element in wyrazenie: # Sprawdzamy czy input uzytkownika jest dzialaniem
    if element not in dopuszczalne:
        czy_dzialanie = False
if czy_dzialanie == False:
    print("Wyrazenie musi składać się tylko z trzech części: liczba, operacja, liczba. ")

while czy_dzialanie:
    for element in wyrazenie: # Sprawdzamy czy uzytkownik nie przekroczyl liczby operacji
        if element in mozliwe_operacje:
            znak_ilosc += 1

    if znak_ilosc == 1:
        for element in wyrazenie:
            if element in mozliwe_operacje: # Sprawdzamy czy operator jest na liscie
                znak = element # Sprawdzamy jaka operacje chce wykonac uzytkownik
                break
            else:
                operacja += 1 # Wyszukujemy index operatora, aby oddzielic liczby
        liczba_1 = int(wyrazenie[:operacja]) # Wyszukujemy liczbe 1 po indeksie
        liczba_2 = int(wyrazenie[operacja + 1:]) # Wyszukujemy liczbe 2 po indeksie

    else:
        print("Wyrazenie musi składać się tylko z trzech części: liczba, operacja, liczba. ")


    if znak == "+":
        print(f"Wynik = {liczba_1 + liczba_2}")
    elif znak == "-":
        print(f"Wynik = {liczba_1 - liczba_2}")
    elif znak == "*":
        print(f"Wynik = {liczba_1 * liczba_2}")
    elif znak == "/":
        print(f"Wynik = {liczba_1 / liczba_2}")
    break


# Zadanie 2
# Masz listę liczb całkowitych wypełnioną liczbami losowymi. Znajdź największy i najmniejszy element, policz elementy ujemne i dodatnie oraz zera. Wydrukuj wyniki.

import random

lista = [] # Tworzymy pusty zbior aby uniknac duplikatow
elementy_ujemne = 0
elementy_dodatnie = 0
zera = 0

dlugosc_listy = random.randint(5, 25) # Wyznaczamy dlugosc listy z podanego zakresu

for liczba in range(dlugosc_listy): # Utworzenie listy z losowa dlugoscia i liczbami
    liczba = random.randint(-20, 20) # Wyznaczamy losowe liczby calkowite ktore maja byc dodane do listy
    lista.append(liczba)

for liczba in lista:
    if liczba < 0:
        elementy_ujemne += 1 # Liczymy elementy ujemne
    elif liczba > 0:
        elementy_dodatnie += 1 # Liczymy elementy dodatnie
    else:
        zera += 1 # Liczymy zera


print(f"Najwiekszy element listy = {max(lista)}")
print(f"Najmniejszy element listy = {min(lista)}")
print(f"Liczba elementow ujemnych = {elementy_ujemne}")
print(f"Liczba elementow dodatnich = {elementy_dodatnie}")
print(f"Liczba zer = {zera}")