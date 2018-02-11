print("")
print("                                                   ")
print("     Program liczacy ilosc dni ktore minely od Twoich urodzin :) ")
print("                                                              ")
print("     opracowali: asp. Sylwester Brozyna                      ")
print("                 st. asp. Piotr Bakiewicz        WSPol 2017/18   ")
print("                                                              ")

import datetime

dzis = now = datetime.datetime.now()
print(f'\nTeraz jest {now:%Y,%m,%d}\n')

r=int(input("Podaj rok urodzenia: ")) 
m=int(input("Podaj miesiąc urodzenia: "))
d=int(input("Podaj dzień urodzenia: "))

urodziny = datetime.datetime(r, m, d)

while urodziny > dzis:
    if urodziny > dzis:
        print("\nPodales date ktora jeszcze nie nastapila\n")
        break
while m < 1 or m > 12:
    if m < 1 or m > 12:
        print("\nBledna data. Podany miesiac nie istnieje.\n")

while d < 1 or d > 31:
    if d <1 or d > 31:
        print("\nBledna data. Podany dzien nie istnieje.\n")

wynik = dzis - urodziny
print ("\nOd twoich urodzin minelo: ", wynik)

print("\nAby zakonczyc dzialanie programu kliknij dowolny klawisz\n")
input()


