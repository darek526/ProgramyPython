"""
Operacje na plikach
"""
#tworzenie nowego pliku
zapis=open("plik3.txt", "w") #otwiera plik gdy nie istnieje tworzy plik3.txt
zapis.write("pierwasza linia tekstu\n")#dodanie pierwszej linii tekstu i kolejnych
zapis.write("druga linia tekstu\n")
zapis.write("trzecia linia tekstu\n")
zapis.write("czwarta linia tekstu\n")
zapis.write("piąta linia tekstu\n")
zapis.write("6 linia tekstu\n")
zapis.close()#zamknięcie pliku obowiązkowo

#otwieranie i wyświetlenie pliku
zapis=open("plik3.txt", "r") #otwieramy plik3.txt
zawartosc= zapis.read() # podstawienie  pliku zapis do zmiennej zawartosc i odczyt
print (zawartosc)#wydruk na ekran zawartosci pliku
zapis.close()#zamknięcie pliku obowiązkowo

#dodawanie danych do pliku
zmiana=open("plik1.txt", "a")#otwieramy plik1.txt
zmiana.write("dodajemy cyfry: \n 1233 \n67879")#dodajemy linie np:z cyframi
zmiana.close()#zamykamy plik

#ponowne wyświetlenie zawartości plik1.txt
f=open("plik1.txt", "r")#otwieramy plik1.txt
print(f.read())#odczyt i wyświetlenie w jednej linii
f.close()#zamknięcie pliku
