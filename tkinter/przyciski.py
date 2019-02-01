#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *

okno=Tk()

#ramki definiowanie góry dołu
gora_ramki = Frame(okno)
gora_ramki.pack()
dol_ramki= Frame(okno)
dol_ramki.pack(side = BOTTOM)
lewa_strona=Frame(okno)
lewa_strona.pack(side=LEFT)

#tworzenie przycisków
przycisk1 = Button(lewa_strona, text ="Przycisk 1", fg="black")
"""
przycisk1 nazwa przycisku info dla programu
Button funkcja definiująca przyciski
gora_ramki(dól,lewa lub prawa strona ramki) położenie przycisku górnej części ramki
zdefiniowanie położenia kilku przycisków góra dół lub prawa albo lewa strona 
spowoduje że te przyciski będą obok siebie
text funkcja opisująca przycisk
"Przycisk 1" nazwa na przycisku widoczna dla użytkownika działa \n znak nowej lini
fg definiownie czcionki
"green" napis będzie w kolorze zielonym
"""
przycisk2 = Button(lewa_strona, text ="Przycisk 2\n można używać\nznaku nowej lini", fg="brown")
przycisk3 = Button(gora_ramki, text ="Przycisk 3", fg="red")
przycisk4 = Button(gora_ramki, text ="Przycisk 4", fg="green")

#uruchomienie i lokalizacja przycisków względem siebie
#jeśli przy definiowaniu przycisku podamy położenie np gora ramki
# a przy .pack podamy BOTTOM przycisk będzie na samej górze ramki
# można pominąć opis w () wtedy przyciski będą jeden pod drugim domyślnie TOP
# nie nalęży przesadzać z ilości opisów (side=  )

przycisk1.pack(side=RIGHT)
przycisk2.pack()
przycisk3.pack()
przycisk4.pack()

okno.mainloop()
#4 przyciski na gorze po środku przycisk 3 pod nim przycisk 4
#środek przy lewej krawedzi przycisk 2(3 linie tekstu)z jego prawej strony przycisk 1
"""
# !/usr/bin/python3
from tkinter import *

okno = Tk()
#ramki
gorna_ramka = Frame(okno)
gorna_ramka.pack()

dolnaramka = Frame(okno)
dolnaramka.pack( side = BOTTOM )

#tworzenie przycisków
czerwonyprzycisk = Button(gorna_ramka, text ="Red", fg ="red")
czerwonyprzycisk.pack(side = LEFT)

zielonyprzycisk = Button(gorna_ramka, text ="Brown", fg="brown")
zielonyprzycisk.pack(side = LEFT)

zolty_przycisk = Button(gorna_ramka, text ="Blue", fg ="blue")
zolty_przycisk.pack(side = LEFT)

czarny_przycisk = Button(dolnaramka, text ="Black", fg ="black")
czarny_przycisk.pack(side = BOTTOM)

okno.mainloop()
# 4 przyciski
#Red Brown Blue w jednej linii na samej górze po środku
#Black na samym dole po środku
"""
