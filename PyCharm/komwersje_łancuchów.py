"""
konwersja przekształcanie łańcuchów
"""
car = input("podaj ile masz samochodów:\n ")
#komunikat o podanie liczby samochodów
car = int(car)#konwersja przekształcenie podanej wartości na wartość typu int liczby całkowite
"""
jeśli nie przekształcimy zmiennych na int (liczby całkowite) to ilość pojazdów
byłby dodaniem łańcuchów tekstowych np 3+5 wynik 35
po konwersji dane traktowane są jak liczby całkowite 3+5 wynik 8
"""
rowery= input("podaj ile masz rowerów:\n")
rowery=int(rowery)

pojazdy= car + rowery
#pojazdy=int(pojazdy) nie musimy konwertować na int

print("posiadasz ", pojazdy, "pojazdów")
