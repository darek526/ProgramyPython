# !/usr/bin/python3
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
for nr, kawalek in enumerate(podziel_liste(lista, 4)):#w nawiasie nazwa listy do podziału i ilość elementów
    # w każdej nowej liście liczba musi być taka sama jak przy warunku if powyżej i pętli for
    print("kawalek{} =".format(nr+1),kawalek)#wyswietli kilka list jedna pod drugą