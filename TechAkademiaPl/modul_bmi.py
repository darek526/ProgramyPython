def bmi(imie,wzrost,waga):
    wynik = waga/(wzrost**2)
    print(imie,"Twoje bmi wynosi: ",wynik)
dane=["Marek",1.81,88,]#tworzymy liste z danymi informacjami
bmi(*dane)#tylko jeśli kolejność i ilość jest zgodna wpisanie jakielkolwiek wartości błąd
#bmi(dane[0],dane[1],dane[2])# ten sam efekt mniej pisania
#po wywołanie funkcji bmi wykorzystujemy wartości z listy
