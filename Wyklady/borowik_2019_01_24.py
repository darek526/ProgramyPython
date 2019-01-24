"""
logowanie do wirtualnego środowiska
"""
class Klasa(object):#Klasa dziedziczy po object
    def __init__(self):# inicjalizcja funkcja która jest uruchamiana self
        self.n = 5 # pole klasy zmienna lokalna
    def funkcja(self, parametr):#self inf dla interpretera że jest to funkcja tej klasy
        self.n = parametr
    def drukuj(self):#wydruk na ekran
        print(self.n)
    def zwieksz(self):
        self.n = self.n + 2
    @staticmethod#dekorator
    def metoda_statyczna(parametr):#dotyczy wszystkich obiektów m i k
        print("Parametr: " + str(parametr))

print(type(k))#sprawdzenie typu wynik <class '__main__.Klasa'>
k = Klasa()
k.drukuj()
k.metoda_statyczna(10)

m = Klasa()
m.zwieksz()
m.drukuj()
k.drukuj()
m.metoda_statyczna(7)
"""
5
Parametr: 10
7
5
Parametr: 7
"""
