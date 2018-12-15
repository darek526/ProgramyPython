"""
struktura danych kolecja unikalnych wartości
każda wartość musi być inna
"""
a = set()
print(a)
#set() (zbiór pusty
a = set([1,2,34,5,5,2,7])
print(a) #jesli przy deklaracji zbioru wpiszemy kilka razy
# takie same warości tylko raż zostanie ona wyświetlona
# {1, 2, 34, 5, 7}
b = set([1, 3, 5, 23, 14])
print(a)
print(b)
"""
{1, 2, 34, 5, 7}
{1, 3, 5, 14, 23}
"""
#część wspólna dwóch zbiorów
print(a.intersection(b))
#{1,5}

#połączenie dwóch zbiorów
print(a.union(b))
#{1, 2, 34, 3, 5, 7, 14, 23}#każda wartość tylko raz

#róznica a/b(tylko w a)
print(a.difference(b))
# {2, 34, 7}

#różnica symetryczna a b(odwrotność części wspólnej tylko w a i tylko w b)
print(a.symmetric_difference(b))
# {2, 3, 34, 7, 23, 14}