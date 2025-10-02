lista = [1, 2, 3, 4, 5]  # CTRL + ALT + L - Pycharm sformatuje liste dodajac spacje jesli napisalismy wszystko ciagiem

for liczba in lista:
    print(liczba)
print("Koniec petli 1.")

napis = "Python"

for litera in napis:  # Mozemy wyciagac znaki ze stringow
    print(litera)
print("Koniec petli 2.")

lista_slow = ["slowo", "cos", "tam"]
for slowo in lista_slow:
    print(slowo)
print("Koniec petli 3.")

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for liczba in lista_liczb:
    if liczba % 2 == 0:
        continue  # Pomija spelniony warunek - wraca na start petli
    print("liczba nieparzysta:", liczba)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szukany_element = int(input("Podaj liczbe: "))
for element in lista:
    if element == szukany_element:
        print("Znaleziono szukany element:", element)
        break
    print("Przetworzony element:", element)

