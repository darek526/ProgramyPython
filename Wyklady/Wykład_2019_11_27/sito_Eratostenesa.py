#wyszukuje wszystkie liczby pierwsze z podanego przedziału
# przy dużych liczbach wolno pracuje
# nie działa
import math
a=[0,0]
k=int(input("wpisz liczbę maksymalną k= "))
for n in range(2,k+1): a.append(1)#dodanie samych 1
for n in range(2,int(math.sqrt(k))):
    if a[n]==1:
        i=2*n
        while i<=k:
            a[i]=0
            i=i+n
ilosc_liczb=0
for i in range(k+1):
    if a[i]==1:
        print("liczba",i,"jest liczbą pierwszą")
        ilosc_liczb=ilosc_liczb+1
print("ilość liczb pierwszych w tym przedziale wynosi",ilosc_liczb)
print("gęstość teoretyczna", (math.log(k))/k)
print("gęstość eksperymenralna",ilosc_liczb/k)
print((math.log(math.e)))