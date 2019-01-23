lista=[17, 5, 3, 5, 24, 8, 21, 7, 23, 12, 7, 6, 17, 7, 5, 7, 6]
print(lista)
print("lista sklada się z {} elementów".format(len(lista)))
def podziel_liste(calosc, dlugosc):
    kawalki = []
    for start in range(0, len(calosc), dlugosc):
        kawalek = calosc[start:start+dlugosc]
        kawalki.append(kawalek)
        if len(kawalek)<4:
            for i in range(4 - (len(kawalek))):
                kawalek.append(0)#uzupełnienie listy do odpowiedniej ilości elementów 
    return kawalki
#print(podziel_liste(lista,4))#wyswietli macierz w nawiesie trzeba wpisać nazwę listy do edycji i ilość elementów
for kawalek in podziel_liste(lista, 4):#w nawiasie nazwa listy do podziału i ilość elementów
    # w każdej nowej liście liczba musi być taka sama jak przy warunku if powyżej i pętli for
    print(kawalek)#wyswietli kilka list jedna pod drugą
#https://pl.python.org/forum/index.php?action=printpage;topic=6219.0
"""
#blok = lista[:4]
#blok=lista.split(";",3)
#blok=len(lista)%4
#print(len(lista))
#s.center(długość) – centruje napis w polu o podanej długości (uzupełniając spacjami)
#s.rjust(długość) – wyrównuje do prawej w polu o podanej długości (uzupełniając spacjami)
a=len(lista)#zlicza ilość elementów listy
b=(a//4)+1#floor division (podłoga) dzielenie bez reszty zaokrągla w dół
k=[]
k2=[]
k3=[]
k4=[]
k5=[]
for i in range(b):
    pass
for j in range(4):
    k.append(lista[j])
for v in range(4):
    v=v+4
    k2.append(lista[v])
for s in range(4):
    s=s+8
    k3.append(lista[s])
for p in range(4):
    p=p+12
    k4.append(lista[p])
for q in range(4):
    pass
    #q=q+16
    #k5.append(lista[q])
"""

"""
print(k)
#print(len(k))
print(k2)
print(k3)
print(k4)
print(k5)

utworzenie 10 pustych list nie działa
[ [] for x in range(10) ]
"""
"""
#https://pl.python.org/forum/index.php?action=printpage;topic=6219.0
#dzieli liste na kilka krótszych po 4 elementy każda działa
for start in range(0, len(lista), 4):  # dla każdej liczby od 0, mniejszej niż długość napisu, wybieraj po 4 liczbe
    print(lista[start:start+4])
"""
