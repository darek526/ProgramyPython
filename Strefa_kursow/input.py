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
"""
stolica = 'Dodoma'    # nowa stolica Tanzanii
kraj = 'Tanzania'
populacja = 53950935
 
print('Stolicą kraju ' + kraj + ' jest ' + stolica + '. Populacja kraju: ' + str(populacja) + ' mieszkańców.')
print('Stolicą kraju %s jest %s. Populacja kraju: %d mieszkańców.' % (kraj, stolica, populacja))

    %s – napis, łańcuch znaków,
    %d – liczba całkowita,
    %f – liczba rzeczywista, zmiennoprzecinkowa,
    %e – liczba rzeczywista w notacji naukowej.
print('Najpopularniejsze stałe matematyczne to %s = %.2f i %s = %.3f.' % ('pi', 3.141593, 'e', 2.718282))
#%.2f cyfra po. oznacza ilość wyświetlanych cyfr po przecinku
"""
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
"""
print('Stolicą kraju {} jest {}. Populacja kraju: {} mieszkańców.'.format(kraj, stolica, populacja))
print('Stolicą kraju {2} jest {0}. Populacja kraju: {1} mieszkańców.'.format(stolica, populacja, kraj))  
# wywołanie zmiennej za pomocą indeksu (odwrócona kolejność)
print('Stolicą kraju {kr} jest {st}. Populacja kraju: {pop} mieszkańców.'.format(kr=kraj, st=stolica, pop=populacja))   
# wywołanie do zmiennej przez nazwę
"""
