'''
 Manipulacje cytatami
 Demonstruje metody (upper, lower. title) które poprzedzamy nazwą łańcuch i kropką
 nazwa_łańcucha.metoda
Cytat z wypowiedzi prezesa IBM, Thomasa Watsona, z 1943 r.
'''
quote = "\tMyślę, że istnieje światowy RYNEK dla może pięciu komputerów."
print("Oryginalny cytat:")
print(quote)
print("\nDużymi literami:\n\t\t nazwa.upper()")
print(quote.upper())
print("\nMałymi literami:\n\t\t nazwa.lower()")
print(quote.lower())
print("""\nPierwsza litera każdego słowa została zamieniona na dużą, a wszystkie
pozostałe są zamieniane na małe:\n\t\t nazwa.title()""")
print(quote.title())
print('\nZamiana słów: pięciu na milionów:\n\t\t nazwa.replace("tekst1", "tekst2")')
#najpierw słowo do zamiany w "tekst" później , i nowe słowo "tekst2"
print(quote.replace("pięciu", "milionów"))
print('\nZamienia wszystkie małe litery na dużę a duże na małe:\n\t\t nazwa.swapcase()')
print(quote.swapcase())
print("\nZamienia tylko pierwszą literę pierwszego słowa na dużą, pozostałe zmienia na małe:\n\t\t nazwa.capitalize()")
print(quote.capitalize())
print("""\nWszystkie białe znaki (tabulatory, spacje i znaki nowego wiersza) 
znajdujące się na początku i na końcu zostały usunięte:\n\t\t nazwa.strip()""")
print(quote.strip())