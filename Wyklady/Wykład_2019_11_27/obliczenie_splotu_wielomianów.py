#mnożenie wielomianów obliczanie splotu
#dwóch ciagów opisujących wielomian f ig

a=[]
b=[]
n=int(input("Wprowadź stopień wielomiany n= "))
for i in range(n+1):
    print("Wprowadź współczynnik wielomianu o numerze i= ")

    x=int(input())
    a.append(x)
for i in range(n + 1):
    print("Wprowadź współczynnik wielomianu o numerze i= ")

    x = int(input())
    b.append(x)
for i in range(n+1):
    a.append(0)
    b.append(0)
for k in range(2*n+1):
    cx=()
    for j in range(i+1):
        cx=cx + a[j] *b[i-j]
    c.append(cx)
print(c)
#Obliczenie dl Z 5
for i in range(2*n+1):
    cx=()
    for j in range(i+1):
        cx=cx +