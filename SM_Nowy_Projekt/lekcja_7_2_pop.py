lista = [1, 2, 3, 4, 5]

print(f"To nasza lista: {lista}")

element_pop = lista.pop()
print(f"Zmienna lista po pierwszej metodzie pop: {lista}")
print(f"Zmienna element.pop: {element_pop}")

lista.pop() # pop domyslnie zabiera ostatnia wartosc
print(f"Zmienna lista po drugiej metodzie pop: {lista}")

lista.pop(1)
print(f"Zmienna lista po trzeciej metodzie pop: {lista}")

lista_2 = [1]
lista_2.pop()
print(f"Lista_2 po uzyciu pop: {lista_2}")

lista_3 = [2]
print(f"Zwrocony element z lista_3: {lista_3.pop()}")

print(id(lista_3))
print(hex(id(lista_3)))

#del lista # Usunie liste, wywola blad przy nastepnej probie odwolania sie do tej listy
print(lista)
del lista[1]
print(f"Lista po uzyciu metody del na elemencie z indeksem 1: {lista}")

# Dodawanie elementow w srodku listy
lista_4 = [3, 6, 5, 4]
lista_5 = lista_4[0:3] + ["a", "b"] + lista_4[3:]
print(lista_5)

print(min(lista_4)) # Zwraca najmniejsza wartosc
print(max(lista_4)) # Zwraca najwieksza wartosc
print(sum(lista_4))

lista_6 = ["a", "b", "c"]
print(min(lista_6)) # W przypadku liter dziala alfabetycznie


print("Metoda sort:", lista_4.sort())
print("Metoda sorted:",sorted(lista_4))
print("Metoda reversed:",reversed(lista_4))
print("Metoda reversed przekonwertowana na liste:",list(reversed(lista_4)))

print("Metoda reversed przekonwertowana na liste:",str(reversed(lista_4)))

# jakie wartosci mozemy przekonwertowac na jakie? npt list na str itp.
