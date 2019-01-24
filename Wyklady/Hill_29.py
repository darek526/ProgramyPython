"""
Program pobiera tekst jawny szyfruje go szyfrem Hilla mod29, następnie deszyfruje.
Każdą literę koduje się jako numer: A = 0, B =1, ..., Z=25, !=26, ?=27, .=28 .
Blok n jest przedstawiany w postaci wektora o n wymiarach. 
Następnie jest mnożony przez macierz o wymiarach 4x4, modulo 29 (wartość wynika z liczby elementów w układzie).
Cała tablica traktowana jest jako klucz. Macierz jest odwracalna w Z29 tylko wtedy deszyfrowanie będzie możliwe.
"""

def zamiana_liter_na_cyfry():
    text_cyfry = []
    napis = (input("Wpisz tekst jawny, tylko 26 liter lub '? ! ':\n")).upper()  # pobiera napis i automatycznie zamienia małe litery na duże
    # napis= napis.upper() #można użyc tej lini wtedy nie dodajemy .upper() za input
    napis = " ".join(napis)  # oddziela każdy znak spacja, pozbywa sie spacji
    text = napis.split()  # zamiana łańcucha znaków napis string na listę text
    for i in range(len(text)):
        text_cyfry.append(ord(text[i]) - 65)
    return text_cyfry
#zamiana_liter_na_cyfry()
def podziel_liste(calosc, dlugosc):
    kawalki = []
    for start in range(0, len(calosc), dlugosc):
        kawalek = calosc[start:start + dlugosc]
        kawalki.append(kawalek)
        if len(kawalek) < 4:
            for i in range(4 - (len(kawalek))):
                kawalek.append(0)  # uzupełnienie listy do odpowiedniej ilości elementów
    return kawalki
print(podziel_liste(zamiana_liter_na_cyfry(),4))#wyswietli macierz w nawiesie trzeba wpisać nazwę listy do edycji i ilość elementów
#for nr, kawalek in enumerate(poziel_liste(lista, 4)):  # w nawiasie nazwa listy do podziału i ilość elementów
    # w każdej nowej liście liczba musi być taka sama jak przy warunku if powyżej i pętli for
 #   print("kawalek{} =".format(nr + 1), kawalek)  # wyswietli kilka list jedna pod drugą
def szyfruj():

    klucz_cyfry =[]
    klucz="sgsgcgvcshsys"
    klucz=klucz.upper()#zamiana na duże litery
    klucz= " ".join(klucz)  # oddziela każdy znak spacja, pozbywa sie spacji
    klucz = klucz.split()  # zamiana łańcucha znaków napis string na listę text
    for i in range(len(klucz)):
        klucz_cyfry.append(ord(klucz[i]) - 65)
    return klucz_cyfry
#print("klucz: ",szyfruj())
