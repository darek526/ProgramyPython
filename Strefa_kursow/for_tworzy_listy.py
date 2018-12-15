"""
Tworzymy szybko liste używając pętli for
"""
nowa_lista = [i for i in  range(9)]
#licznik poczatkowy = 0 fetla for po podanym liczniku
# w zakresie do 9(oczywiscie 9 to strażnik czyli 9-1
print(nowa_lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

#można ograniczyć zakres np.  od 3  do 9(straznik)
lista = [i for i in range(3,9)]
print(lista)
#[3, 4, 5, 6, 7, 8]

# w podanym zakresie okreslamy krok (ile dodajemy do licznika)
lista = [i for i in range(3,9,2)]
print(lista)
#[3, 5, 7]

#lista tylko z liczb parzystych
list = [i for i in range(2, 9) if i % 2 == 0]
print(list)
#wartości spełniające kryterium  po if zostaną dodane pozostałe zostaną pominięte
#[2, 4, 6, 8]

# lub w zakresie z krokiem spełniające warunek
lista = [i for i in range(2,9, 3) if i % 2!=0]
print(lista)
#[5]
# w zakresie od 2 do 9 krok +3  tylko liczby nieparzyste
# (reszta z dzielenia przez 2 różna od zera)