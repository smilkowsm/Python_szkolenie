def czy_izogram(slowo):
    slowo_1 = set(slowo)
    if len(slowo_1) == len(slowo):
        return True
    else:
        return False
    
#if len(set(slowo)) == len(slowo):
#    return True


if __name__ == "__main__": 
# Jezeli uruchomimy ten plik to zmienna __name__ ma wartosc  "__main__"
# Gdy zaimportujemy tenplik do innego pliku __name__ zwroci nazwe pliku z tym kodem
    while True:
        nasze_slowo = input("Podaj slowo: ")
        if czy_izogram(nasze_slowo):
            print(f"Slowo: {nasze_slowo} jest izogramem")
        else:
            print(f"Slowo: {nasze_slowo} nie jest izogramem")
        
        pytanie = input("Czy chcesz kontynuowac? [T/N]")
        if pytanie.upper() != "T":
            break


