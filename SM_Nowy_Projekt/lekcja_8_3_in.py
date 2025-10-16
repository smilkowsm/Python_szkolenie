lista_liczb = list(range(0, 11, 2))
print(lista_liczb)
odwrocona_lista_liczb = list(range(11, 0, -2))
print(odwrocona_lista_liczb)

szukana_liczba = 3

print(f"czy szukana_liczba jest w lista_liczb: {szukana_liczba in lista_liczb}")
print(f"czy szukana_liczba jest w odwrotna_lista_liczb: {szukana_liczba in odwrocona_lista_liczb}")
print("*"*50)
print(f"Indeks szukana_liczba {szukana_liczba} w odwrocona_lista_liczb: {odwrocona_lista_liczb.index(szukana_liczba)}")


if szukana_liczba in lista_liczb:
    print(f"Indeks szukana_liczba {szukana_liczba} w lista_liczb: {lista_liczb.index(szukana_liczba)}")
else:
    print(f"szukana_liczba {szukana_liczba} nie znajduje sie w lista_liczb")
