f = open("plik.txt")

while True:
    linia = f.readline() # Odczytuje z pliku (jak bysmy puszczali bez petli to czytalaby zawsze kolejna linie, bo zapamietuje index)
    if not linia:
        break
    print(linia)

    