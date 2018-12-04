#!/usr/bin/env/usr/bin/python3

def main():
    napis=input("Wpisz słowo, program sprawdzi czy jest to palindrom:\n ")
    print(palindrom(napis))

def palindrom(s):#s przekazuje wpisany napis
    """Tworzy lustzrane odbicie napisu s"""
    t=""#definiujemy nowy łańcuch znaków zaczynamy od pustego napisu
    for c in s:#przechodz pokoleji łancuch s
        t=c + t#

    if s==t:
    # print(s + " " + t)
        return s == t, (s +" "+t)#po przecinku wpisuje ciąg jak poelecenie print powyżej
    else:
        return s == t, (s + " " + t)

main()
