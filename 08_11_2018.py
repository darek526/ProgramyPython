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
zapis=open("plik3.txt", "r") 
#otwieramy plik3.txt z parametrem „r” – Odczyt danych z pliku tekstowego.
zawartosc= zapis.read() # podstawienie  pliku zapis do zmiennej zawartosc i odczyt
print (zawartosc)#wydruk na ekran zawartosci pliku
zapis.close()#zamknięcie pliku obowiązkowo

#dodawanie danych do pliku
zmiana=open("plik1.txt", "a")
#otwieramy plik1.txt z parametrem „a” – Dopisanie danych do pliku.
# Jeśli plik nie istnieje, zostaje stworzony.
zmiana.write("dodajemy cyfry: \n 1233 \n67879")#dodajemy linie np:z cyframi
zmiana.close()#zamykamy plik

#ponowne wyświetlenie zawartości plik1.txt
f=open("plik1.txt", "r")
#otwieramy plik1.txt z parametrem „r” – Odczyt danych z pliku tekstowego.

print(f.read())#odczyt i wyświetlenie w jednej linii
"""Rożne możliwości wyswietlanai, edycji zawartości pliku
    read([rozmiar]) – Odczytuje całą zawartość pliku, jeśli podamy argument, odczyta tylko wskazaną przez niego ilość znaków.
    readline([rozmiar]) – Odczytuje jedną linię z pliku, jeśli podany argument, odczyta tylko wskazaną liczbę znaków z bieżącej linii.
    readlines() – Odczytuje wszystkie linie z pliku i zwraca jako listę.
    write(dane) – Zapisuje „dane” do pliku.
    writelines(dane) – Zapisuje listę „dane” do pliku.
"""
f.close()#zamknięcie pliku
