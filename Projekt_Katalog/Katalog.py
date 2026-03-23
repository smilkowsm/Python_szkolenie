import json # Pakiet potrzebny do bazu danych
import re # Pakiet potrzebny przy formatowaniu stron
import requests # Pakiet potrzebny do pobierania informacji ze stron
from bs4 import BeautifulSoup # Pakiet potrzebny do ladnego formatowania stron, uzywam do dodania tytulu artykulu

# Pewnie daloby sie to troche schludniej zrobic, ale kierujac sie zasada ze jak dziala to nie ruszac oraz brakiem czasu zostawilem dzialajacy kod.

# Klasa bazowa
class Media:
    def __init__(self, tytul, gatunek, rok, ocena="Brak"): # Domyslnie kazda nowo dodana pozycja bedzie miala w ocenie "Brak"
        self.tytul = tytul
        self.gatunek = gatunek
        self.rok = rok
        self.ocena = ocena

    def slownik(self): # Funkcja bedie zmianiala nasze listy na slownik, zeby zapisywac wszystko w bazie w formacje json
        return self.__dict__

# Klasy dziedzicace
class Gra(Media):
    def __init__(self, tytul, gatunek, rok, studio, ocena="Brak"):
        super().__init__(tytul, gatunek, rok, ocena)
        self.studio = studio
        self.kategoria = "gra"


class Film(Media):
    def __init__(self, tytul, gatunek, rok, rezyser, ocena="Brak"):
        super().__init__(tytul, gatunek, rok, ocena)
        self.rezyser = rezyser
        self.kategoria = "film"


class Ksiazka(Media):
    def __init__(self, tytul, gatunek, rok, autor, wydawnictwo, ocena="Brak"):
        super().__init__(tytul, gatunek, rok, ocena)
        self.autor = autor
        self.wydawnictwo = wydawnictwo
        self.kategoria = "ksiazka"


class Katalog: # Klasa odpowiadajaca za baze danych, musialem sie tutaj troche posilkowac czatem zeby ogarnac zapisywanie wszystkiego w json'ie
    def __init__(self):
        self.plik = "baza.json" # W tym pliku zapisujemy wszystkie pozycje (trzeba uruchomic skrypt z tego samego folderu w ktorym znajduje sie baza)
        self.gry = []
        self.filmy = []
        self.ksiazki = []
        self.wczytaj()

    def zapisz(self):
        wszystkie_pozycje = []
        wszystkie_pozycje += [pozycja.slownik() for pozycja in self.gry] # Tu uzywamy funkcji slownik ktora zamienia nasze listy
        wszystkie_pozycje += [pozycja.slownik() for pozycja in self.filmy]
        wszystkie_pozycje += [pozycja.slownik() for pozycja in self.ksiazki]
        
        with open(self.plik, "w") as plik:
            json.dump(wszystkie_pozycje, plik, indent=4)

    def wczytaj(self):
        with open(self.plik, "r") as plik:
            dane_json = json.load(plik)

        for element_json in dane_json:

            if element_json["kategoria"] == "gra":
                self.gry.append(
                    Gra(
                        element_json["tytul"],
                        element_json["gatunek"],
                        element_json["rok"],
                        element_json["studio"],
                        element_json["ocena"],
                    ))

            elif element_json["kategoria"] == "film":
                self.filmy.append(
                    Film(
                        element_json["tytul"],
                        element_json["gatunek"],
                        element_json["rok"],
                        element_json["rezyser"],
                        element_json["ocena"],
                    ))

            elif element_json["kategoria"] == "ksiazka":
                self.ksiazki.append(
                    Ksiazka(
                        element_json["tytul"],
                        element_json["gatunek"],
                        element_json["rok"],
                        element_json["autor"],
                        element_json["wydawnictwo"],
                        element_json["ocena"],
                    ))


    def wybierz_liste(self): # Podmenu z wyborem kategorii ktore chcemy wyswietlic
        
        print("""
---WYBOR KATEGORII---

1 - Gry
2 - Filmy
3 - Ksiazki
              
0 - Wroc
            """)
        print("-" * 50)


        wybor = input("Wybierz kategorie: ")

        if wybor == "1":
            print("\nGRY:\nPozycja | Tytul | Gatunek | Rok Wydania | Ocena | Studio")
            return self.gry
        elif wybor == "2":
            print("\nFILMY:\nPozycja | Tytul | Gatunek | Rok Wydania | Ocena | Rezyser")
            return self.filmy
        elif wybor == "3":
            print("\nKSIAZKI:\nPozycja | Tytul | Gatunek | Rok Wydania | Ocena | Autor | Wydawnictwo")
            return self.ksiazki
        elif wybor == "0":
            return
        else:
            print("Bledny wybor")
            

    def pokaz(self, lista_kategorii):
        if not lista_kategorii:
            print("Brak pozycji")
            
        for indeks, pozycja in enumerate(lista_kategorii): # Tu uzywam enumerate do indeksowania pozycji, nie jest to zapisywane w bazie
            tekst_pozycji = f"{indeks} | {pozycja.tytul} | {pozycja.gatunek} | {pozycja.rok} | Ocena: {pozycja.ocena}"
            if ["kategoria"] == "gra":
                tekst_pozycji += f" | Studio: {pozycja.studio}"
            elif ["kategoria"] == "film":
                tekst_pozycji += f" | Rezyser: {pozycja.rezyser}"
            elif ["kategoria"] == "ksiazka":
                tekst_pozycji += f" | Autor: {pozycja.autor} | Wydawnictwo: {pozycja.wydawnictwo}"
            print(tekst_pozycji)

    def dodaj(self):
        print("""
---DODAJ POZYCJE---

1 - Gry
2 - Filmy
3 - Ksiazki
              
0 - Wroc
            """)
        
        wybor = input("Wybierz kategorie: ")
        if wybor == "0":
            return
        
        tytul = input("Tytul: ").title() # Uzywam title zeby kazde slowo z automatu bylo zpisywane z wielkiej litery
        gatunek = input("Gatunek: ").title()
        rok = input("Rok: ")

        if wybor == "1":
            studio = input("Studio: ").title()
            self.gry.append(Gra(tytul, gatunek, rok, studio))
        elif wybor == "2":
            rezyser = input("Rezyser: ").title()
            self.filmy.append(Film(tytul, gatunek, rok, rezyser))
        elif wybor == "3":
            autor = input("Autor: ").title()
            wydawnictwo = input("Wydawnictwo: ").title()
            self.ksiazki.append(Ksiazka(tytul, gatunek, rok, autor, wydawnictwo))
        else:
            print("Bledny typ")
            return
        self.zapisz()

    def usun(self):
        print("\n---USUN POZYCJE---")
        lista_kategorii = self.wybierz_liste()
        if lista_kategorii is None:
            return

        self.pokaz(lista_kategorii)

        try:
            indeks = int(input("Numer do usuniecia: "))
            lista_kategorii.pop(indeks)
            self.zapisz()
        except:
            print("Bledny numer")

    def ocen(self):
        print("\n---OCEN POZYCJE---")
        lista_kategorii = self.wybierz_liste()
        if lista_kategorii is None:
            return
        self.pokaz(lista_kategorii)
        try:
            indeks = int(input("Numer: "))
            ocena = int(input("Ocena 1-10: "))
            lista_kategorii[indeks].ocena = ocena
            self.zapisz()
        except:
            print("Bledne dane")

def newsy():  

    """
Tu jako dadatkowa opcje w katalogu dodalem cos co kiedys sobie juz robilem i wydaje mi sie ze akurat pasuje do projektu.
Jest to funkcja ktora pozwala wyszukiwac newsy na temat gier, filmow/seriali, ksiazek.
Po wybraniu kategorii, pozwala nam wyszukac newsa za pomoca slowa kluczowego i zwraca nam tytul artykulu i link do niego.
Dla newsow odnosnie gier i filmow/seriali odwoluje sie do portalu ppe.pl, a dla ksiazek premieryksiazkowe.pl.
Zakres przeszukiwanych stron ustawilem na sztywno aby przeszukiwal 5 pierwszych stron. Nie jest to zapisywane do bazy, bo dla niektorych wyszukiwan
moze zwrocic sporo wynikow i mocno by zasmiecalo. 
"""

    while True:
        print("""
1 - Gry
2 - Filmy
3 - Ksiazki
              
0 - Wroc
          """)

        wybor = input("Wybierz kategorie: ")
        print("#" * 50)


        if wybor == "1":
            klucz = input("Podaj slowo kluczowe: ")
            print("#" * 50)
            for strona in range(1,6):
                x = requests.get(f"https://www.ppe.pl/news.html?type=news&page={strona}") # podajemy link i zakres stron, za pomoca request pobiera nam informacje ze strony
                output = re.sub(r" ", "", x.text) # formatuje strone
                matches = re.findall(rf'/news/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE) # wybiera tylko linie ktore zaczynakja sie na: /news/, zawieraja "klucz" i koncza sie ' " ' i ignoruja wielkie/male litetry
                if matches:
                    for i in matches:
                        url = "https://www.ppe.pl" + i.rstrip('"') 
                        response = requests.get(url)
                        soup = BeautifulSoup(response.text, "html.parser") # tego pakietu uzywamy do formatowania i zwracania tytulu artykulow
                        title = soup.title.string.strip()
                        print(title)
                        print("https://www.ppe.pl", i, sep="")
                        print("-" * 50)
        elif wybor == "2":
            klucz = input("Podaj slowo kluczowe: ")
            print("#" * 50)
            for strona in range(1,6):
                x = requests.get(f"https://www.ppe.pl/filmy-seriale?type=article&page={strona}")
                output = re.sub(r" ", "", x.text)
                matches = re.findall(rf'/news/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE)
                if matches:
                    for i in matches:
                        url = "https://www.ppe.pl" + i.rstrip('"')
                        response = requests.get(url)
                        soup = BeautifulSoup(response.text, "html.parser")
                        title = soup.title.string.strip()
                        print(title)
                        print("https://www.ppe.pl", i, sep="")
                        print("-" * 50)
        elif wybor == "3":
            klucz = input("Podaj slowo kluczowe: ")
            print("#" * 50)
            for strona in range(1,6):
                x = requests.get(f"https://premieryksiazkowe.pl/spizarnia-mola/newsy/page/{strona}/?df_blog") 
                output = re.sub(r" ", "", x.text)
                matches = re.findall(rf'https://premieryksiazkowe.pl/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE)
                if matches:
                    for i in matches:
                        url = i.rstrip('"')
                        response = requests.get(url)
                        soup = BeautifulSoup(response.text, "html.parser")
                        title = soup.title.string.strip()
                        print(title.rstrip('⋆ Premiery książkowe. Nowości warte czytania')) # Tutaj dolozylem rstrip zeby usuwal trekst ktory z jakiegos powodu zawsze byl dodawany po tytule artykulow z tej strony
                        print(i.rstrip('"'))
                        print("-" * 50)
        elif wybor == "0":
            break
        else:
            print("Bledna opcja")

def menu():

    katalog = Katalog()

    while True:
        print("""
 ______________________________________________
|       Katalog Filmow / Ksiazek / Gier        |
|                                              |
|1. Wyswietl kategorie                         |
|2. Dodaj pozycje                              |
|3. Usun pozycje                               |
|4. Ocen pozycje                               |
|5. Newsy                                      |
|                                              |
|0.Koniec                                      |
|______________________________________________|
""")
        wybor = input("Wybor: ")

        if wybor == "1":
            lista = katalog.wybierz_liste()
            if lista:
                katalog.pokaz(lista)
        elif wybor == "2":
            katalog.dodaj()
        elif wybor == "3":
            katalog.usun()
        elif wybor == "4":
            katalog.ocen()
        elif wybor == "5":
            newsy()
        elif wybor == "0":
            break
        else:
            print("Bledna opcja")

menu()
