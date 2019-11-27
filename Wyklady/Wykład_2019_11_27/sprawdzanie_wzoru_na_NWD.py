import math
zmienna_boolowska=True
for n in range(1,501):
    for m in range(1,501):
        for k in range(2,10):
            if math.gcd(k**n-1,k**m-1) !=k**math.gcd(n,m) -1:
                zmienna_boolowska=False
                print("równość nie zachodzi dla k= ",k, "n= ",n, "m= ",m)
if zmienna_boolowska:
    print("równość zachodzi dla wszystkich sprawdzanych wartości zmiennych")
#wolno liczy dla wartości  n m powyżej 401