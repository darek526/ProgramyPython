import matplotlib.pyplot as plt
def main():
    #tworzenie listy pkt na wykresie dowolne nazwy list
    x_coordinates=[0,1,2,3,4,5,6,7,8,9,10]
    y_coordinates=[0,-3,2,3,2,3,2,3,4,3,5]

    #tworzenie wykresu
    plt.plot(x_coordinates,y_coordinates)

    #dodawanie opisu rysunku
    plt.title("Wykres naszej funkcji")

    #dodawanie siatki rysunku
    plt.grid(True)

    #Wyświetlanie rysunku
    plt.show()
main()