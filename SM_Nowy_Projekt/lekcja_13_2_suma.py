def suma_wszystkich(a, b, *args): # *args odpowiada za niezliczona ilosc argumentow, czyli tutaj mamy 2 wymagane + tyle ile chcemy
    """
    Sumuje 'a', 'b', oraz wszystkie dodatkowe argumenty (*args).
    """
    wynik = a + b

    for liczba in args:
        wynik += liczba
    return wynik


wynik = suma_wszystkich(5, 5, 5)
print(wynik)




def suma_wszystkich(a, b, *args, c, d): # Jesli chcemy zdefiniowac c i d to musimy je okreslic przy wywolaniu
    """
    Sumuje 'a', 'b', oraz wszystkie dodatkowe argumenty (*args).
    """
    wynik = a + b + c + d # trzeba uwzglednic c i d

    for liczba in args:
        wynik += liczba
    return wynik


wynik = suma_wszystkich(5, 5, 5, 7, 9, c = 1, d = 2)
print(wynik)




