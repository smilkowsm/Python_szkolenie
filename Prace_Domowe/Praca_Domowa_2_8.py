# Praca Domowa 2.8

# Zadanie 1
# Wydrukuj liczby wypełnione gwiazdkami. Zaimplementuj okno dialogowe z użytkownikiem za pomocą menu.

print("""
________________________________________________________________________________
|                       			WYBIERZ WZOR                                |
|   																			|
|  *****  *       *********      *      *****  *    *  *      *  *****      *   |
|   ****  **       *******      ***      ***   **  **  **    **  ****      **   |
|    ***  ***       *****      *****      *    ******  ***  ***  ***      ***   |
|     **  *****      ***      *******     *    **  **  **    **  **      ****   |
|      *  ******      *      *********   ***   *    *  *      *  *      *****   |
|      A   B          C          D      *****     F    G      H  I          J   |
|                                         E                                     |
|_______________________________________________________________________________|    
""")
wybor = input("Wybierz wzor: ")
wybor = wybor.upper()
dlugosc = int(input("Podaj dlugosc: "))



if wybor == "A":
    wartosc = 1
    while dlugosc:
        print(" " * wartosc, "*" * dlugosc)
        wartosc += 1
        dlugosc -= 1

elif wybor == "B":
    wartosc = 1
    while wartosc <= dlugosc:
        print("*" * wartosc)
        wartosc += 1

elif wybor == "C":
    wartosc = 0
    if dlugosc % 2 != 0:
        while dlugosc:
            if dlugosc % 2 != 0:
                print(" " * wartosc, "*" * dlugosc)
                wartosc += 1
                dlugosc -= 1
            else:
                dlugosc -=1
    else:
        while dlugosc:
            if dlugosc % 2 == 0:
                print(" " * wartosc, "*" * dlugosc)
                wartosc += 1
                dlugosc -= 1
            else:
                dlugosc -=1

elif wybor == "D":
    dlugosc = float(dlugosc)
    wartosc = 1
    if dlugosc % 2 != 0:
        while dlugosc:
            if dlugosc % 2 != 0:
                print(" " * int(dlugosc - (0.5 * dlugosc + 0.5)), "*" * wartosc)
                wartosc += 2
                dlugosc -= 1
            else:
                dlugosc -= 1
    else:
        wartosc = 2
        while dlugosc:
            if dlugosc % 2 == 0:
                print(" " * int(dlugosc - (0.5 * dlugosc + 0.5)), "*" * wartosc)
                wartosc += 2
                dlugosc -= 1
            else:
                dlugosc -= 1

elif wybor == "E":
    dlugosc_2 = dlugosc
    wartosc_2 = 0
    if dlugosc_2 % 2 != 0:
        while dlugosc_2:
            if dlugosc_2 % 2 != 0:
                print(" " * wartosc_2, "*" * dlugosc_2, sep = "")
                wartosc_2 += 1
                dlugosc_2 -= 1
            else:
                dlugosc_2 -= 1
        dlugosc = float(dlugosc)
        wartosc = 1
        while dlugosc:
            if dlugosc % 2 != 0:
                print(" " * int(dlugosc - (0.5 * dlugosc + 0.5)), "*" * wartosc, sep = "") 
                wartosc += 2
                dlugosc -= 1
            else:
                dlugosc -= 1
    else:
        dlugosc_2 = dlugosc
        wartosc_2 = 0
        while dlugosc_2:
            if dlugosc_2 % 2 == 0:
                print(" " * wartosc_2, "*" * dlugosc_2, sep = "")
                wartosc_2 += 1
                dlugosc_2 -= 1
            else:
                dlugosc_2 -= 1
        dlugosc = float(dlugosc)
        wartosc = 2
        while dlugosc:
            if dlugosc % 2 == 0:
                print(" " * int(dlugosc - (0.5 * dlugosc + 0.5)), "*" * wartosc, sep = "") 
                wartosc += 2
                dlugosc -= 1
            else:
                dlugosc -= 1
    

elif wybor == "F":
    wartosc = 1
    wartosc_2 = wartosc
    dlugosc_2 = dlugosc
    while dlugosc:
        print("*" * wartosc, " " * (dlugosc * 2), "*" * wartosc, sep = "")
        dlugosc -= 1
        wartosc += 1
    while dlugosc_2:
        print("*" * (dlugosc_2 - 1), " " * ((wartosc_2 + 1) * 2), "*" * (dlugosc_2 - 1), sep = "")
        dlugosc_2 -= 1
        wartosc_2 += 1

elif wybor == "G":
    wartosc = 1
    dlugosc_2 = dlugosc
    while dlugosc:
        print("*" * wartosc)
        dlugosc -= 1
        wartosc += 1
    while dlugosc_2:
        print("*" * (dlugosc_2 - 1))
        dlugosc_2 -= 1

elif wybor == "H":
    wartosc = 1
    wartosc_2 = wartosc
    dlugosc_2 = dlugosc
    while dlugosc:
        print(" " * dlugosc, "*" * wartosc)
        dlugosc -= 1
        wartosc += 1
    while dlugosc_2:
        print(" " * (wartosc_2 + 1), "*" * (dlugosc_2 - 1))
        dlugosc_2 -= 1
        wartosc_2 += 1

elif wybor == "I":
    while dlugosc:
        print("*" * dlugosc)
        dlugosc -= 1

elif wybor == "J":
    wartosc = 1
    while dlugosc:
        print(" " * dlugosc, "*" * wartosc)
        dlugosc -= 1
        wartosc += 1

else:
    print("Wybierz wzor z podanego zakresu!")