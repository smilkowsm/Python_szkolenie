def generator_potegi(wykladnik):
    """Funkcja zewnetrezna (Enclosing) - definiuje staly wykladnik."""
    # "wykladnik" jest zmienna, ktora zapamieta domkniecie

    def podnies_do_potegi(liczba):
        """Funkcja wewnetrzna - odwoluje sie do zmiennej zewnetrznej 'wykladnik'."""
        return liczba ** wykladnik
    
    # Zwracamy funkcje wewnetrzna - powstaje domkniecie
    return podnies_do_potegi

# 1. Tworzymy domkniecie dla potegi 2 (kwadrat)
kwadrat = generator_potegi(2)

# 2. Tworzymy domkniecie dla potegi 3 (szescian)
szescian = generator_potegi(3)

print(f"5 do kwadratu: {kwadrat(5)}") # kwadrat(5) uzywa zapamietanej wartosci 2 (linijka 13)
print(f"3 do szescianu: {szescian(3)}") # szescian(3) uzywa zapamietanej wartosci 3 (linijka 16)

