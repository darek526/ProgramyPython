'''
Dlugi komentarz kilka linii
'''
"""
Dlugi komentarz jw.
"""
#komentarz krotki 1 linia
#deklarowanie zmiennej liczbowej
a=21 #nie musimy deklarowac typu zmiennej
print(a) #wyświetla na ekranie wartosc zmiennej a
a=2.332#zmiana wartosci parametru a na liczbe zmiennoprzecinkowe
    #  pamietamy aby uzywac . nigdy ,
print(a) #ponowne wyswietlenie parametru a ale juz  zmienionego
b=3+5j #liczby zespolone
print(b) #wynik (3+5j)
dwojkowa = 0b1011 #liczby  w sytemie 2-ym zero b/B liczba binarna
print(dwojkowa) #wynik podaje w systemie 10-ym bedzie to 11
liczb_osemkowa=0o15 #0o15 zero litera o duza lub mala liczba w systemie 8-owym
#na ekranie zobaczymy wartosc liczby osemkowej15  ale przeliczona na system dziesietny 13
print(liczb_osemkowa)
liczba_16 = 0XABc
#0xabc zero litera x duza lub mala liczba w systemie 16-owym mozna uzywac malych i duzych liter
print(liczba_16)
#wyswietla 2748 bo jest to wartosc w systemie 10-nym  podanej liczby w systemie 16-ym

a, b, c=4, 5, 6 #deklarowanie kilku zmiennych jednocześnie
print(c)
a=(1, 2, 3)
(x, y, w)=a #tzw krotka definiowanie kilku zmiennych
print(w)
'''del (w) #usuwanie zmiennej
print(w) #zostanie wyswietlony komunikat o błedzie
'''
#ciagi znakowe
a="dowolny tekst "
'''Dane tekstowe umieszczamy miedzy "tekst" lub 'tekst'
znaki specyjalne:
\' apostrof
\t tabulator
\n nowa linia
'''
print(a)
dlugi_tekst='''kilka
lini
tekstu''' #mozna uzyc tez zamiennie """dlugi tekst"""
print(dlugi_tekst) #wyswietla tekst w kilku liniach
#laczenie wpisow
print(a+dlugi_tekst)
'''wynik polaczenie  przy uzyciu +
dowolny tekst kilka
lini
tekstu
'''
#powtarszanie lini *3
print(a*3)
#Łączenie i powtarzanie znaków
print("B"+"a"*5+"rdzo pyszne") #Baaaaardzo pyszne
