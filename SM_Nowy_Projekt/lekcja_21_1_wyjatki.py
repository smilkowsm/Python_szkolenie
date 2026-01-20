def berzpieczne_dzielenie(a, b):
    try:
        #Kod potencjalnie wywolujacy blad
        wynik = a / b
        print(F"Wynik dzielenia: {wynik}")
    except ZeroDivisionError:
        # Ta sekcja uruchomi sie tylko jesli wystapi nam ten konkretny blad.
        print("Blad: Nie mozna dzielic przez zero!")
        wynik = None
    except TypeError:
        print("Blad: Upewnij sie ze uzywasz liczb")
        wynik = None
    except:
        print("Jakis blad")
        wynik = None
    return wynik

# Przyklad 1: Poprawne dzialanie
berzpieczne_dzielenie(10, 2)

# Przyklad 2: Blad dzielenia przez 0 (ZeroDivisionError)
berzpieczne_dzielenie(10, 0)

# Przyklad 3: Blad wartosci danych ()
berzpieczne_dzielenie(10, "a")

