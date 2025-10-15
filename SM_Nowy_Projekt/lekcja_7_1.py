lista = [1, 6, 3, 4]
lista.append(5)
print(f"Zmienna lisata po dodaniu wartosci 5: {lista}")
print("Dodanie liczby 5 w funkcji print za pomoca metody append:", lista.append(5))
print(f"Zmienna lisata po dodaniu wartosci 5: {lista}")
print(f"Uzycie metody sort w funkcji print: {lista.sort()}")
print(f"Zmienna lista po uzyciu metody sort: {lista}")

tekst = "Nasze zdanie"
print(f"To jest nasza zmienna tekst po uzyciu upper w funkcji print: {tekst.upper()}")
print(f"Na tym tekscie uzyc metody upper".upper())

print("Tekst {} {}".format("elementy", 1)) # Doda tyle lelmentow ile mamy utworzonych klamr
print("Tekst {} {} {}".format("elementy", 1, 5))
print("Tekst {b} {c} {a} informacje dalsze".format(a="elementy", b=1, c=5))
print("Tekst {2} {1} {0} informacje dalsze".format("elementy", 1, 5))
print("Tekst {2} {1} {0} informacje dalsze".format("elementy", 1, lista))
print("Tekst {0[0]} {0[1]} {0[2]} informacje dalsze".format([5,2,3,4]))
