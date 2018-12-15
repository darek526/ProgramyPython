"""
zbiór wartości
nie posiada indeksu
zawiera pary klucz-wartość
dane z możliwością edycji
"""

slownik = {"klucz1":1, "klucz2":2}
print(slownik)# wyświetli cały słownik
# {'klucz1': 1, 'klucz2': 2}
print(slownik["klucz1"])#szukanie poszczeólnych wartości po kluczu
#1

# po kluczu mozemy nadpisać nową wartość
slownik["klucz1"] = 33
print(slownik)
# {'klucz1': 33, 'klucz2': 2}

#dodanie nowej wartości
slownik["klucz3"] = "nowy"
print(slownik)

#wielokrotne użycie takiego samego klucza wyświetli
# tylko 1 ostatnią(najnowszą wartoś) pary klucz-wartość
#dlatego kazdy klucz musi być inny

#usuwanie klucza i wartości
del slownik["klucz1"]
print(slownik)
# {'klucz2': 2, 'klucz3': 'nowy'}
# użycie print(slownik["klucz1"]) wyrzuci błąd zartzyma program
# aby sprawdzić w bezpieczny sposób czy klucz istnieje i zobaczyc jego zawartość:

print(slownik.get("klucz"))
# None (info o braku takiego klucz)
# jeśli klucz istnieje wyswietli jego zawartość

#aby dodać kilka kluczy z ich wartościami lub zmienić wartość istniejąceg:

slownik.update({
    "klucz2":"kot",
    "klucz4":3.14,
    "klucz5":True
})
print(slownik)
# {'klucz2': 'kot', 'klucz3': 'nowy', 'klucz4': 3.14, 'klucz5': True}

#wyświetlenie tylko  samych wartości za pomocą pętli for
for klucz in slownik:#zamiast słowa klucz możemy użyc np i s lub innego znaku
    print(slownik[klucz])#ten sam znak który jest po fo musi być w []
"""
kot
nowy
3.14
True
"""

#możemy wyswitlić tylko same wartości w postaci listy
print(slownik.values())
# dict_values(['kot', 'nowy', 3.14, True])

#Wyswietlenie tylko samych kluczy w formie listy:
print(slownik.keys())
# dict_keys(['klucz2', 'klucz3', 'klucz4', 'klucz5'])