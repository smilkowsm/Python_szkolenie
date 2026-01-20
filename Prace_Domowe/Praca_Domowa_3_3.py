# Praca Domowa 3.3

# Zadanie 1
# Dwie listy liczb całkowitych zostały wypełnione liczbami losowymi. Wykonaj następujące czynności:
# Utwórz trzecią listę zawierającą elementy obu list;
# Utwórz trzecią listę zawierającą elementy obu list bez powtórzeń;
# Utwórz trzecią listę zawierającą elementy wspólne dla obu list;
# Utwórz trzecią listę zawierającą elementy unikalne dla każdej z list;
# Utwórz trzecią listę zawierającą tylko najmniejsze i największe wartości z każdej listy.
import random

lista_1 = []
lista_2 = []

dlugosc_listy = random.randint(5, 15) # Wyznaczamy losowa dlugosc listy z podanego zakresu


for liczba in range(dlugosc_listy): # Utworzenie 2 list z losowa dlugoscia i liczbami
    liczba_1 = random.randint(-20, 20) # Wyznaczamy losowe liczby calkowite ktore maja byc dodane do listy
    lista_1.append(liczba_1)
    liczba_1 = random.randint(-20, 20)
    lista_2.append(liczba_1)

lista_3 = []
lista_3.extend(lista_1) # Dodanie elementow z listy pierwszej
lista_3.extend(lista_2) # Dodanie elementow z listy drugiej

print(f"Pierwsza lista: {lista_1}") # Sprawdzenie zawartosci listy 1
print(f"Druga lista: {lista_2}") # Sprawdzenie zawartosci listy 2
print(f"Trzecia lista zawierajaca elementy obu list: {lista_3}") # Sprawdzenie zawartosci listy 3

lista_3 = set(lista_3) # Zmiana na set/usuniecie duplikatow
lista_3 = list(lista_3) # Ponowna zmiana na liste
print(f"Trzecia lista zawierajaca elementy obu list, bez duplikatow: {lista_3}") # Sprawdzenie zawartosci listy 3 po usunieciu duplikatow

lista_3 = []
for element in lista_1: # Wyciagniecie wspolnych elementow z listy 1 i 2
    if element in lista_2:
        lista_3.append(element)

print(f"Trzecia lista zawierajaca elementy wspolne obu list: {lista_3}") # Sprawdzenie zawartosci listy 3 z wspolnymi elementami

lista_3 = set() 
for element in lista_1: # Wyciagniecie roznych elementow z listy 1 i 2
    if element not in lista_2:
        lista_3.add(element)
for element in lista_2:
    if element not in lista_1:
        lista_3.add(element)
lista_3 = list(lista_3)
print(f"Trzecia lista zawierajaca elementy unikalne obu list: {lista_3}") # Sprawdzenie zawartosci listy 3 z roznymi elementami

lista_3 = []
lista_3.append(max(lista_1)) # Wyciagniecie maksymalnych i minimalnych wartosci z obu list
lista_3.append(max(lista_2))
lista_3.append(min(lista_1))
lista_3.append(min(lista_2))
print(f"Trzecia lista zawierajaca elementy minimalne i maksymalne obu list: {lista_3}") # Sprawdzenie zawartosci listy 3 z max i min elementami