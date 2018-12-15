"""
Bardzo podobna do listy ale bez mozliwości edycji
"""
krotka = (1,2,35,"kot", False, "duży kot")

#wyswietlenie krotki
print(krotka)
#(1, 2, 35, 'kot', False, 'duży kot')

#iteracja krotki po elementach
for i in krotka:
    print(i)
"""
1
2
35
kot
False
duży kot
"""
#utworzenie krotki z fragmentu innej krotki
nowa = krotka[:4]
print(nowa)
#(1, 2, 35, 'kot')

#sprawdzenie czy wartość występuje( lub niewystepije) w krotce
#odpowiedź True False
print("kot" in nowa)
#True
print(1 not in nowa)
#False (pytanie było czy nie wystepuje a wystepuje)

#łączenie krotek
stara = (3.14, 2.4, "dom")
nowa_krotka = stara + nowa * 2 #łączymy 2 krotki w jedną
# wcześniej nowa zostaje zdublowana przez mnożenie
print(nowa_krotka)
# (3.14, 2.4, 'dom', 1, 2, 35, 'kot', 1, 2, 35, 'kot')

#zliczenie elementów krotki
print(len(nowa_krotka))
# 11

#Inny sposób tworzenia nowej krotki
suma = nowa_krotka + (99,33,"las")
print(suma)
#(3.14, 2.4, 'dom', 1, 2, 35, 'kot', 1, 2, 35, 'kot', 99, 33, 'las')

#tworzenie krotki z listy lub jej części
lista = [2, 3.14, "noc w lesie", 99, 3]
print(lista)
krotka = tuple(lista[:3])#tylko 3 pierwsze elementy listy
print(krotka)
# [2, 3.14, 'noc w lesie', 99, 3]
# (2, 3.14, 'noc w lesie')

#zliczenie ilość elementów krotki
print(len(krotka))
# 3


krotka2 = (2, -44, 2.3, 66, 342, 0.33)
print(min(krotka2))
# -44
print(max(krotka2))
# 342 (najweksza wartość krotki

#sumowanie wszystkich wartości krotki
print(sum(krotka2))
# 368.63

#przypisanie poszczególnych  wartości z krotki do zmiennych
#ilość zmiennych musi odpowiadać ilości elementów krotki

print(len(krotka2))#liczy ilość elementów krotki
#6
a, b, c, d, e, f = krotka2
print(b)
# 0.33
print(krotka2)
(2, -44, 2.3, 66, 342, 0.33)
#utworzenie listy z wartości krotki
listka = list(krotka2)
print(listka)
#[2, -44, 2.3, 66, 342, 0.33]

#sortowanie tylko listy
listka.sort()
print(listka)
#[-44, 0.33, 2, 2.3, 66, 342]