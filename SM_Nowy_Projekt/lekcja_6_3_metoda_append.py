lista_1 = ["a", "b", "c"]
lista_1.append("d") # append moze dodac tylko 1 element
lista_1.append("e")
lista_1.append(["f", "2"])
print("Zmienna lista_1:", lista_1)
print("Indeks 0 listy_1:", lista_1[0])
print("Indeks -1 listy_1:", lista_1[-1])
print("Indeks -1 listy_1 i indeksu 0 wewnatrz tej listy", lista_1[-1][0])

a, b, c = lista_1 # Bedzie tu blad poniewaz w tym momencie lista ma mniej elementow.
# Jesli przeniesiemy to do 2giej linijki gdzie lista ma 3 elementy to by zadzialalo
a, b, c = lista_1[:3] # To juz zadziala, bo sa 3 elementy
a, b, c = lista_1[0], lista_1[1], lista_1[2] # Tez zadziala bo sa 3 zmeinne

a, b = b, a # Podmienia ich wartosci - a=1, b=2 bedzie a=2, b=1


