pierwsza_lista = [1, 2, 3, ]
druga_lista = ["a", "b", "c"]
suma_list = pierwsza_lista + druga_lista
print("Suma list:", suma_list)

trzecia_lista = [4, 5, 6]
print("Suma pierwszej i trzeciej listy:", pierwsza_lista + trzecia_lista)

# Dodawanie lelmentow z 2 list:
rozwiazanie_1 = []
rozwiazanie_1 = [
                pierwsza_lista[0]+trzecia_lista[0],
                pierwsza_lista[1]+trzecia_lista[1],
                pierwsza_lista[2]+trzecia_lista[2]
]
print(rozwiazanie_1)

# Drugi sposob:

indeks = 0

for _ in pierwsza_lista:
    trzecia_lista[indeks] = pierwsza_lista[indeks] + trzecia_lista[indeks] # trzecia_lista zostanie nadpisana
    indeks += 1
print(trzecia_lista)


# Trzeci sposob:
indeks = 0
rozwiazanie_2 = [0,0,0]
for _ in pierwsza_lista:
    rozwiazanie_2[indeks] = pierwsza_lista[indeks] + trzecia_lista[indeks]
    indeks += 1
print(rozwiazanie_2)
