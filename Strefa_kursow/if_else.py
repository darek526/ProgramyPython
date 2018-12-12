"""
>   większy
>=  wiekszy lub równy
<   mniejszy
<=  mniejszy lub równy
==  rówwny
!=  rózny (nie równy)

"""
a=0

if a == 1:
    print("jeśli warunek po if jest spełniony wartość bedzie True zadziała ten blok")
else:
    print("Jeśli nie speLniony będzie warunek po if (False) zadziała blok po else")
print("\nTen blok zadziała bez względu na spełnienie warunku if else\n koniec")

#pobieramy tylko 1 znak z klawiatury
while 1:#pętla nieskończona
    bit=input("Podaj 0 lub 1 tylko jeden znak: ")
    if len(bit) < 1:
        print("Powtórz nic nie wpisałeś: ")
        #jesli podaliśmy za mało znaków wyśietli info
    elif len(bit) >1:
        print("wpisałeś więcej niż 1 znak powtórz tylko 1 znak")
        #wpisano za dużo znaków
    else:
        print("ok {}".format(bit))
        print("ok " + bit)#tylko wtedy gdy bit to string
        print("ok", bit)
        #jeśli podamy wystarczającą ilość > 4 wyświetli info
        break#kończy, przerywa pętle nieskończoną while


"""
operatory logiczne:
and  oraz obydwa warunki muszą być spełnione
or lub wystarczy że jeden warunek będzie spełniony
not zaprzeczenie
"""
a = 2
b = 3
c = 4
if a ==2 and b == 3 and c ==4:
    print("warunek and spełniony dla a b c")

a = 0
if not a:
    print("warunek spełniony gdy a=0 lub a=False")

#True(1)"string z zawartosćią"  False,(0),"",None
a = True #False
print(type(a))
#<class 'bool'>