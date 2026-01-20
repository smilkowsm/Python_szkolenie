def ustal_wiek(wiek):
    if not isinstance(wiek, int):
        raise TypeError("Wiek musi byc liczba calkowita.")
    
    if wiek < 0 or wiek > 150:
        # Podnosimy blad jesli wartosc jest nieprawidlowa.
        raise ValueError("Wiek musi byc w zakresie 0-150.")
    
#ustal_wiek(-5)


try:
    ustal_wiek(-5)
except ValueError as e:
    print(f"Zlapany blad wartosci {e}")

 