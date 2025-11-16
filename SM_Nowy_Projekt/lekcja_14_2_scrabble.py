wartosci = {
         1: "A E I N O R S W Z",
         2: "C D K L M P T Y",
         3: "B G H J Ł U",
         5: "Ą Ę F Ó Ś Ż",
         6: "ĆŃ",
         7: "Ź",
         9: "Q V X"
     }


def scabble_punkty(slowo):
    #zwrocic puntkacje za slowo ile to slowo ma punktow
    pkt = 0
    for litera in slowo.upper():
        for wart, test_wart in wartosci.items():
            for test_litera in test_wart:
                #print("Testing: ", test_litera,' == ',litera)
                if test_litera == litera:
                    pkt += wart
                    print(" Punkt za ",litera , " ", wart)

    return pkt


if __name__ == '__main__':

    while True:
        slowo = input("Napisz slowo:  ")
        pkt = scabble_punkty(slowo)
        print("Dostales punktów: ", pkt)
        kont = input("Czy kontynuowac T/N ? : ")
        if kont.upper() == 'N':
            break