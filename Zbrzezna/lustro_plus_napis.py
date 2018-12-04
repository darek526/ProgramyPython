#!/usr/bin/env/usr/bin/python3

def main():
    napis=input("wpisz łańcuch znaków: ")
    print(mirror(napis))

def mirror(s):#s przekazuje wpisany napis
    """Tworzy lustzrane odbicie napisu s"""
    t=""#zaczynamy od pustego napisu
    for c in s:#przechodz pokoleji łncuch s
        t=c + t#
    return s + ' ' + t#wyswietli napis spacja lustrzane odbicie
main()