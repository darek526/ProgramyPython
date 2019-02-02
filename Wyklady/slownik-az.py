import string

lista_liter = []
lista_liczb = []
i = 0
for c in list(string.ascii_lowercase):
    lista_liter.append(c)
    lista_liczb.append(i)
    i = i + 1


lista_liter.append(" ")
lista_liter.append("." )
lista_liter.append("?")

lista_liczb.append(26)
lista_liczb.append(27)
lista_liczb.append(28)

print(lista_liter)
print(lista_liczb)
    
napis = input("napis: ")
zakodowany = []
for c in napis:
    zakodowany.append(lista_liter.index(c.lower()))
print(zakodowany)

odkodowany  = ""
for i in zakodowany:
    odkodowany = odkodowany + lista_liter[lista_liczb[i]]
print(odkodowany)

