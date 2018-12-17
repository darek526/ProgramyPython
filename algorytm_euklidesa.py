"""
NWD a i b algorytm Euklidesa
"""

a=int(input("podaj liczbę a: "))
b=int(input("podaj liczbę b: "))
if a==b:
    print("NWD = {}".format(a))
else:
    r = 1
    while r !=0:
        r= a % b
        a=b
        b=r
        if r==0:
            print("NWD = {}".format(a))
