# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
okno=Tk()

def pisz(event):#event funkcja pisz pobiera zdarzenie z zewnątrz dalej zdefiniowane w .bind
    print("Dzień dobry")

przycisk = Button(okno,text = "Uruchom funkcję", bg = "red")
przycisk.bind("<Button-1>",pisz)
#bind(wydarzenie dla naszego przycisku) <Button-1>", pisz[lewy przycisk myszy uruchamia funkcje pisz.Prawyprzycisz myszy to -3]
przycisk.pack(side=LEFT)#lewastrona okna
#czerwony przycis uruchom funkcje naciśnięcie wypisze tekst Dzień dobry w terminalu
okno.mainloop()

"""
#inny sposób uruchomienia funkcji pisz
# !/usr/bin/python3
from tkinter import *
okno=Tk()

def pisz():
    print("Dzień dobry")
#po command wpisujem nazwę funkcji którą ma uruchomic nas przycisk
przycisk = Button(okno,text = "Uruchom funkcję", bg = "red", command = pisz)
przycisk.pack(side=LEFT)#lewastrona okna
#czerwony przycis uruchom funkcje naciśnięcie wypisze tekst Dzień dobry w terminalu
okno.mainloop()
"""
