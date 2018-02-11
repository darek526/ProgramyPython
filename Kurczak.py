czas=""
kurczak_jest=0
rodzaj_programu=0

#komunikaty - start, ktore mozna pozniej wykorzystac
kom_0="Koniec. Brak kurczaka"
kom_1="Kurczak nie zostal upieczony"
kom_2="Kurczak gotowy. Smacznego!"
rodzaj1="1-krotki program, kurczak krwisty\n"
rodzaj2="2-program sredni, kurczak al'dente\n"
rodzaj3="3-program dlugi, kurczak chrupiacy\n"
kom_rodz_1="Zakres czasu pieczenia 60-70 min"   # kom_rodz_1="Zakres czasu pieczenia" + cz1 + " - " + cz2 + min"
kom_rodz_2="Zakres czasu pieczenia 80-90 min"
kom_rodz_3="Zakres czasu pieczenia 100-110 min"
kom_rodz_blad_1="Czas za krotki. "
kom_rodz_blad_2="Czas za dlugi. "
#komunikaty - koniec

#pobranie informacji
kurczak_jest=int(input("\nCzy masz kurczaka?\n"))
if kurczak_jest==0:
    print(kom_0)
    exit
elif kurczak_jest==1:
    kurczak_piec=int(input("\nCzy chcesz upiec kurczaka\n"))
    if kurczak_piec==0:
        print(kom_1)
        exit
    elif kurczak_piec==1:
        print("\nWybierz rodzaj programu\n\n", rodzaj1, rodzaj2, rodzaj3)
        rodzaj_programu=int(input())
        
        if rodzaj_programu==1:
            print(kom_rodz_1)
            while not czas.isdigit(): #najprostsze sprawdzanie czy wprowadzona nizej dana = czas jest liczba, jesli nie to robi pętle tego co jest pod nim za wcięciem (tab)
                czas=input("\nJaki czas pieczenia: \n") #powinna byc procedura sprawdzenia czy wprowadzono liczby
            czas=int(czas)
            if 60 <= czas <= 70:
                print(kom_2)
            elif czas < 60:
                print(kom_rodz_blad_1, "\n", kom_1)
            elif czas > 70:
                print(kom_rodz_blad_2, "\n", kom_1)

        elif rodzaj_programu==2:
            print(kom_rodz_2)
            while not czas.isdigit():
                czas=input("\nJaki czas pieczenia: \n") #powinna byc procedura sprawdzenia czy wprowadzono liczby
            czas=int(czas)
            if 80 <= czas <= 90:
                print(kom_2)
            elif czas < 80:
                print(kom_rodz_blad_1, "\n", kom_1)
            elif czas > 90:
                print(kom_rodz_blad_2, "\n", kom_1)

        elif rodzaj_programu==3:
            print(kom_rodz_3)
            while not czas.isdigit():
                czas=input("\nJaki czas pieczenia: \n") #powinna byc procedura sprawdzenia czy wprowadzono liczby
            czas=int(czas)
            if 100 <= czas <= 110:
                print(kom_2)
            elif czas < 100:
                print(kom_rodz_blad_1, "\n", kom_1)
            elif czas > 110:
                print(kom_rodz_blad_2, "\n", kom_1)
            
    
