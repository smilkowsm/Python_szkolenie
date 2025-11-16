def konfiguracja_profilu(imie, *args, **kwargs):
    """
    Przyjmuje imie, opcjonalne argumenty pozycyjne (*args)
    oraz ustawienia naszego profilu jako argumenty nazwane (**kwargs)   
    """
    print(f"Konfiguruje profil dla {imie}")

    for klucz, wartosc in kwargs.items():
        print(f"\t- Ustawienia {klucz.capitalize()}: {wartosc}")

konfiguracja_profilu("Sebastian", wiek = 32, waga = 70, wzrost = 178, miasto = "Gdansk") # argsy sa zrwacane jako tuple, kwargsy jako slownik


