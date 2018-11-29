"""
słowniki:
zapisujemy zawartość w nawiasach {treść}
podobne do list ale dostęp do poszczególnych elementów odbywa się nie za pomocą indeksu(pozycji)
lecz za pomocą kluczy(umieszczamy je w 'treść' lub"treść" chyba że jest to cyfra np: 3)
następnie za każdym kluczem umieszczamy : za którym wpisujemy zawartość
    tekst w "tresc" lub 'tresc'
    cyfry 12
    całe listy [1,2,3] krotki (1,2,3)
poszczególne pary klucz zawartość oddzielamy ,
"""
slownik={"a":"b", "klucz":15, 3:(1,2,3,4)}
print(slownik) # {'a': 'b', 'klucz': 15, 3: (1, 2, 3, 4)}
#wyswietleni słownika może zmieniać kolejność elementów

#szukanie elmentów po kluczu
print(slownik['klucz']) # 15
# jeśli nazwa klucza to tekst uzywamy "" lun''

#info o ileości elementów w słowniku
print(len(slownik)) # 3
# 3 elementy b, 15, (1,2,3,4)

#wyswietlenie w formie listy tylko same  klucze słownika
print(list(slownik.keys())) # ['a', 'klucz', 3]

#sprawdzenie czy elment wystepuje w słoniku
print(7 in slownik) #False
# 7 nie ma w tym słowniku

#dodanie elementu do słownika
#nazwa_słownika ["nazwa_klucza"]="tekst" lub 45
slownik["c"]=7
print(slownik) # {'a': 'b', 'klucz': 15, 3: (1, 2, 3, 4), 'c': 7}
#print(15 in slownik)

#usunięcie elementu po kluczu tekst w '' lub ""
del slownik[3]
print(slownik) # {'a': 'b', 'klucz': 15, 'c': 7}
# klucz 3 to lista (1,2,3,4)

#kasowanie zawartości słownika
slownik.clear()
print(slownik) #{}
#pusty słownik

'''
#kasowanie całego słownika
del slownik
print(slownik)#NameError: name 'slownik' is not defined
#błąd bo del skasowało nam cały słownik
'''