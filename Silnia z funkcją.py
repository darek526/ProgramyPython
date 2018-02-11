#silnia

#tu jest funkcja
def silnia(arg1):
    if arg1 > 1:
        return (arg1 * silnia(arg1 - 1))

    else:
        return 1
#koniec funkcji

wartosc=""
while not wartosc.isdigit():
    wartosc=input("Podaj wartosc dla ktorej chcesz wyliczyc silnie: ")

print("Silnia z twojej liczby wynosi: ", silnia(int(wartosc)))
