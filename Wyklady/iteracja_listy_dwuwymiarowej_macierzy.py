a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in a:
    for j in i:
        print(j, end=' ')
print()#1 2 3 4 5 6 7 8 9
#przesunięcie print() o 1 tab w prawo wypisze:
'''
1 2 3 4 
5 6 
7 8 9 
'''
#https://snakify.org/pl/lessons/two_dimensional_lists_arrays/
"""
#inna forma zapisu
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
print()
"""
#tworzenie słownika
A = dict(zip('abcdefghijklmnopqrstuvwxyz .?', (range(29))))
for key, val in A.items():
    print(key, val)
#print(A)
b = dict(zip((range(29)),'abcdefghijklmnopqrstuvwxyz .?'))
for key, val in A.items():
    print(key, val)
#print(b)