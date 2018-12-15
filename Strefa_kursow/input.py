#input funkcja umożliwia wpisywanie danych np do zmiennej
#input domyślnie zapisuje pobrane dane jako string
imie = input("Jak masz na imie? \n")
print("Witaj " + imie)#jesli imię mialoby inny typ niz string wystąpi błąd
# należałoby dokonać konwersji na string str(imie)
"""
Jak masz na imie?
Darek
Witaj Darek
"""
nazwisko = input("Podaj swoje nazwisko: \n")
print("Nazywasz sie ", nazwisko)#taki zapis umożliwia łączenie róznych typów zmiennych
"""
Formatowanie konwersaj różnych typów
zmiennych
"""
x = int(input("Podaj warość x: \n"))#Konwersja pobranej wartości do integer liczba całkowita
#x = float(input("podaj wartość x:\n")) konwersja pobranej wartości do float liczba zmienno przecinkowa
#\n znak nowej linii program sam przejdzie do nowej linii
x += 2#<=> x = x + 2(zwiększmy wartość z o 2)
print(x)#14
#print("wartość x wynosi: " + x)x jest int liczbą całkowitą "wartośc x wynosi" to ciąg znakóœ string
#nie można ich połączyć razem wystąpi błąd należy dokonać konwersji int na string
#str(wartość)
print("wartość x wynosi: " + str(x))
#print("Wartość x wynosi: ", x) #taki zapis umożliwia łączenie róznych typów zmiennych
print("wartość x wynosi {}".format(x))# za pomocą metody .format dokonujemy
# konwersji wartości x i ta wrtość zostanie wpisan między {}
"""
ilosc = 12
cena = 35
print("Mamy {} sztuk zabawek jedna kosztuje {} zł".format(ilosc, cena))
#Mamy 12 sztuk zabawek jedna kosztuje 35 zł
"""