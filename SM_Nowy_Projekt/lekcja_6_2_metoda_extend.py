lista_1 = [4, 5, 6]
lista_2 = [7, 8, 9]

lista_3 = lista_1 + lista_2
print(lista_3)

print("ID lista_1:", id(lista_1))
lista_1 += lista_2 # lista_1 = lista_1 + lista_2
print("ID lista_1 po zmianie:", id(lista_1))
print("Zmienna lista_1", lista_1)

lista_4 = ["a", "b", "c"]
lista_1.extend(lista_4)
print(lista_1)
