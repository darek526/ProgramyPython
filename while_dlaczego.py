# Symulator trzylatka
# Demonstruje pętlę while
#nie działa
print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo.\n")
response = "Dlatego"
while response != "Dlatego.":
    response = input("Dlaczego?\n")
    print("Aha, już wiem.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")