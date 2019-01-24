
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
"""[2, 6, 9]
5
3
[5, 7, 3, 2, 3, 4, 5]
5
3
"""
