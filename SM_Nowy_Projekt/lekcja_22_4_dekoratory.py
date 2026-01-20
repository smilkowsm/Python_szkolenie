import time

def miernik_czasu(funkcja):
    # Funkcja wewnetrzna (wrapper) przyjmuje *args i **kwargs funkcji oryginalnej
    def wrapper(*args, **kwargs):
        start_time = time.time()
        wynik = funkcja(*args, **kwargs)
        end_time = time.time()

        czas_wykonania = end_time - start_time
        print(f"Funkcja '{funkcja.__name__}' wykonana w {czas_wykonania:.4f}s")
        return wynik # Zwracamy wynik oryginalnej funkcji
    return wrapper

@miernik_czasu
def licz_do_n(n):
    """Prosta funkcja ktora po prostu zlicza."""
    suma = 0
    for i in range(n):
        suma += 1
    return suma

wynik_liczenia = licz_do_n(1_000_000)

print(f"Wynik liczenia = {wynik_liczenia}")

licz_do_n_udekorowany = miernik_czasu(licz_do_n)
print(licz_do_n_udekorowany(1000000))