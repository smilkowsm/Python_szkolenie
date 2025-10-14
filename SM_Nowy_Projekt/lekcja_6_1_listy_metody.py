lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Zmienna lista:", lista)

liczba = 11
print("Zmienna liczba:", liczba)
kopia_liczby = liczba
print("Zmienna kopia_liczby:", kopia_liczby)
liczba = 12
print("Zmienna liczba po zmianie:", liczba)
print("Zmienna kopia_liczby:", kopia_liczby)

kopia_listy = lista
print("Zmienna kopia_listy:", kopia_listy)

lista[4] = None
print("Zmienna lista:", lista)
print("Zmienna kopia_listy:", kopia_listy)

print("ID zmiennej liczba:", id(liczba))
print("ID zmiennej kopia_liczby:", id(kopia_liczby))
print("ID zmiennej lista:", id(lista))
print("ID zmiennej kopia_listy:", id(kopia_listy))

lista_copy = lista.copy()
print("Zmienna lista_copy:", lista_copy)
lista[-1] = "Koniec"
print("Zmienna lista po zmianie:", lista)
print("Zmienna lista_copy:", lista_copy)
lista_wycinek = lista[:]
print("Zmienna lista_wycinek", lista_wycinek)
lista[0] = "Poczatek"
print("Zmienna lista po zmianie:", lista)
