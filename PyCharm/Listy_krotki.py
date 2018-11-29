'''
listy i krotki
'''
lista=[2,3, 3,14, "cztery"]
print(lista)
# wynik [2, 3, 3, 14, 'cztery']
krotki=(2,3, 4, 3.14, "siedem")
print(krotki)
#wynik (2, 3, 4, 3.14, 'siedem')
print(lista[0])
#wyswietla 0 -owy czli 1 element listy 2
print(krotki[-1])
#wyśietla ostatni elemnt krotki siedem
print(lista[1:3])
#wyświetla 2 i 3 element(zakres pierwsza liczba do druga -1) [3, 3]
print(22 in lista)
'''
sprawdzenie czy dany element wystepuje na liście lub krotce wynik
  True prawda jest
  False nieprawda niema
'''
#edycja tylko listy
lista[1]=33
print(lista)
#zamiana 1 elemnetu  tylko dla list krotek nie można edytować
#zamienia 2 element listy [2, 33, 3, 14, 'cztery']
lista[-1]='pies'# pamietamy o "" lub'' w których należy umieścić tekst
print(lista)
#wyświetla [2, 33, 3, 14, 'pies']
lista[1:4]=[9, 8, "trzeci"]
print(lista)
#wynik [2, 9, 8, 'trzeci', 'pies']