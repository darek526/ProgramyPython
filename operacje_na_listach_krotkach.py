"""
operacje na listach i krotkach
lista=[1,2,3]
krotka=(1,2,3)
"""
#informacja o nr indeksu(pozycji na liście) podanego elementu
lista1=[1,2,3,4,56,2, 3]
print(lista1.index(56))# 4
# element o nazwie 56 znajduje się pod indeksem nr 4

#sprawdzenie ile razy wystepuje wybrany element
print(lista1.count(22))# 2
#cyfra 3 występuje 2 razy brak elementu 0

#sprawdzenie z ilu elementów składa się nasz lista
print(len(lista1))# 7
#liczy nie indeks(od 0) tylko liczy element(od 1)