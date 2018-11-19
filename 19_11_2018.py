"""
liczby zespolone
(a,b)+(c,d)=(a+c,b+d)
(a,b)*(c,d)=(a*c-b*d,a*d+b*c)
a+bj=(a,b)
j*j=-1
"""
zm1=3.1+5.32j
zm2=1+1j
print(zm1,zm2)
#(3.1+5.32j)  (1+1j)

a=5
b=3
z=complex(a,b)
print("część rzeczywista:", end="")
print(z.real)
print(z.imag)
"""
operacje poziomu bitowego
"""
"""
rozkazy logiczne
OR
AND
XOR
"""
"""
liczby binarne, 8-owe, 16-owe
"""
print(bin(23))#0b10111
print(oct(23))#0o27
print(hex(23))#0x17
"""
dodawanie macierzy
mnożenie macierzy 
"""
mac1=[[1,2,3],[4,5,6],[7,8,9]]
mac2=[[9,8,7],[6,5,4],[3,2,1]]
#suma=[[0,0,0],[0,0,0],[0,0,0]]

iloczyn=[[0,0,0],[0,0,0],[0,0,0]]#piszemy same 0
for i in range(0,3):
    for j in range(0,3):
        iloczyn[i][j]=0
        for k in range(0,3):
            iloczyn[i][j]=iloczyn[i][j]+mac1[i][k]*mac2[k][j]
print(iloczyn)#[[30, 24, 18], [84, 69, 54], [138, 114, 90]]

"""
szyfr liniowy ciało z29
"""
"""
szyfr AES foto 11.55
"""
"""
szyfr RSA
1 wybrać dwie(p,q) różne liczby pierwsze(dla sprawdzenia mogą byc małe),
    można z internetu lub użyc generatora liczb pierwszych
    (algorytm Millera-Rabina)(Liczby Mersenne’a)(Sito Eratostenesa)
2 liczymy φ(n)=φ(p*q)=(p-1)(q-1)=120
3 największy wspólny dzielnik
"""
"""
szyfr Rabina
1 wybrać dwie(p,q) różne liczby pierwsze
"""
"""
Chińskie twierdzenie o resztach
"""
"""
Szyfr Playfair
"""