# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
def suma():
    a=int(pobierz_a.get())
    b=int(pobierz_b.get())
    dodawanie=a+b
    wynik= "suma {} + {} \nwynosi {}".format(a,b,dodawanie)
    label_2=Label(okno, bg="silver")
    label_2["text"]=wynik
    label_2.grid(row=2,column=1)
def roznica():
    a=int(pobierz_a.get())
    b=int(pobierz_b.get())
    odejmij=a-b
    wynik= "Różnica {} - {}\nwynosi {}".format(a,b,odejmij)
    label_2=Label(okno,bg="silver")
    label_2["text"]=wynik
    label_2.grid(row=3,column=1)
okno=Tk()
#definiowanie etykiet
etykiet_a=Label(okno, text ="wpisz wartość a: ",bg="gold")
pobierz_a=Entry(okno,bg="yellow")
etykiet_b=Label(okno, text ="wpisz wartość b: ",bg="gold")
pobierz_b=Entry(okno,bg="yellow")
#definiownie przycisków
przycisk1=Button(okno, text="dodaj a do b", bg="red", command=suma)
przycisk2=Button(okno, text="odejmij a od b",bg="green", command=roznica)
#położeni etykiet
etykiet_a.grid(row=0, column=0)
pobierz_a.grid(row=0, column=1)
etykiet_b.grid(row=1, column=0)
pobierz_b.grid(row=1, column=1)
#położenie przycisków
przycisk1.grid(row=2, column=0)
przycisk2.grid(row=3,column=0)
okno.mainloop()
