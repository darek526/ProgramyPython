"""
listy to zbiory różnych zmiennych którym przyporządkowane są ich pozycje
numerowanie pozycji zaczynamy od 0
"""
moja_lista = [1, 2.2, True, None, "x", "Ala ma kota"]
#wyświetlenie całej listy:
print(moja_lista)
# [1, 2.2, True, None, 'x', 'Ala ma kota']
#Iteracja po elementach: wyswietlenie poszczególnych elementó listy
for i in  moja_lista:#wybiera element z listy
    print(i)# wyswietla ten element i wraca do kolejnego elementy
"""
1
2.2
True
None
x
Ala ma kota
"""
#zamiana istniejącego elementu na inny
# (stary kasuje na jego miejsce nadpisuje nowy
#wpisanie []indeksu większego niż posiada lista jest błędem
moja_lista[3] = "wtorek"
print(moja_lista)
#[1, 2.2, True, 'wtorek', 'x', 'Ala ma kota']

#METODY
#dodanie jednego nowegu elementu na koniec listy
moja_lista.append("sobota")
print(moja_lista)
#[1, 2.2, True, 'wtorek', 'x', 'Ala ma kota', 'sobota']
#odwrócenie kolejności listy
moja_lista.reverse()
print(moja_lista)
#['sobota', 'Ala ma kota', 'x', 'wtorek', True, 2.2, 1]
#sortowanie od wartości najmniejszej do największej
# sortuje tylko liczby
moja_lista2 = [32.4,21.6,4,77,33,9,5]
print(moja_lista2)
moja_lista2.sort()
print(moja_lista2)
"""
[32.4, 21.6, 4, 77, 33, 9, 5]
[4, 5, 9, 21.6, 32.4, 33, 77]
"""
#elementy listy
print(moja_lista)#cała lista
print(moja_lista[:2])#elementy o indeksie 0 i 1
print(moja_lista[3:])#od indeksu 3(liczy od 0) do kończ listy
"""
['sobota', 'Ala ma kota', 'x', 'wtorek', True, 2.2, 1]
['sobota', 'Ala ma kota']
['wtorek', True, 2.2, 1]"""

#łączenie dwóch list
moja_lista3 = moja_lista + moja_lista2
print(moja_lista3)
# ['sobota', 'Ala ma kota', 'x', 'wtorek', True, 2.2, 1, 4, 5, 9, 21.6, 32.4, 33, 77]
moja_lista4 = moja_lista * 2 + moja_lista2#moja lista będzie wpisana dwa razy
print(moja_lista4)
#['sobota', 'Ala ma kota', 'x', 'wtorek', True, 2.2, 1, 'sobota', 'Ala ma kota', 'x', 'wtorek', True, 2.2, 1, 4, 5, 9, 21.6, 32.4, 33, 77]

#zliczenie elementów listy
print(len(moja_lista4))
#21 tyle elmentów zawiera moja_lista4

#sprawdzenie czy konkretna wartość występije na liście
# odpowiedż: True False
print("wtorek" in moja_lista4)# czy wartość wtorek występuja w moja_lista4
# można użyć not in czy nie wystepuje
# True
print(3.14 in moja_lista4)# czy 3.14 wystepuje w liście
#False