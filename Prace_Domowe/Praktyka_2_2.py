# Praktyka 2.2

# Zadanie 1
# Użytkownik wpisuje czas w sekundach od początku dnia. Na podstawie podanej przez użytkownika liczby oblicz, ile godzin, minut i sekund pozostało do północy.

sekundy_od_poczatku = (int(input("Wpisz czas w sekundach od poczatku dnia: ")))
doba = 86400
sekund_do_polnocy = doba - sekundy_od_poczatku

if sekund_do_polnocy >= 0 and sekund_do_polnocy <= 86400:
    sekundy_reszta = sekund_do_polnocy % 60
    minuty = sekund_do_polnocy // 60
    minuty_reszta = minuty % 60
    godziny = minuty // 60
    print(f"Do polnocy zostalo {godziny} godzin, {minuty_reszta} minut i {sekundy_reszta} sekund.")
else:
    print("Podaj poprawna wartosc.")

# Zadanie 2
# Użytkownik wpisuje średnicę okręgu. Na podstawie wybranej przez użytkownika wartości oblicz pole lub obwód okręgu.

import math

srednica = float(input("Podaj srednice okrtegu: "))
pole = math.pi * ((srednica * 0.5) ** 2)
obwod = math.pi * srednica
wybor = input("Co chcesz obliczyc? \n 1 - Pole \n 2 - Obwod \n Twoj wybor: " )
if wybor == "1":
    print(f"Pole okregu o srednicy {srednica} wynosi {pole:.2f}")
elif wybor == "2":
    print(f"Obwod okregu o srednicy {srednica} wynosi {obwod:.2f}")
else:
    print("Musisz wybrac 1 lub 2")

# Zadanie 3
# Użytkownik wpisuje koszt jednej konsoli do gier, jej ilość oraz rabat. Na podstawie dokonanego wyboru oblicz całkowitą kwotę zamówienia lub koszt jednej konsoli z uwzględnieniem rabatu.

koszt_konsoli = float(input("Podaj koszt konsoli: "))
ilosc = int(input("Ilosc konsol w zamowieniu: "))
rabat = float(input("Podaj wysokosc rabatu: "))
koszt_po_rabacie = koszt_konsoli - rabat
if ilosc == 1:
    print(f"Koszt jednej konsoli z uwzglednieniem rabatu wynosi {koszt_po_rabacie} zl")
elif ilosc > 1:
    print(f"Koszt zamowienia {ilosc} konsol z uwzglednieniem rabatu wynosi {koszt_po_rabacie * ilosc:.2f} zl")
else:
    print("Podaj poprawna ilosc.")

# Zadanie 4
# Użytkownik wpisuje rozmiar pliku w gigabajtach i przepustowość łącza w bitach na sekundę. W oparciu o wybór użytkownika oblicz, ile godzin, minut lub sekund zajmie pobranie pliku.

rozmiar = float(input("Rozmiar pliku (GB): "))
przepustowosc = float(input("Przepustowosc lacza (b/s): "))
bity = rozmiar * 8 * (1024**3)
wybor = input("Chcesz otrzymac czas pobierania w:\n1 - sekundach\n2 - minutach\n3 - godzinach\nWybor: ")
b_s = bity / przepustowosc

if wybor == "1":
    print(f"Czas pobierania pliku o wielkosci {rozmiar}GB wynosi {b_s:.1f} sekund.")
elif wybor == "2":
    b_m = b_s / 60
    print(f"Czas pobierania pliku o wielkosci {rozmiar}GB wynosi {b_m:.1f} minut.")
elif wybor == "3":
    b_g = b_s / 3600
    print(f"Czas pobierania pliku o wielkosci {rozmiar}GB wynosi {b_g:.1f} godzin.")
else:
    print("Wpisz poprawne dane.")

# Zadanie 5
# Użytkownik wpisuje godzinę (od 0 do 23). Jeśli otrzymana wartość mieści się w zakresie od 0 do 6, wyświetl "Good Night"; jeśli od 6 do 13, wyświetl "Good Morning"; 
# jeśli od 13 do 17, wyświetl "Good Day"; jeśli od 17 do 0, wyświetl "Good Evening". Górna granica zakresu nie jest uwzględniana. Na przykład, jeśli wpisano 6, 6 należy do zakresu od 6 do 13.

godzina = int(input("Podaj godzine (od 0 do 23): "))
if godzina >= 0 and godzina < 6:
    print("Good Night")
elif godzina >= 6 and godzina < 13:
    print("Good Morning")
elif godzina >= 13 and godzina < 17:
    print("Good Day")
elif godzina >= 17 and godzina < 24:
    print("Good Evening")
else:
    print("Podaj poprawny zakres")