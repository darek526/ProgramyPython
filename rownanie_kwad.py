#program liczy pierwiastki rownania kwadratowego
import math
#print("podaj wartosc a b c ")
a=int(input("podaj liczbe a "))
b=int(input("podaj liczbe b "))
c=int(input("podaj liczbe c "))
print('a =',a,'b =',b,'c =', c)
delta=(b**2)-(4*a*c)
print('delta =',delta)
d = math.sqrt(delta)
if d > 0:
        x1 = (-b-d)/(2*a)
        x2 = (-b+d)/(2*a)
        print('x1=', x1, 'x2=', x2)
if d == 0:
        x0= (-b)/(2*a)
        print('x0=', x0)
if d <0:
        print("delta mniejsza od zera brak rozwiazan")
print("\nKoniec.")#linia inf o zakonczeniu programu