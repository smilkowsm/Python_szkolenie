licznik = 0
while licznik <= 5:
    print("Wartosc licznika wynosi:", licznik) # Jesli przesuniemy print po "licznik += 1" odliczanie zacznie sie od 1
    licznik += 1
    print("Zwiekszamy wartosc licznika o 1")

print("\tKoniec petli\n") # \t - tabulator | \n - ENTER
print("Wartosc licznika wynosi:", licznik)

while True: # W takiej formie petla bedzie nieskonczona - warunek zawsze jest prawdziwy
    print("Petla nieskonczona")
    break    # break przerywa petle


while True:
    koniec = input("Zakonczyc petle? Y/N ")
    if koniec != "Y":
        print("Petla")
    else:
        break

