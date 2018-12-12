'''najpierw nazwa zmiennej identyfikatora po znaku =jej wartość nigdy odwrotnie
przy nazwach najpierw litera później cyfry. Nie używamy spacji słowa łączymy _
slowoDrugie tzw camel
nie uzywamy słów kluczowych break cllass ok 20
'''
a = 1
b = 2
c = 4
print(a, b, c)
'''1 2 4 można było napisaź  też w 3 poleceniach print(a) print(b) print(c) 
 wtedy wyświetla:
 1
 2
 4
 '''
a = 1
b = 2
c = a + b
print(a, b, c)
# 1 2 3
print(a)
print(b)
print(c)
'''
typy zmiennych
'''
a = 2
b = 4.5
print(a)# 2
print(b)# 4.5
# funkcj type podaje typ (rodzaj) zmiennej<
print(type(a)) # class 'int'>
print(type(b))# <class 'float'>
# funkcja isinstance sprawdza czy zmienna ma podany typ wynik True lub False
print(isinstance(a, int)) #True
print(isinstance(b, int)) # False
"""
operacje matematyczne
a + b dodawanie
a - b odejmowanie
a * b mnożenie
a / b dzielenie wynik zawsze to float 4/2=2.0 19/4=4.75
a // b dzielenie  gdzie wynik to wymuszony integer(integer division) 
    odrzuca to co jest po przecinku4//2=2 ale 10//3=3 19//4=4
a % b reszta z dzielenia np 10 $ 5 = 0 bo dzieli się bez reszty
10 % 3 = 1 bo  3*3=9 i zostaje 1 reszty
moąna sprawdzać parzystość liczby jeśli a % b = 0 jest to liczba przysta
a **b potęgowanie a do potegi b
jesli mamy 2 liczby int i float wynik zawsze float 
kolejność operacji jak w innch potegowanie mnożenie dodawanie aby zmienić używamy nawiasów
"""
"""
Inkrementacja zwiekszenie wartośći zmiennej o 1 czyli +1
a += 1  <=>  a = a + 1
Dekrementacj zmniejszenie wartości o 1 czyli -1
a -= 1 <=> a = a - 1
a *= 2 <=> a = a * 2

"""