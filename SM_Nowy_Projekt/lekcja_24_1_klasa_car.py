class SamochodOsobowy:
    przyspieszenie = 10 # Atrybut klasowy

    def __init__(self, numer_rejestracyjny): # Konstruktor (metoda specjalna)
        self.numer_rejestracyjny = numer_rejestracyjny
        self.czy_w_ruchu = False
        self.predkosc = 0
    
    def jedz(self):
        self.czy_w_ruchu = True

    def przyspiesz(self):
        self.predkosc += self.przyspieszenie
        self.czy_w_ruchu = True

    def stop(self):
        self.predkosc = 0
        self.czy_w_ruchu = False

honda = SamochodOsobowy("CB 167HY")
print("Obiekt SamochodOsobowy (honda:)", honda)
print("Numer rejestracyjny (honda):", honda.numer_rejestracyjny)
print("Czy honda jedzie:", honda.czy_w_ruchu)
#honda.jedz() # Przenieslismy cialo def jedz do def przyspiesz
#print("Czy honda jedzie:",honda.czy_w_ruchu)
print("Predkosc (honda):", honda.predkosc)
honda.przyspiesz()
print("Predkosc (honda):", honda.predkosc)
print("Czy honda jedzie:", honda.czy_w_ruchu)
honda.stop()
print("Predkosc (honda):", honda.predkosc)
print("Czy honda jedzie:", honda.czy_w_ruchu)
honda.przyspiesz()
honda.przyspiesz()
honda.przyspiesz()
print("Czy honda jedzie:", honda.czy_w_ruchu)
print("Predkosc (honda):", honda.predkosc)
honda.stop()
print("Czy honda jedzie:", honda.czy_w_ruchu)
print("Predkosc (honda):", honda.predkosc)
