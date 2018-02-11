import random       #wywolanie funkcji random

random.seed()
a=random.randint(1,9)
licznik=1
print(a)
while 1:
    print("Podaj swoja cyfre")
    cyfra=input()
    cyfra=int(cyfra)

    if cyfra<a:
        print("Twoja liczba jest za mała")
        licznik+=1
    elif cyfra>a:
        print("Twoja liczba jest za duża")
        licznik+=1
    else:
        print("Brawo! Trafiłeś szóstkę za", licznik, "razem")
        break

