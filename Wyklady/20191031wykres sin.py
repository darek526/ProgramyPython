import matplotlib.pyplot as plt
import numpy as np
def main():
    #tworzenie listy pkt na wykresie dowolne nazwy list
    x_1=np.linspace(-10.5,10.5)
    y_1=np.sin(x_1)#funkcj sinus
    y_2=np.cos(x_1)#funkcja cos dla tych samych x

    #tworzenie wykresu dodajemy parametry color , grubość, rodzaj(- ciągła --przerywana :kropki) lini
    plt.plot(x_1,y_2)
    plt.plot(x_1,y_1)

    #dodawanie opisu rysunku
    plt.title("Wykres naszej funkcji")

    #dodawanie siatki rysunku
    plt.grid(True)

    #Wyświetlanie rysunku
    plt.show()
main()