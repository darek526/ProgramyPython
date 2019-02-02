# !/usr/bin/python3
def zamiana_liter_na_cyfry():
    text_cyfry = []
    napis = (input("Wpisz tekst jawny, tylko 26 liter lub '? ! ':\n")).upper()  # pobiera napis i automatycznie zamienia małe litery na duże
    # napis= napis.upper() #można użyc tej lini wtedy nie dodajemy .upper() za input
    #napis = " ".join(napis)  # oddziela każdy znak spacja, pozbywa sie spacji
    #text = napis.split()  # zamiana łańcucha znaków napis string na listę text
    for i in range(len(napis)):
        text_cyfry.append(ord(napis[i]) - 65)
    return text_cyfry
print(zamiana_liter_na_cyfry())
"""
def cyfry_na_litery():
    text_cyfry = [0, 11, 0, 12, 0, 10, 14, 19]
    text=[]
    for i in range(len(text_cyfry)):
        text.append(chr(text_cyfry[i]+65))
    text2 = str.join(" ", text)
    return text2
print(cyfry_na_litery())
#print(str(text2))
#https://pl.python.org/forum/index.php?action=printpage;topic=3563.0
"""
