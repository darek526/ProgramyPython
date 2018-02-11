print("***************************************************************************")
print("**              _____________________                                    **")
print("**             |  _________________  |                                   **")
print("**             | | 0 1  1  0  1  0 | |                                   **")
print("**             | |_________________| |                                   **")
print("**             |  ___ ___ ___   ___  |                                   **")
print("**             | | 7 | 8 | 9 | | + | |                                   **")
print("**             | |___|___|___| |___| |                                   **")
print("**             | | 4 | 5 | 6 | | - | |                                   **")
print("**             | |___|___|___| |___| |                                   **")
print("**             | | 1 | 2 | 3 | | x | |                                   **")
print("**             | |___|___|___| |___| |                                   **")
print("**             | | . | 0 | = | | / | |                                   **")
print("**             | |___|___|___| |___| |                                   **")
print("**             |_____________________|                                   **")
print("**                                                                       **")
print("**           KALKULATOR WARTOSCI BINARNYCH, DZIALANIA AND, OR i XOR      **")
print("**                                                                       **")
print("**    opracowali: asp. Sylwester Brozyna                                 **")
print("**                st. asp. Piotr Bakiewicz            WSPol 2017/18      **")
print("**                                                                       **")
print("***************************************************************************")

a=""
b=""
dzialanie=""

while a!=1 and a!=0:
    a=input("Podaj pierwsza wartosc, 0 lub 1: ")
    if a.isdigit():
        a=int(a)
        if a!=1 and a!=0:
            print("Podales bledna wartosc! Podaj 0 lub 1.")
    else:
        print("Podales litere lub znak! Musisz podac cyfre 0 lub 1.")
while b!=1 and b!=0:
    b=input("Podaj druga wartosc, 0 lub 1: ")
    if b.isdigit():
        b=int(b)
        if b!=1 and b!=0:
            print("Podales bledna wartosc! Podaj 0 lub 1.")
    else:
        print("Podales bledna wartosc! Musisz podac 0 lub 1.")
while dzialanie !=1 and dzialanie !=2 and dzialanie !=3:
    dzialanie=input("\nWybierz, ktora operacje chcesz wykonac: \n 1 - AND\n 2 - OR\n 3 - XOR\n 4 - Wyjscie\n\nTwoj wybor to: \n")
    if dzialanie=="1":
        print("\nWynik dzialania AND wynosi: ")
        print(a and b)
        break
    elif dzialanie =="2":
        print("\nWynik dzialania OR wynosi: ")
        print(a or b)
        break
    elif dzialanie =="3":
        print("\nWynik dzialania XOR wynosi: ")
        print(a ^ b)
        break
    elif dzialanie =="4":
        break
    else:
        print("\nZly wybor!\n")
        
print("Aby zakonczyc dzialanie programu kliknij dowolny klawisz")
input()
        
