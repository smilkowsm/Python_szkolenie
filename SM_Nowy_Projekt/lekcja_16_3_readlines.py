with open("plik.txt") as f:

    linia = f.readlines() # Odczytuje jako lista, kazda linijka to oddzielny element listy
    print(linia)
    for linie in linia: 
        print(linia, end="")

