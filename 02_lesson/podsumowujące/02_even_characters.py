tekst = str(input("Podaj dowolny tekst, dla którego mam wyœwietliæ znaki znajduj¹ce siê na parzystych pozycjach:\n"))

# metoda z pêtl¹ for
for e in range(len(tekst)):
    if e % 2 == 0:
        print(tekst[e], end='')
print()
# metoda string slicing
print(tekst[::2])