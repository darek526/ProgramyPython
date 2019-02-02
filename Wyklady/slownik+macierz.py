#!/usr/bin/env python
import string
from numpy import matrix
import numpy as np
#tylko 3 litery
lista_liter = [] #tablica liter
lista_liczb = [] #tablica liczb
i = 0
'''tworzenie listy liter i liczb Z29'''
for c in list(string.ascii_lowercase):
    lista_liter.append(c)
    lista_liczb.append(i)
    i = i + 1
'''dodanie do angielskiego języka ascii trzech kolejnych znaków'''
lista_liter.append(" ")
lista_liter.append("." )
lista_liter.append("?")

lista_liczb.append(26)
lista_liczb.append(27)
lista_liczb.append(28)

print(lista_liter)
print(lista_liczb)
'''po wpisaniu tekstu jawnego następuje zamiana na liczby'''  
napis = str(input('Podaj tekst jawny ! trzy litery a-z:\n'))
zakodowany = []
for c in napis:
    zakodowany.append(lista_liter.index(c.lower()))
#print(zakodowany)

'''poniżej mnożenie macierzy gdzie matrixB to liczby z tektu jawnego'''
'''matrixA to klucz: GYBNQKURP , gdzie wyznacznik macierzy jest różny od 0.
Klucz w programie jest stały'''
matrixA = [[6, 13, 20], [24,16,17], [1,10,15] ] 
'''matrixB to wiadomość zmieniona z liter na cyfry tj z str na int'''
matrixB = [zakodowany]

'''matrixA * matrixB '''
matrix_mult = [[sum(x * y for x, y in zip(rows, cols)) for cols in zip(*matrixA)] for rows in matrixB]

'''dzielenie modulo 26'''
a = np.array(matrix_mult)
#print(a)
modulo = a%26
#print(modulo)

'''zamiana macierzy na listę'''
for m in modulo:
    #print(m)
    pass

'''zamiana cyfr na litery'''
odkodowany  = ""
for i in m:
    odkodowany = odkodowany + lista_liter[lista_liczb[i]]
print('Zaszyfrowany tekst to:\n',odkodowany)
print('Dziękujemy za uwagę i współpracę.\nDo zrobaczenia!!!')



