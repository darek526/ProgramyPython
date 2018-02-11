import random       #wywolanie funkcji random

random.seed()

#poczatek
while 1:
    a=random.randint(10,20)
    print(a)
    print("Czy chcesz kontynuowac t/n")

    #  decyzja=input()
    #  if decyzja=="n":   zamiast tych dwóch linii możemy zrobić to: 

    if input()=="n":
        break
#koniec 
