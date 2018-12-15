"""
for wartość in zestaw_wartość:
    blok do wykonania
    zrób coś
"""
lista = [1, 2, 3, 4, 5]
for q in lista:# a lub dowolna inna litera
    print(q)#wypisuje kolejno wszystkie elementy listy:
"""
1
2
3
4
5
"""
# for break
for s in lista:
    if s >= 4:
        #gdy s osiągnie wartość 4 pętla zostanie zatrzymana
        break
    print(s)
"""
1
2
3
"""

#for range
for i in range(4):#jedna wartość zakres od 0 do liczba -1
    print(i)
"""
0
1
2
3
"""
for i in range(2,4):# dwie liczby zakres od  pierwszej do drugiej -1
    print(i)
"""
2
3
"""
for i in range(1, 4, 2):# trzy liczby pierwsz początek zakresu druga -1 koniec
    # trzecia krok o jaki będziemy zwiększać nasz licznik tu +2
    print(i)
"""
1
3
"""
#trójkąt z gwiazdek
for i in range(10):#zakres od 0 do 10-1
    print("*" * i)#mnozymy string przez kolejne wartości i
"""

*
**
***
****
*****
******
*******
********
*********
odwrócone
for i in range(10,1,-1)
"""