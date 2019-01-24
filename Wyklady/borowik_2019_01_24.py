"""
logowanie do wirtualnego środowiska
"""
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
"""
"""
polimorfizm
"""
"""
class Zwierze(object):
    def porusza_sie(self):
        print("porusza się")
    def przedstaw_sie(self):
        print("Ja jestem zwierze  ")
class Ssak(Zwierze):
    def porusza_sie(self):
        print("biegne")
    def przedstaw_sie(self):
        print("Ja jestem ssakiem")
class Ptak(Zwierze):
    def porusza_sie(self):
        print("lecę")
    def przedstaw_sie(self):
        print("Ja jestem ptakiem")
class Ryba(Zwierze):
    def porusza_sie(self):
        print("pływam")
    def przedstaw_sie(self):
        print("Ja jestem rybą")
    def run(self,struktura):# uruchamia funkcje klasie
        pass

zwierzeta = [ Zwierze(), Ptak(), Ssak(), Ryba(), Ptak()]
for zwierze in zwierzeta:
    zwierze.przedstaw_sie()
    zwierze.porusza_sie()
Ja jestem zwierze  
porusza się
Ja jestem ptakiem
lecę
Ja jestem ssakiem
biegne
Ja jestem rybą
pływam
Ja jestem ptakiem
lecę
"""
"""

"""
lista =[2,3,54,6,7,8,9,6,4,]
print(lista[::3])# co 3 element listy
#dowolna liczba parametru funkcji
def funkcja(x,y,*param):
    print(x)
    print(y)
    print(list(param))
    return x,y
a,b=funkcja(5,3,5,7,3,2,3,4,5)
print(a)
print(b)
"""
[2, 6, 9]
5
3
[5, 7, 3, 2, 3, 4, 5]
5
3
"""
def rozszerzony_alg_Euklidesa(a,b):
    u=1
    w=a
    x=0
    z=b
    while w:
        if w<z:
            q=u
            u=x
            x=q
            q=w
            w=z
            z=q
        q=w//z
        u-=q*x
        w-=q*z
    if z==1:
        if x<0:
            x+=b
        return x#istnieje rozwiązanie liczba w przedziale[0,b-1]
    else:
        return -1#nie istnieje
print(rozszerzony_alg_Euklidesa(5,7))#3

#wyjątki
try:
    5+"5"
except TypeError as er:
    print(er)#unsupported operand type(s) for +: 'int' and 'str'
    #print("Niezgodne typy int i str") bez as er po ATyeError
# tam gdzie wystapi błąd nie przerywa programu tylko dostajemy info o błędzi

#dzielenie przez 0
try:
    4/0
except ZeroDivisionError as err:
    print(err)
    #print("Nie dzielimy przez 0")
else:
    print("Dzielenie wykonano ok")
finally:
    print("zawsze wyświetli ten komunikat")
#generowanie własnych wyjątków
def wyjatek(text):
    print(text)

odpowiedz="tak"
try:
    if odpowiedz=="tak":
        raise wyjatek("Zła odpowiedź")
except:
    print("Niestety żle")#Niestety żle
else:
    print("Dobra odpowiedź")
