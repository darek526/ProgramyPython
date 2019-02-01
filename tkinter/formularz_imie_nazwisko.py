# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
okno=Tk()

#definiowanie etykiet
etykieta_imie = Label(okno,text = "Imię",bg = "green")
etykieta_nazwisko = Label(okno,text = "Nazwisko", bg = "green")

#definiowanie pola do wpisywania
pobierz_imie = Entry(okno, bg = "yellow")#pole do wpisywania imienia żółte tło
pobierz_nazwisko = Entry(okno, bg = "yellow")#jw tylko do nazwiska

# .grid() pozostawienie pustych() wszystkie 4 pozycje zostaną wypisane jedna pod drugą
etykieta_imie.grid(row = 0, sticky =E)#podanie pozycji wiersz 0
# sticky wyrównuje tekst do E(East)[wschód] czyli do prawej strony W do lewej
# sticky = N+E+W+S wyśrodkuje tekst w bloku
etykieta_nazwisko.grid(row = 1)#podanie pozycji wiersz 1
pobierz_imie.grid(row = 0, column = 1)#podanie pozycji wiersz 0 kolumna 1(0 kolumna [blok pionowy]
# to etykieta_imie) podanie 0 lub pominięcie pole wpisywanie imienia zakryje etykietę imię
pobierz_nazwisko.grid(row = 1, column = 1)#podanie pozycji wiersz 1 kolumna 1

#tworzenie  okna zaznaczania opcji tutaj łączenia kolumn
c = Checkbutton(okno,text = "Zaznacz 2 kolumny")
c.grid()#na samym dole pole do zaznaczenia i jego opis
okno.mainloop()
