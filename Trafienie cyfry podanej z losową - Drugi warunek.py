import random       #wywolanie funkcji random

random.seed()

while 1:

    print("Podaj liczbe od ktorej bedzie zaczynal sie zakres")
    poczatek=int(input())
    #lub krocej: koniec=input("Podaj poczatek zakresu") zamiast dwoch wierszy

    print("Podaj liczbe koncowa zakresu") 
    koniec=int(input())

    if poczatek>koniec:
        print("a>b")
    else:
        break

a=random.randint(poczatek,koniec)
licznik=0     # uruchomienie licznika i jego wyzerowanie

while 1:
    print("Podaj liczbe z podanego zakresu")
    cyfra=input()     # wczytanie liczby
    cyfra=int(cyfra)  # można w jednej linii: cyfra=int(input())

    licznik+=1   # licznik o 1 w górę przed każdą pętlą
    if cyfra<a:
        print("Twoja liczba jest za mała")
    elif cyfra>a:
        print("Twoja liczba jest za duża")
    else:
        print("Brawo! Trafiłeś liczbe za", licznik, "razem")
        break   # zakończenie pętli po trafieniu ==

    

