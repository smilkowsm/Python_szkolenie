def test_wyjatkow(wartosc):
    otwarty_plik = None # Zmienna do uzycia w 'finally'

    try:
        otwarty_plik = open('plik.txt', 'w')

        # Potencjalnie ryzykowna operacja
        wynik = 10 / wartosc
        otwarty_plik.write(f"Wynik: {wynik}\n")
    except ZeroDivisionError:
        print(" -> EXCEPT: Zlapano dzielenie przez zero.")
    except TypeError:
        print(" -> EXCEPT: Zlapano nieprawidlowy typ danych.")
    else:
        # Wykona sie tylko jesli try przebiegl bezblednie
        print(" -> ELSE: Operacja zakonczona sukcesem.")
    finally:
        # Wykona sie zawsze
        print(" -> FINALLY: Zamykanie pliku i sprzatanie.")
        if otwarty_plik:
            otwarty_plik.close()

# Test 1
print(" -- Test 1 --")
test_wyjatkow(5)

# Test 2
print(" -- Test 1 --")
test_wyjatkow(0)