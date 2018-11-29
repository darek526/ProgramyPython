"""
listy wielowymiarowe
macierze
"""
macierz=[1,[1,2,3,4]]
#[1]licba 1
#[1,2,3,4]lista wewnętrzna
print(macierz)
#wynik [1, [1, 2, 3, 4]]

#sprawdzenie elementu z 2 listy 3 pozycja
#print (nazwa_listy[nr listy][nr pozycji,indeksu])
print(macierz[1][2]) #wynik 3

#zmiana zawartości listy wewnetrznej
macierz[1][2]=5
#zamiana w liście nr1 pozycji nr2 na wartość 5
#pamiętamy że liczymy nr lit i pozycji od zera
#jeśli wpiszemy pozycje lub nr listy który nie wystepuje otrzymamy komunikat o błędzie
print(macierz) #[1, [1, 2, 5, 4]]