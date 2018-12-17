"""
NWD(a,b) ;a,b=N
a>b
nwd(a,b)=nwd(a-b,b)44
"""
a=int(input("podaj liczbę a: "))
b=int(input("podaj liczbę b: "))
while a!=b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("NWD= {}".format(a))