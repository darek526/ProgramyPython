#!/usr/bin/env/usr/bin/python3

def main():
    napis=input("wpisz łańcuch znaków: ")
    print(palindrom(napis))

def palindrom(s):#s przekazuje wpisany napis
    """Tworzy lustzrane odbicie napisu s"""
    t=""#zaczynamy od pustego napisu
    for c in s:#przechodz pokoleji łncuch s
        t=c + t#
    print(s +" "+ t)
    return s == t
main()