"""
formatownie łańcuchów
"""
#stary sposób formatowania pathon 2 i 3
napis="Ta liczba %f to %s" %(3.14, "liczba pi")
#wynik Ta liczba 3.140000 to liczba pi
print(napis)
#nowy sposób formatowania tylko pathon>3
'{0}, {1}, {2}' .format('a', 'b', 'c')
#uruchamia się tylko w konsoli wynik 'a, b, c'
