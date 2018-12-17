"""
metody operowania strukturami danych np: dodawać, odejmowac, edytować
wszystko jest obiektem w Pythonie
atrybuty (pola)
klasa to ogólny ale precyzyjny opis zbioru obiektów danej klasy
hermetyzacja komunikacja(wspólpraca) obiektów za pomoćą metod
dziedziczenie gdy opracujemy klase możemy ją wykorzystac w innej klasie (rodzic-potomek)
klasa zwierzęta może byc wykorzystana w klasie ssaki. Rodzic może mieć kilku potomków
klasa to model świata rzeczywistego np biuro
polimorfizm(przeciążanie operatorów) ta sam nazwa dla różnych funkcji w różnych klasach
"""
class Kalkulator:#nieużywa się _ korzystamy z dużych liter w każdym
    # słowie, można użyc () jeśli klasa jest potomkiem piszemy(Rodzic_danej _klasy)
    #nasz.obiekcik_1=Kalkulator()
    def __init__(a,b):
            self.a=a#tworzymy atrybuty self widziane przez wszystkie metoy klasy
            self.b=b#przenika przez wszystkie definicje modułów

    def dodawanie(self):#definiujemy metody z  słowem (self)
        return self.a + self.b
    def odejmowanie(self):
        return self.a - self.b
    def mnozenie(self):
        return self.a * self.b
    def dzielenie(self):
        return  a/b # self.a / self.b

    def wydruk_obliczony_wynik:

        print(c)

