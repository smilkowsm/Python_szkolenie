def dodaj_jeden(x):
    return x + 1

print(f"Standardowa funkcja: {dodaj_jeden(5)}")

dodaj_jeden_lambda = lambda x: x + 1

print(f"Funkcja lambda: {dodaj_jeden_lambda(5)}")

lista_studentow = [
    {'imie': 'Anna', 'ocena': 4.5},
    {'imie': 'Bartek', 'ocena': 5},
    {'imie': 'Celina', 'ocena': 3}
]

posortowana_lista = sorted(lista_studentow, key=lambda x: x['ocena'], reverse=True) # reverse zmienia kolejnosc - wynik pokaze od najwiekszej do najmniejszej

for student in posortowana_lista:
    print(student)

i = 0
for student in posortowana_lista:
    i += 1
    print(f"{i}:", student)


lista_liczb = [1, 5, 3, 7, 9, 8]

for liczba in lista_liczb:
        print(liczba)

print(sorted(lista_liczb))



def sortowanie():
    lista_liczb = [1, 5, 3, 7, 9, 8]
    nowa_lista = []
    for _ in lista_liczb:
        nowa_lista.append(max(lista_liczb))
        lista_liczb.remove(max(lista_liczb))
    print(nowa_lista)

