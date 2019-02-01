# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *

okno=Tk()

etykieta1 = Label(okno, text = "etykieta 1", bg = "green")#zielone tło czarny napis
etykieta2 = Label(okno, text = "etykieta 2", bg = "red", fg = "green")
etykieta3 = Label(okno, text = "etykieta 3", bg = "black", fg = "yellow")#czarne tło żółty napis
etykieta4 = Label(okno, text = "etykieta 4", bg = "yellow", fg = "red")
etykieta5 = Label(okno, text = "etykieta 5\ndruga linia", bg = "blue", fg = "pink")

etykieta1.pack(fill = X)#wypełnij po osi x poziomy zielony pasek po całej szerokości
etykieta2.pack(side = LEFT,fill = Y)#wypełnij po osi Y pionowy czerwony pasek poniżej zielonego przy lewej krawędzi
etykieta3.pack(fill = X)# po osi X poziomy  czarny pasek od pionowego czerwoneo do prawej krawędzi
etykieta4.pack(side = RIGHT, fill = Y)# po osi Y pionowy żółty pasek przy prawej krawędzi poniżej czarneog
etykieta5.pack()#brak parametrów () kolor niebieski tylko tam gdzie tekst
okno.mainloop()
