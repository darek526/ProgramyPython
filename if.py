"""
If else
"""

#if
if 1<2: #if warunek do spełnienia
    print ("prawda")#prawda

if 1: #jaka kolwiek wartość różna od zera
    #wpisanie zera brak napisu niespełniony warunek
    print("prawda")#prawda

if -451: #jaka kolwiek wartość różna od zera
    print("prawda")#prawda

if True: # wpisanie None brak napisu niespełniony warunek
    print("prawda")

if "tekst":
# napis jest przekładany na logiczne True nie jest to napis
#  pusty posiada w sobie akąś informację
    print("prawda")#prawda

x=True
y=False
if x or y: #dla x and y brak napisu bo taki zapis logiczn and daje false
    print("prawda") #prawda

#zagnieżdanie instrukcji
a=-1
if a<0:
    print("liczba ujemna") #liczba ujemna
    if a != -20:#różne od
        print("różne od -20")#różne od -20

