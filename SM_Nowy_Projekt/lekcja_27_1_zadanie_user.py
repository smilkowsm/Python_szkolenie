""" Zadanie (User):
 
Stwórzcie klase User która przyjmuje imię, nazwisko, email oraz sprawdza czy
email został podany prawidłowo (Czy w naszym emailu znajjduje sie @)
Przykład:
user@wp.pl
 
userwp.pl
'Podałeś wadliwy email.'
 
Stworzona do tego niech jest metoda statyczna is_valid_email
 
Dodatkowo wykożystajcie __str__
 
Następnie stwórzcie klase Admin i utworzcie hierarchię klas Uzytkownik
Administrator
 
Dodajcie argument superhasło do klasy admin.
 
"""
class User:

    def __init__(self, imie, nazwisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        

    @staticmethod
    def is_valid_email(email):
        if "@" not in email:
            return "Podałeś wadliwy email."
        else:
            return email

uzytkownik = User("Sebastian", "Milkowski", "smilkowski@wp.pl")


print(uzytkownik.imie)
print(uzytkownik.nazwisko)
print(uzytkownik.email)
print(uzytkownik.is_valid_email("smilkowskiwp.pl"))

class Admin:



    pass