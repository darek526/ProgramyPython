"""
dodawanie i mnożenie macierzy kwadratowej
17/12/2018
"""
n = int(input("podaj wymiar macierzy"))
wiersz=[]
macierz_a =[]
macierz_b = []
macierz_c = []#macierz wynikowa
for j in range(n):

    for i in range(n):
        wiersz.append(float(input("Podaj element nr {} wiersza macierzy".format(i))))
    print(wiersz)

    macierz_a.append(wiersz)
    print(macierz_a)

for j in range(n):

    for i in range(n):
        wiersz.append(float(input("Podaj element nr {} wiersza macierzy".format(j))))
    print(wiersz)

    macierz_b.append(wiersz)
    print(macierz_b)
if wybor ==0:
    #dodawanie macierzy
    for i in range(n):
        for j in range(n):
            macierz_c [i][j] = macierz_a[i][j] + macier_b[i][j]

else:
    #mnozenie macierzy: suma mnożenia wierszy przez kolumny
    for i in range(n):
        for j in range(n):
            macierz_c[i][j]=0
            for k in range(n):
                macierz_c[i][j]+= macierz_a[i][k] * macierz_b[k][i]#ostani nawias[j]
print(macierz_c)