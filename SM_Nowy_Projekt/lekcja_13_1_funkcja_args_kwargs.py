def funkcja(arg_1, arg_2, kwarg_1 = 0, kwarg_2 = None ):
    print(f"arg_1 = {arg_1}, arg_2 = {arg_2}, kwarg_1 = {kwarg_1}, kwarg_2 = {kwarg_2}")

print("funkcja(arg = 11, arg_2 = 22):")
funkcja(11, 22)


print("funkcja(arg = 11, arg_2 = 22):")
funkcja(arg_1 = 11, arg_2 = 22)


print("funkcja(33, 44, 55):")
funkcja(33, 44, 55) # Python uzna pierwsze wartosci jako argumenty nienazwane(argsy)


print("funkcja(33, 44, 55):")
funkcja(33, kwarg_2=44, arg_2=55) # Mozemy przypisywac wlasciwosci w roznej kolejnosci ( argsy nie maja wartosci domyslnej, kwargs maja domyslne wartosci i nie musimy jeje podawac ale mozemy je nadpisac)


# funkcja(kwarg_1= = 11, kwarg_2= = 22, 55, 70) # To jest zle, najpierw musimy podawac argumenty nienazwane (argsy)


def nowa_funkcja(*args, **kwargs):
    pass