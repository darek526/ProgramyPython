#!/usr/bin/env/usr/bin/python3

def main():
    napis=input("wpisz łańcuch znaków: ")
    print(odwrocony(napis))

def odwrocony(s):#s przekazuje wpisany napis
    """Tworzy lustzrane odbicie napisu s"""
    t=""#zaczynamy od pustego napisu
    for c in s:#przechodz pokoleji łncuch s
        t=c + t#
        print(t)#pokazuje wkażdy obieg pętli krok po kroku  nie jest konieczny
    return t# zwracy odwrócony łańcuch 987654321
main()
"""
wpisz łańcuch znaków: 123456789
1
21
321
4321
54321
654321
7654321
87654321
987654321
987654321
"""
