a=int(input("podaj liczbę a: "))
b=int(input("podaj liczbę b: "))
k=0
if a==b:
    print("NWD = {}".format(a))
else:
    while a%2==0 & b%2 == 0:
        k = k + 1
        a = a /2
        b = b /2
    while a!=b:
        #print("NWD = {}".format(a*2**k))
        if a % 2 == 0:
            while a % 2 == 0:
                a = a/ 2
        elif b % 2 ==0:
            while b% 2=0:
                b = b/2
        else:
            if a>b:
                a = a -b
            else:
                b = b -a
    print("NWD = {}".format(a*2**k))