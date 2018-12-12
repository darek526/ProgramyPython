"""
my_tekst = " tekst"
my_tekst = 'tekst'
indeks to pozycja w ciągu znkowym zaczynamy liczyć od zera to pierwsza pozycja od lewej
"""
prefix = "Kurs"
nazwa = "Python"
print(prefix + nazwa)# KursPython
print(prefix + " " + nazwa) # Kurs Python(konkatenacja dwóch stringów
print(len(nazwa))# 6 (ilość elementów stringu)
print(nazwa[0])# P (zerowy indeks litera P)
slowo = "dzien dobry"
print(len(slowo))# 11 liczy również spacje
print(slowo.capitalize())# Dzien dobry (zamienia pierwszą litere pozycja 0 na dużą
print(slowo.title())# Dzien Dobry (zamienia w każdym słowie piewszą literę na dużą
name = "konkatenacja stringu"
print(name[0])#k(zerowa pozycjia to litera k pierwszy element bo liczymy od 0)
print(name[-1])#u(ostatni element)
print(name[0:4])#konk(wyświetla od 0 pozycji do 4 -1 można pominąć zero[:4])
print(name[3:6])# kat(od 3 pozycji do 6-1)
print(name[15:])#ringu( od nr 15 do końca)
print(name[15:-1])#ring(od 15 elementu do końca ale bez ostatniego

a = "abc"
print(a * 3)#abcabcabc
print(3 * a + " " + "koiec")#abcabcabc koniec

#metody sprawdzania string
#.islower(czy pierwsza litera jest mała)
slowo = "Dzien dobry"
print(slowo.islower())#False
print(slowo.isalnum())#False(czy są tylko litery lub cyfry nie bo jest spacja)
print(slowo.isalpha())#False(czy są tylko litery nie bo jest spacja)
print(slowo.find("D"))#0(info że znalazł literę D jest na 0(pierwszej pozycji)
print(slowo.find("c"))#-1(info że w tym ciągu znaków litera c nie występuj

print("z" in slowo)#True(info ze występuje jeśli nie to False)
print("z" not in slowo)#False(info ze lit z nie wystepuje )
