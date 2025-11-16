def oblicz_bmi(waga, wzrost):
    wynik = waga / wzrost ** 2
    print(wynik)

oblicz_bmi(90, 2)

def bmi(waga, wzrost):
    wynik = waga / wzrost ** 2 # Mozemy cala ta funkcje zapisac z samymi ifami i bedzie dzialac tak samo, poniewaz return dziala tez jak break i nie bedzie sprawdzac reszty warunkow po spelnieniu warunku
    if wynik < 18.5:
        return "Masz niedowage."
    elif wynik < 25:
        return "Masz prawidlowa wage."
    elif wynik < 30:
        return "Masz nadwage."
    return "Masz otylosc." # Dajemy w tym wcieciu zamiast else i bedzie to dzialac tak jakby ten else byl

moja_waga = float(input("Podaj swoja wage: "))
moj_wzrost = float(input("Podaj swoj wzrost: "))

(bmi(moja_waga, moj_wzrost)) # Nie wyswietli tego
print(bmi(moja_waga, moj_wzrost)) # Wyswietli
moje_bmi = (bmi(moja_waga, moj_wzrost))
print(moje_bmi) # Wyswietli

