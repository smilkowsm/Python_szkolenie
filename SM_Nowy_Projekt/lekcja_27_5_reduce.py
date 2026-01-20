from functools import reduce

liczby = [1, 2, 3, 4, 5]

suma = reduce(lambda x, y: x + y, liczby)
print(suma)

czesci_zdania = ["Ala", "ma", "kota.", "Kot", "ma", "Ale."]
zdanie = reduce(lambda x, y: x + " " + y, czesci_zdania)

print(zdanie)