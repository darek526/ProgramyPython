"""
Pętla while
"""
#I przykład
x=0#deklarujemy zmienną początkową
while x<6:
    # warunek do spełnienia aby pętla była wykonywana
    x +=1 # inny zapis x=x+1 dodajemy 1 do x
    # blok kodu: instrukcje które będą wykonywane wewnątrz pętli
    # do momentu kiedy warunek przy while będzie prawdziwy
    print(x)
    a=1
    while a<5:#zagnieżdżenie pętli w pętli
        a *=2#a=a*2 gdyby wybrać a=0 dojdzje do stworzenia pętli nieskończonej nigdy się nie skończy
        print("\ta="+str(a))
        #aby porawnie wyświetlić 2 łańcuchy (+)
        # musimy zamienić a które jest int na łąńcuch str \t dodaje tabulator
        # print("a=",a) #tak jest ok
"""
najpierw sprawdzany jest warunek przy pierwszej pętli
jest spełniony x<6
jesli jest spełniony dodaje 1 do x wypisuje wynik(1),
przechodzi do 2 pętli sprawdza warunek czy a<5 tak (x=0)
jeśli jest spełniony mnoży a *2 wypisuje wynik (a=2)
wracamy do początku 2 pętli sprawdzamy czy a<5  tak
mnożymy 2*2 wypisuje wynik (a=4)
wracamy do początku 2 pętli sprawdamy warunek  czy a<5 tak
mnozymy 4*2 wypisujemy wynik (a=8)
wracamy do początku 2 pętli sprawdzamy warunek czy a<5 nie
wykonywanie petli 2 zostaje zakończone.
Teraz wracamy do pętli 1 sprawdzamy warunek czy x<6 tak(x=1)
dodaje 1 do x wypisuje wynik(2) przechodzi do 2 pętli i znów mnoży przez 2 
najpier 1 *2=2 itd.
1
	a=2
	a=4
	a=8
2
	a=2
	a=4
	a=8
3
	a=2
	a=4
	a=8
4
	a=2
	a=4
	a=8
5
	a=2
	a=4
	a=8
6
	a=2
	a=4
	a=8
"""
# II przykład
a=2
while a<9:
    a*=2# a=a*2
    print("a=",a)# zapis bez konwersji
    x=1
    while x<4:
        x+=1
        print("\t x="+str(x))
        #konwersja x na łańcuch znaków str \t dodaje tabulator
"""
a= 4
	 x= 2
	 x= 3
	 x= 4
a= 8
	 x= 2
	 x= 3
	 x= 4
a= 16
	 x= 2
	 x= 3
	 x= 4"""

