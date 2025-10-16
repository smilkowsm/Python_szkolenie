lista_zakupow = ["jajka", "szynka", "ser"]
ilosci = [4, 2, 3]

print(f"lista_zakupow: {lista_zakupow}")
print(f"ilosci: {ilosci}")
print("Funkcja zip:", zip(lista_zakupow, ilosci))
print("Lista po spakowaniu::", list(zip(lista_zakupow, ilosci)))

dluzsza_lista = ["red", "hot", "chili", "peppers"]
krotsza_lista = ["Czerwone", "gorace", "czili"]
print(f"dluzsza_lista: ({len(dluzsza_lista)}) - {dluzsza_lista}")
print(f"krotsza_lista: ({len(krotsza_lista)}) - {krotsza_lista}")

print("Lista po spakowaniu:", list(zip(dluzsza_lista, krotsza_lista)))

print("*"*50)
print("Lista po spakowaniu:", list(zip(lista_zakupow, dluzsza_lista, krotsza_lista)))

print(list(zip("51", krotsza_lista)))
