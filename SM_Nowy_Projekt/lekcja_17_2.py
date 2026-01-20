licznik_globalny = 0 # G


def licznik_otaczajacy():
    licznik_otaczenia = 0  # E

    def inkrementuj():
        nonlocal licznik_otaczenia # Modyfikujemy zmienna E
        global licznik_globalny  # Modyfikujemy zmienna G

        licznik_otaczenia += 1
        licznik_globalny += 1

    inkrementuj()
    inkrementuj()
    print(f"E (Otoczający) po inkrementacji: {licznik_otaczenia}")

licznik_otaczajacy()
print(f"G (Globalny) po inkrementacji: {licznik_globalny}")