""" Rzut kośćmi
 Demonstruje generowanie liczb losowych
 uzycie modułu random,  funkcji randint() randrange()
"""
import random # import modułu random który zawiera funkcję randint() randrange()
# generuj liczby losowe z zakresu 1 - 6
rzut1 = random.randint(1, 6)
#wywołanie funkcji randint() z zaimportowanego modułu random tzw notacja z kropką:
#nazwa_modułu.nazwa_funkcji(argumenty) tutaj argument to zakres losowanych liczb (na kostce)

rzut2 = random.randrange(6) + 1
#wywołanie funkcji randrange() z zaimportowanego modułu random tzw notacja z kropką:
#tutaj argument jest jeden(6) bo funkcja losuje liczbe całkowitą od 0 do 5 czyli 6 wariantów
#0,1,2,3,4,5 dlatego do wyniku dodajemy 1
suma = rzut1 + rzut2
print("Wyrzuciłeś", rzut1, "oraz", rzut2, "i uzyskałeś sumę", suma)
# przkładowy wynik: Wyrzuciłeś 2 oraz 6 i uzyskałeś sumę 8