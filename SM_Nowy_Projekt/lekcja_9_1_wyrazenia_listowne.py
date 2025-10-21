lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Pomnoz parzyste liczby x2 i dodaj do nowej listy
nowa_lista = []
for i in lista:
    if i % 2 == 0:
        i = i * 2
        nowa_lista.append(i)

print(nowa_lista)

print("*" * 50)

#      (3 krok)(   1 krok   ) (   2 krok   )
wynik = [x * 2 for x in lista if x % 2 == 0] # Wyrazenie listowne
# wynik = [(x * 2) for x in lista if x % 2 == 0] # Dajemy () dla przejrzystosci, dziala tak samo
print(wynik)

lista = [1, 2, 3, 4, 5]
lista_2 = [101, 102, 103, 104, 105]
nowsza_lista = []
for x in lista:
    for y in lista_2:
        wynik = (x * y)
        nowsza_lista.append(wynik)
print(nowsza_lista)

wynik = [x * y for x in lista for y in lista_2] # To samo co wyzej
