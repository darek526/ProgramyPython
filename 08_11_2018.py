"""
Operacje na plikach
"""
plik2=open("plik2.txt", "w") #otwier plik gdy nie istnieje tworzy taki plik
plik2.write("pierwasza linia tekstu\n")#dodanie pierwszej linii tekstu
plik2.write("druga linia tekstu\n")
plik2.write("trzecia linia tekstu\n")
plik2.write("czwarta linia tekstu\n")
plik2.write("piąta linia tekstu\n")
plik2.write("6 linia tekstu\n")
plik2.close()#zamknięcie pliku
plik2=open("plik2.txt","r")
zawartosc= plik2.read() # podstawienie  pliku do zmiennej zawartosc i odczyt
print (zawartosc)#wydruk na ekran zawartosci pliku
plik2.close()#zamknięcie pliku