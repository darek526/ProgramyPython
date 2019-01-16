"""
-bloki kodu do wielokrotnego wykorzystania
-zestaw deklaracji które często się powtarzają
-kluczowe elementy języka
-liczne funkcje wbudowane oraz możliwość definiowania własnych
def nazw_funkcji(argumenty):
    deklaracje
"""
def suma(a,b):
    print(a + b)
suma(3,4)#7 musimy podać dwa argumenty w nawiasie brak jednego błąd programu
suma(23443,435)#23878
#aby uniknąć błedu nie wpisania argument funcji
# domyślna wartość argumentu
# mozna zdefiniować argument lub argumenty
def suma(a=2, b=3):
    print(a + b)
suma()# 5
suma(7)# 10
suma(4,9)# 13
# suma(,5) taki zapis wyrzuci błąd, musimy użyć tego spsobu zapisu:
suma(b=17)# 19
#suma(2, c=1, b=6) jeśli mamy więcej argumentów można stosować ten sposób
# zapisu, nie musimy pisać a=2 bo 2 będzie odczytana z pierwszej pozycji jako a

def moja_funkcja(a, *krotka, **slownik):#mozna podać tylko jedną wartość zostanie dopisan do a
    # później możemy podać dowolne wartości które zosatną wpisane w krotke
    # poźniej możemy podać klucze z ich wartościami zostaną wpisane w słownik
    # należy pamiętać o kolejności podawanych wartości nie można wymieszać wartości krotek i słownika
    print(a)
    print(krotka)
    print(slownik)
moja_funkcja(3.14, "wdw", 23, 11, True, klucz1=21, klucz2=22, klucz3="domek")
"""
3.14
('wdw', 23, 11, True)
{'klucz1': 21, 'klucz2': 22, 'klucz3': 'domek'}
"""
#można użyć pętli for do wypisanie wartości krotki i słownika:
def moja_2_funkcja(a, *krotka, **slownik):
    print(a)
    for i in krotka:
        print(i)
    for klucz in slownik:
        print(slownik[klucz])
moja_2_funkcja(3.14, "wdw", 23, 11, True, klucz1=21, klucz2=22, klucz3="domek")
"""
3.14
wdw
23
11
True
21
22
domek
"""

def dodawanie(a,b):
    return a+b, a*b, a-b # zwróc sume, iloczyn i różnice liczb a i b
    # wyniki zostaną podane w postacji krotki
    # koniec programu dodawanie, napisanie czegoś poniżej nie uruchomi się
x = dodawanie(3,4)
print(x)#wyświetli trzy wyniki w krotce (7, 12, -1)
print(x[2])#-1 Tylko pozycja nr 2 krotki x

#zmienne globalne i lokalne

x = 1#zmienna globalna
def moja_funkcja():
    x = 2#zmienne lokalne
    y = 3
    print(x,y)
moja_funkcja()#2 3
print(x) #1wywołanie tylko zmiennej globalnej
def moja_2_funkcja():
    global x#wywołanie zmiennej lobalnej zmiana x
    # wewnątrz tej funkcji zmini wartość x dla całego programu
    x+=1
    y=5
    print(x,y)
moja_2_funkcja()
print(x)# x=2
"""
2 5
2
"""
"""
Generatory funkcji, ułatwiają tworzenie iteratoróœ"""

def generator(a):
    for i in range(a):
        yield i+2
        #w generatorach zamiast return uzywamy instrukcji yield
"""for i in generator(4):
    print(i, end=", ")#2, 3, 4; 5,
    #standartowo funkcja print kończy się nową linią, można to zmienić funkcją end=""
    # end= anuluje nową linie a wartość w ""będzie użyte na końcu linii np ,.: spacja itd
#przypisanie generatora do zmiennej i użyć tej zmiennej jako argument funkcji next"""
# do sprawdzenia wartości utworzonej przez nasz generator
gen=generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
2
3
4
5
6
"""
