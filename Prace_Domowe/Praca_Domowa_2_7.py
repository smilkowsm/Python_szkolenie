# Praca Domowa 2.7

# Zadanie 1
# Wypisz wszystkie liczby pierwsze w podanym przez użytkownika zakresie. Liczba jest pierwsza, jeśli jest podzielna tylko przez samą siebie i przez jeden. 
# Na przykład 3 jest liczbą pierwszą, ale 4 już nie.

zakres = [liczba for liczba in range(int(input("Podaj zakres od: ")), int(input("Podaj zakres do: ")) + 1)]
liczby_pierwsze = []
for liczba in zakres:
    if liczba > 1:
        liczba_pierwsza = True
        for liczby in range(2, int(liczba ** 0.5) + 1):
            if liczba % liczby == 0:
                liczba_pierwsza = False
                break
        if liczba_pierwsza == True:
            liczby_pierwsze.append(liczba)

print(f"Liczby pierwsze w podanym zakresie: {liczby_pierwsze}")

# Zadanie 2
# Wydrukuj tabliczkę mnożenia dla wszystkich liczb od 1 do 10. Na przykład:
#1*1 = 1 1*2 = 2 ..... 1*10 = 10
#.....................................
#10*1 = 10 10*2 = 20 .... 10*10 = 100

for liczba in range(1, 11):
    for element in range(1,11):
        print(f"{liczba} * {element} = {liczba * element}", end = " ")
    print(f"\n{"*" * 250}")

# Zadanie 3
# Wydrukuj tabliczkę mnożenia w podanym przez użytkownika zakresie. Jeśli użytkownik podał 3 i 5, tabliczka mnożenia może wyglądać następująco:
#3*1 = 3 3*2 = 6 3*3 = 9 ... 3*10 = 30
#........................................
#5*1 = 5 5*2 = 10 5*3 = 15 ... 5*10 = 50

zakres = [liczba for liczba in range(int(input("Podaj zakres od: ")), int(input("Podaj zakres do: ")) + 1)]
for cyfra in zakres:
    for element in range(1,11):
        print(f"{cyfra} * {element} = {cyfra * element}", end = " ")
    print(f"\n{"*" * 250}")
