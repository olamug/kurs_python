przedmioty = input("Podaj przedmioty podzielone myślnikiem: ")
oceny = input("Podaj oceny podzielone myślnikiem")
przedmioty = przedmioty.split("-")
# wyświetli ['matma', 'polski', 'historia'] przy print(przedmioty)
oceny = oceny.split("-")
licznik = 0
while licznik < 3:
    print(przedmioty[licznik], "-",  oceny[licznik])
    licznik = licznik + 1