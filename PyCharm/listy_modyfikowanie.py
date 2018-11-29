"""
modyfikowanie list
"""
#dołączenie kilku elementów do listy
lista1=[1,2,3,4]
lista2=lista1 + [5,6,7,8]
print(lista2)#[1, 2, 3, 4, 5, 6, 7, 8]
#łączenie dwóch list
lista3=lista1 + lista2
print(lista3)# [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8]

#sortowanie listy od min do max
#nazwa_listy.sort()
lista3.sort()
print(lista3)#[1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8]

#sortowanie odwrócona klejność od max do min
lista3.reverse()
print(lista3)#[8, 7, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1]

#dodawanie elementu na koniec listy
lista1.append(123)
print(lista1) # [1, 2, 3, 4, 123]

#dodawanie elementu na wybraną pozycję
lista1.insert(2,55)
print(lista1)
# [1, 2, 55, 3, 4, 123] 55 wchodzi na 2 pozycję(numeracja od zera )
# a to co było na pozycji 2 przeskakuje na pozycję 3. zwiększamy ilość pozycji listy o +1

#usunięcie ostatniego elementu listy
lista1.pop()
print(lista1) #[1, 2, 55, 3, 4]

#usunięcie wybraneo elementu listy(nie pozycji nr)
lista1.remove(55)
print(lista1) # [1, 2, 3, 4]
#usunięcie elementu o indeksie nr(podajemy nr pozycji np [1])
del lista1[1]
print(lista1) # [1, 3, 4]
#usunięcie kilku elementów podajemy indeks od pozycji do pozycji podanej ale -1
del lista1[1:3]
# podanie indeksy większego niż jest faktycznie nie pokazuje jako błąd
print(lista1)# [1]