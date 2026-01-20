cena_netto = [100, 250, 50, 120]

cena_brutto = list(map(lambda cena: cena * 1.1, cena_netto))

print(cena_brutto)

imiona = ["ania", "Bartek", "celina"]

imiona_baza = list(map(lambda imie: imie.capitalize(), imiona))

print(imiona_baza)

