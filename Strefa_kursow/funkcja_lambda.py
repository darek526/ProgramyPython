"""
Funkcja jednorazowa
"""
podwajanie = lambda a: a * 2
potegowanie = lambda a: a * a
print(podwajanie(7))#14
print(potegowanie(7))#49

#funkcja lambda jako element listy
lista=[(lambda  a:a*5),(lambda a:a*6),(lambda a:a*7)]
for i in lista:
    print(i(3))
"""
15
18
21
"""
print(lista[1](3))#wypisuje tylko pozycje nr 1 z listy#18
