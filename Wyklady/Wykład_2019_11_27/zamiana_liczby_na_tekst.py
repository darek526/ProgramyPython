def zamiana_na_tekst(number_1):
    list_1=[]
    a=""
    while number_1 !=0:
        list_1.append(chr(number_1 % 256))
        number_1=number_1//256#obliczamy część całkowitą iloraz cząstkowy
    for i in range(len(list_1)):
        a=a+list_1[i]#zamiana listy na string(tekst)
    return a
#koniec funkcji
print(zamiana_na_tekst(245416267745379773948736278894488019213821475356591056971552980189603703169403875184))
# liczba wpisan w print to wynik działania programu zamieniającego tekst na liczbe
# problem przy ś ć ń ą