#szyfr podstawieniowy z użyciem słownika
import random
#utworzenie listy od 0 do256
kryptogram=""
a=list(range(256))
b=list(range(256))
slownik_szyfr={}
print(a)
#
random.shuffle(b)
#budowanie słownika z uzyciem list
for i in range(256):
    slownik_szyfr[i]=b[i]
print(slownik_szyfr)
wiadomosc_jawna=input("wprowadź wiadomość jawną\n")
for i in range(len(wiadomosc_jawna)):
    kryptogram=kryptogram + chr(b[ord(wiadomosc_jawna[i])])
print(kryptogram)