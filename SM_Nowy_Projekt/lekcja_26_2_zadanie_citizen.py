""" Zadanie Citizen

Napisz klasę Citizen, która implementuje metodę init, przyjmującą dwa argumenty: first name i last name. Stwórz obiekt
tej klasy, a następnie wyświetl imię i nazwisko obywatela.

Dodaj metodę klasową set_nationality do klasy Citizen (a wraz z nią pole klasowe nationality o wybranej wartości
domyślnej). Wywołaj tę metodę. Stwórz drugi obiekt klasy i zobacz, jaką wartość będzie miało pole nationality w obu
obiektach.

Dodatkowo możesz spróbować dodać atrybut klasowy total_number_of_citizens będący liczbą. Zwiększaj ją za każdym razem,
kiedy tworzony będzie nowy obywatel.
"""

class Citizen:
    nationality = "Nieznana"
    total_number_of_citizens = 0

    def __init__(self, first_name, last_name, nationality=None):
        self.first_name = first_name
        self.last_name = last_name

        # Zwiększamy licznik obywateli przy każdym nowym obiekcie
        Citizen.total_number_of_citizens += 1

    # Metoda klasowa do zmiany narodowości
    @classmethod
    def set_nationality(cls, new_nationality):
        cls.nationality = new_nationality

    def __str__(self):
        return f"Obywatel: {self.first_name} {self.last_name}, Obywatelstwo: {self.nationality}"

if __name__ == '__main__':
    dawid_n = Citizen("dawid", "nowak") # Tworzymy pierwszego obywatela
    lukasz_s = Citizen("lukasz", "skoczek") # Tworzymy drugiego obywatela
    jan_k = Citizen("jan", "kat") # Tworzymy trzeciego obywatela

    Citizen.set_nationality("Polska")

    # Sprawdzamy narodowość pierwszego obywatela po zmianie klasy
    print("Narodowość obywatela 1 po zmianie:", lukasz_s.nationality)

    # Sprawdzamy liczbę obywateli
    print("Łączna liczba obywateli:", Citizen.total_number_of_citizens)
    z = str(jan_k)
    print(jan_k)
    print(z)

    print(type(jan_k))
    print(z.upper())