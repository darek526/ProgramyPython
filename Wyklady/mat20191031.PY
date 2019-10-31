import matplotlib
import random
import nwd
#Algorytm rozwiązania liniowego układu kongruencji

#Steina
def steina():
    
def element_odwrotny(a,n):
    import nwd
    l=nwd.roz_alg_euk(a,n)
    if l[0]==1:
        return l[1]%n
    else:
        print("element nie ma elementu odwrotnego")
# koniec funkcji element_odwrotny
r=int(input("Wprowadź liczbę kongruencji"))
m=[]
for i in range(r):
    print("Wprowadź moduł nr",i+1)
    zm_pom=int(input())
    m.append(zm_pom)
for i in range(r):
    for j in range(r):
        if i!=j and stein(m[i],m[j])!=l:
            print("złe moduły, wprowadź nowe")
        else:
            print("Moduły są dobrze wybrane")
M=l
for i in range(r):
    M=M*m[i]
a=[]#lista współczynników
for i in range(r):
    print("Wprowadź współczynnik nr",i+1)
    zm_pom=int(input())
    a.append(zm_pom)
k=[]
for i in range(r):
    zm_pom=(M/m[i])*element_odwrotny(M/m[i],m[i])
    k.append(zm_pom)
x_0=0
for i in range(r):x_0=(x_0+k[i]*a[i])%M
print("Rozwiązanie układu kongruencji=",x_0)
#sprawdzenie poprawności rozwiązania
logical_list=[]
for i in range(r):
    zm_pom=(x[i]%m[i]==a[i]%m[i])
    logical_list.append(zm_pom)
wynik=1
for i in range(r):
    wynik=wynik*logical_list[i]
if wynik==1:
    print("x jest dobrym rozwiązaniem")
else:
    print("x_0  nie jest dobrym rozwiązaniem")
