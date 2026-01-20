def generuj_parzyste():
    print("-> Start Generatora")

    yield 0
    print("-> Po pierwszym Yield")

    yield 2
    print("-> Po drugim Yield")

    yield 4
    print("-> Koniec generatora")

gen = generuj_parzyste()
print("Krok 1: Wywolanie next()")
print(next(gen))

print("Krok 2: Wywolanie next()")
print(next(gen))

print("Krok 3: Ostatni next()")
print(next(gen))

try:
    print(next(gen))
except StopIteration:
    print("Osiagnieto koniec sekwencji (StopIteration)")