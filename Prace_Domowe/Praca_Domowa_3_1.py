# Praca Domowa 3.1

# Zadanie 1
# Użytkownik wpisuje ciąg znaków. Sprawdź, czy ten ciąg jest palindromem. Palindrom to słowo lub tekst, który czyta się tak samo do tyłu jak do przodu. 
# Na przykład: racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?".

slowo = input("Wpisz tekst: ")
slowo = slowo.upper() 
tekst = slowo.replace(" ", "").replace("!", "").replace("?", "").replace(",", "").replace(".", "").replace("'", "").replace('"', '') 

if tekst == tekst[::-1]: 
    print("Ten ciag znakow jest palindromem.")
else:
    print("Ten ciag znakow nie jest palindromem.")



# Zadanie 2
# Użytkownik wpisuje tekst, po którym następuje lista zarezerwowanych słów. Znajdź w tekście wszystkie zastrzeżone słowa i zamień w nich małe litery na wielkie. 
# Wydrukuj zmodyfikowany tekst.

tekst = input("Wpisz tekst: ") # Ala ma kota. Kot lubi Alę. Mama Ali Nie lubi go wcale.
lista_slow = tekst.split() 
lista_zrezerwowane = ["Ala", "Kot", "Mama"]
lista = []
for slowo in lista_slow:
    if slowo in lista_zrezerwowane:
        lista.append(slowo.upper())
    else:
        lista.append(slowo)
lista_zmodyfikowana = " ".join(lista)
print(lista_zmodyfikowana)

# Zadanie 3
# Istnieje pewien tekst. Policz liczbę zdań w tekście i wypisz wynik.

tekst = input("Wpisz swoj tekst: \n")
liczba_zdan = 0

for zdanie in tekst:
    if zdanie == "." or zdanie == "?" or zdanie == "!":
        print(zdanie)
        liczba_zdan += 1
print(liczba_zdan)

