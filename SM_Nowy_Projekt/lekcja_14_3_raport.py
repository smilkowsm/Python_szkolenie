# obowiazkowy argument - tytul
# *kwargs
# uwagi - slownik

def generuj_raport(tytul, *args, **kwargs):

    """
    Generuje raport z podanym tytulem, lista ocen (*args)
    oraz uwagi dodatkowe (**kwargs)
    """

    print(f"{tytul}")

    for arg in args:
        print(f"Ocena: {arg}")

    for key, value in kwargs.items():
        print(f"Uwagi: {key} : {value}")

generuj_raport("Raport", 5, 4, 3, uwaga_1 = "uwaga_1", uwaga_2 = "uwaga_2", uwaga_3 = "uwaga_3")






def konfiguracja_profilu(imie, *args, **kwargs):
    """
    Przyjmuje imie, opcjonalne argumenty pozycyjne (*args)
    oraz ustawienia naszego profilu jako argumenty nazwane (**kwargs)   
    """
    print(f"Konfiguruje profil dla {imie}")

    for klucz, wartosc in kwargs.items():
        print(f"\t- Ustawienia {klucz.capitalize()}: {wartosc}")

konfiguracja_profilu("Sebastian", wiek = 32, waga = 70, wzrost = 178, miasto = "Gdansk") # argsy sa zrwacane jako tuple, kwargsy jako slownik



