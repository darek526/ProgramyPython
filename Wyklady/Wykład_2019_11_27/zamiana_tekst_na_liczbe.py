#zamina tekstu na 1c liczbe dziesiętną
def zamiana(text_1):
    number_1=0
    for i in range(len(text_1)):
        number_1=number_1+ord(text_1[i])*(256**i)
    return number_1
#koniec fu
print(zamiana("tresc tekstu"))