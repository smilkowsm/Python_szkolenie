class Ksiazka:
    calkowita_liczba_ksiazek = 0

    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        Ksiazka.calkowita_liczba_ksiazek += 1
        self.id = self.calkowita_liczba_ksiazek

if __name__ == '__main__':

    ksiazka_1 = Ksiazka("quovadis", "sienkiewicz")
    ksiazka_2 = Ksiazka("maly ksiaze", "saint exupery")

print(ksiazka_1.tytul)
print(ksiazka_1.autor)
print(ksiazka_1.id)

print(ksiazka_2.tytul)
print(ksiazka_2.autor)
print(ksiazka_2.id)