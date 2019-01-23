lista=[17, 5, 3, 5, 24, 20, 8, 21, 7, 23, 12, 7, 6, 17, 7, 5, 7, 6]
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
print(lista)
print(len(lista))
print(k)
#print(len(k))
print(k2)
print(k3)
print(k4)
print(k5)
