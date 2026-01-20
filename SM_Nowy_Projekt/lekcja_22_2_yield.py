import sys

lista_milion = [i for i in range(1_000_000)]
print(f"Rozmiar listy (1M elementow): {sys.getsizeof(lista_milion)} bajtow.")

generator_milion = (i for i in range(1_000_000))
print(f"Rozmiar generatora (1M elementow): {sys.getsizeof(generator_milion)} bajtow.")
print(next(generator_milion))