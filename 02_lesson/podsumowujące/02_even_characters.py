tekst = str(input("Podaj dowolny tekst, dla kt�rego mam wy�wietli� znaki znajduj�ce si� na parzystych pozycjach:\n"))

# metoda z p�tl� for
for e in range(len(tekst)):
    if e % 2 == 0:
        print(tekst[e], end='')
print()
# metoda string slicing
print(tekst[::2])