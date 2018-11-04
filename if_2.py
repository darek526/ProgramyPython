"""
instrukcja if, elif, else
"""
wybor=int(input("Podaj liczbe:\n"))
"""komunikat z prośbą o wpisanie liczby, która pobrana będzie jako string
 ciąg znaków. Instrukcja int() konwertuje pobrane dane na liczbe całkowitą
 można to zapisać w 2 liniach kodu:
 wybor=input("Podaj liczbę:\n") #pobranie danych
 wybor=int(wybor) #Konwersja łańcuchów na liczby całkowite
 """
if wybor<0:
    print("liczba ujemna")
elif wybor==0:
    print("to jest 0")#wpisywanie komentarzy wielolinikowych generuje dziwne błędy
else:
    print("jest to liczba dodatnia")
"""brak bloku:
    elif
 spowoduje po wpisaniu 0 wyświetlenie
 jest: to liczba dodatnia, ponieważ nie jest spełniony if czyli nie jest mniejsz od zera
 else to inaczej pozostałe nie spełniające warunku if"""