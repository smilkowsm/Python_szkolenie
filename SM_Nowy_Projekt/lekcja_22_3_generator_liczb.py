def ciag_liczb(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

# Uzycie generatora w petli for
for liczba in ciag_liczb(10):
    print(liczba)


def nasz_range(do, od=0, skok=1):

    while od < do:
        yield od
        od += skok

print(list(nasz_range(10, 5)))
