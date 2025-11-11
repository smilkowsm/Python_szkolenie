# Praktyka 2.3 Rozgałęzienia

# Zadanie 1
# Użytkownik wpisuje sześciocyfrową liczbę. Napisz program, który określi czy ta liczba jest szczęśliwa. (Szczęśliwa liczba to liczba sześciocyfrowa, której suma trzech pierwszych cyfr jest równa sumie trzech ostatnich cyfr).
# Na przykład 123321 jest liczbą szczęśliwą, ponieważ 1+2+3 = 3+2+1.
# Ale 378423 nie jest szczęśliwą liczbą, ponieważ 3+7+8 != 4+2+3.
# Jeśli użytkownik wpisał liczbę inną niż sześciocyfrowa, wyświetl komunikat o błędzie.

while True:
    szczesliwa_liczba = int(input("Podaj 6 cyfrowa liczbe: "))
    szczesliwa_liczba = str(szczesliwa_liczba)
    if len(szczesliwa_liczba) == 6:
        lista = []
        for i in szczesliwa_liczba:
            lista.append(int(i))
        if lista[0] + lista[1] + lista[2] == lista[3] + lista[4] + lista[5]:
            print("Gratulacje! To jest szczesliwa liczba!")
            break
        else:
            print("To nie jest szczesliwa liczba...")
            break
    else:
        print("BLAD! Liczba musi miec 6 cyfr!")
        continue

# Zadanie 2
# Użytkownik wpisuje sześciocyfrową liczbę. Zamień pierwszą i szóstą cyfrę, a także drugą i piątą.
# Na przykład, 723895 powinno stać się 593827.
# Jeśli użytkownik wpisał liczbę inną niż sześciocyfrowa, wyświetl komunikat o błędzie.

while True:
    liczba = int(input("Podaj 6 cyfrowa liczbe: "))
    liczba = str(liczba)
    if (len(liczba)) == 6:
        nowa_liczba = liczba[5] + liczba[4] + liczba[2] + liczba[3] + liczba[1] + liczba[0]
        print(nowa_liczba)
        break
    else:
        print("BLAD! Podana liczba nie ma 6 cyfr!")
        continue

# Zadanie 3
# Użytkownik wpisuje numer miesiąca (od 1 do 12). Na podstawie wpisanej liczby program wyświetli jeden z poniższych komunikatów: Zima, jeśli liczba wynosi 1, 2 lub 12, Wiosna, jeśli liczba mieści się w zakresie od 3 do 5, Lato, jeśli od 6 do 8, Jesień, jeśli od 9 do 11.
# Jeśli liczba jest poza zakresem, wyświetlony zostanie komunikat o błędzie.

while True:
    miesiac = int(input("Podaj liczbe od 1 do 12: "))
    if miesiac < 3 or miesiac == 12:
        print("Zima")
        break
    elif miesiac > 2 and miesiac < 6:
        print("Wiosna")
        break
    elif miesiac > 5 and miesiac < 9:
        print("Lato")
        break
    elif miesiac > 8 and miesiac < 12:
        print("Jesien")
        break
    else:
        print("BLAD! Podana liczba nie miesci sie w zakresie!")
        continue