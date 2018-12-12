"""
while warunek:
    blok operacji

uwaga przy kostrułowaniu warunku należy uważać aby nie zapetlić
stworzyć warunku który zawsze będzie prawdziwy pętla nieskończona

while True:
    print("Pętla działa bez konca warunek True zawsze prawdziwy")
"""

liczba = 0
while liczba < 4:#sprawdza warunek czywartość zmiennej liczba jest mniejszy od 9
    print(liczba)#wyśietla wartość zmiennej liczba
    liczba +=1# dodajemy 1 do wartości zmiennej liczba i wracamy do warunku
"""
0
1
2
3
"""
liczba = 0
while liczba < 4:
    liczba += 1#zamienjając kolejnoś tych 2 lini o
    print(liczba)#w bloku otrzymamy inny wynik
"""
1
2
3
4
"""
#while break
liczba = 0
while liczba < 4:
    liczba += 1
    if liczba == 3:#jeśli liczba osiagnie wartość 3
        break # przerwij działanie petli
                # gdy warunek przy if będzie sspełniony(True
    print(liczba)
"""
1
2
"""

#while continue
liczba = 0
while liczba < 4:
    liczba += 1
    if liczba % 2 ==0:#jeśli wynik dzielenia tej liczby przez 2 wynosi 0
        continue #pomin wypisanie powróć na początek petli while
        # continue działa w tych wypadkch gdy spełniony jest warunek przy if
    print(liczba)#wypisze tylko liczby nieparzyste aby otrzymać tylko liczby
    # parzyste przy warunku if liczba % != 0:
    # lub if not(liczba % 2 == 0):
"""
1
3
"""
while True:#petla nieskończona
    numer = int(input("Podaj liczbę większą od 0:\n"))
    if numer < 0:
        print("Podałeś {} jest mniejsz od zera spróbuj jeszcze raz".format(numer))
        # spełnienie warunku przy if wyświetla info
        continue # continue powraca do  początku pętli while można pisać bez continue ale pierwszy warunek
        # musiałby wyglądać tak if numer > 0:
                                    #print("ok {} jest większe od zera").format(numer))
                                    #break
    elif numer == 0:
        print("Podałeś {} spróbuj jeszcze raz".format(numer))
        # spełnienie warunku przy if wyświetla info
        continue# ontinue powraca do  początku pętli while
    #można użyć instrukcji else ale należy pamiętać aby print i break
    # przesunć w prawo o 1 wcięcie
    # działa bez else bo w tym układzie odnosi się do linii gdzie
    # definiujemy zmienną numer która będzie wpisana z klawiatury
    print("ok {} jest większa od zera".format(numer))
    break#kończy działanie pętli nieskończonej while