f = open("plik.txt", "w") # Nadpisuje plik

# r - tylko do odczytu
# w - do zapisu, jesli plik nie istnieje to zostanie utworzony, jesli istnieje zostanie nadpisany
# x - do tworzenia, operacja nie powiedzie sie jesli plik juz istnieje
# a - dopisywanie, jesli plik nie istnieje to zostanie utworzony, jesli istnieje zostanie dodana nowa wartosc
# + - 

f.write("Ala ma kota")

f.close()
print(f)

with open("plik.txt", "a") as file: # Dodaje do pliku
    file.write("asdasdasd")
    file.write("asdasdasd")
    file.write("asdasdasd")
