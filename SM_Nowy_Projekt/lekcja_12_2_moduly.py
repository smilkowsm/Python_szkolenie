#def pokaz():
#    print(f"To jest nazwa pliku {__name__} z naszego __name__")

#pokaz()
#if __name__ == "__main__":
#    pokaz()
#    from lekcja_11_2_bmi import bmi

# czym jest __name__
import random 

#gramy_dalej = "Tak"

while True:
    print("|________________________|")
    print("| Kamien, Papier, Nozyce |")
    print("|1.Kamien                |")
    print("|2.Papier                |")
    print("|3.Nozyce                |")
    print("|                        |")
    print("|0.Koniec________________|")

    P1 = int(input("Gracz_1 - Kamien, Papier, Nozyce?\n"))
    P2 = random.randint(1, 3)
    if P1 == 0:
        print("KONIEC")
        break
    elif P1 != 1 and P1 != 2 and P1 != 3 and P1 != 0:
        print("Wybierz opcje od 1 do 3!")
        continue
    elif P1 == 1 and P2 == 3:
        print("Gracz_1 wygrywa!")
    elif P1 == 3 and P2 == 2:
        print("Gracz_1 wygrywa!")
    elif P1 == 2 and P2 == 1:
        print("Gracz_1 wygrywa!")
    elif P2 == 1 and P1 == 3:
        print("Gracz_2 wygrywa!")
    elif P2 == 3 and P1 == 2:
        print("Gracz_2 wygrywa!")
    elif P2 == 2 and P1 == 1:
        print("Gracz_2 wygrywa!")
    else:
        print("Remis!") 
    gramy_dalej = (input("Czy chcesz grac dalej? Tak/Nie: "))
    if gramy_dalej == "Nie":
        break