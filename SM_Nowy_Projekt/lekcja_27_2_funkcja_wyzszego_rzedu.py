def funkcja():
    pass

# -- Nasi Pracownicy (zwykle funkcje) --

def format_krzyczacy(tekst):
    return tekst.upper() + "!!!"

def format_uprzejmy(tekst):
    return f"Szanowny Kliencie, informujemy: {tekst}."

# -- Nasz Menager (Funkcja Wyzszego Rzedu) --

def wyslij_powiadomienie(wiadomosc, sposob_formatowania):
    wynik = sposob_formatowania(wiadomosc)
    print(f"System wysyla: {wynik}")

# -- Wykonanie --

wyslij_powiadomienie("Paczka czeka do odbioru", format_krzyczacy)
wyslij_powiadomienie("Paczka czeka", format_uprzejmy)


def format_tajny(tekst):
    return "*" * len(tekst)

wyslij_powiadomienie("qwerty qwe w", format_tajny)

