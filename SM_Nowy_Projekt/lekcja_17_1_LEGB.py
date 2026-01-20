# L => Local
# E => Enclosing | Otaczająca/Zagnieżdżona
# G => Global
# B => Built-it | Wbudowna

# Global
x = 10  # Zasieg globalny
def funkcja_zewnetrzna():
    # Enclosing
    y = 20
    def funkcja_wewnetrzna():
        # Local
        z = 30
        # y = 15
        # x = 0
        # 1. Odczytuje L: z=30
        # 2. Odczytuje E: y=20
        # 3. Odczytuje G: x=10
        print(f"Wewnątrz: x={x}, y={y}, z={z}")

    funkcja_wewnetrzna()
    print(f"Wewnątrz: x={x}, y={y}")
    # Nie można odczytać po za funkcja_wewnetrzna()
    # print(z) # Błąd! NameError: name 'z' is not defined


funkcja_zewnetrzna()
