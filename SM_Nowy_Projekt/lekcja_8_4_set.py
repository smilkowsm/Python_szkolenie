zbior_1 = set(range(5))
zbior_2 = {0, 1, 2, 3, 4}
lista = [5]*10

print("zbior_1:", zbior_1)
print("zbior_2:", zbior_2)
print("lista:", lista)
print("lista przekonwertowana na zbior:", set(lista))
print("lista po usunieciu duplikatow:", list(set(lista)))

zbior_2.add(5)
zbior_2.add(6)
print("zbior_2 po dodaniu elementow 5,6:", zbior_2)

zbior_2.update({9, 8, 7}) # Dziala jak extend w listach
print("zbior_2 po dodaniu zbioru {9, 8, 7}:", zbior_2)

