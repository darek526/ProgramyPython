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
    
    
    
    
    finally:
    print("wykonuje się zawsze")
"""
"""
#inne wyjątki
def ulubione_lody(indeks):
    lody=["czekoladoe", "waniliowe", "truskawkoe"]
    return  lody[indeks]
try:
    print(ulubione_lody(-1))
#brak wartości w nawiasie lub wartość większ od wielkości listy błąd
except (IndexError,TypeError):#błąd brak w indeksi , bład typu ok jest tylko  int
    print("Nie ma takich lodów")
#otwieranie plików
"""
try:
    uchwyt_pliku=open("plik.txt", r)
except:
    print("Plik nie istnieje")
else:
    print(uchwyt_pliku.read())
finally:
    print("Dp zobaczenia")
"""
żródło algorytmów 
http://www.rosettacode.org
"""
#web scraping wyciąganie danych ze strony internetowej
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def czy_poprawna_odp(odpowiedz):
    zawartosc=odpowiedz.headers["Content-Tyoe"], lower()
    return (
            odpowiedz.sttus_code==200 and
            zawartosc is not None and
            zawartosc("html")>-1)
def otworz_url(url):
    try:
        with closing(get(url,stream=True)) as odpowiedz:
            if czy_poprawna_odp(odpowiedz):
                return odpowiedz.content
            else:
                return None
    except RequestException as err:
        print(err)
        print("Prawdopodobnie niedpowiedni link")
strumien=otworz_url("https://www.nbp.pl/home.aspx?f=/kursy/kursyc.html")
html=BeautifulSoup(strumien,"html.parser")
for i, li in enumerate(html.select("td")):
    if i>=111 and i<= 120:
        print(li.text)
#zawartosc=odpowiedz.headers
        print(odpowiedz)
