slownik_1={1:"a", "ala":128, 21:"kot"}
print(slownik_1)
#klucz pierwsza wartośc musi być wartością nie mutowalną
#dodawanie elementów do słownika
slownik_1["nowy_klucz"]=1.8
slownik_1["ala"]=12
slownik_1[1]="bc"
print(slownik_1)

#funkcja zwraca słownik opisujący superpozycję funkcji zadanych
#słownikiem f_1 i f_2
def superposition(f_1,f_2):
    superposition={}
    for i in range(len(f_1)):
        superposition[i]=f_2(f_1[i])
    return superposition
f_1={0:1,1:3,2:1,3:2,4:4}
f_2={0:2,1:3,2:4,3:2,4:4}
print(superposition(f_1,f_2))
#nie działa