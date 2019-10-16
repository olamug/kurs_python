# 1. zadanie - Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
print("ZADANIE PIERWSZE")
txt = 'kalendarz'
print(txt)
middle = len(txt) // 2
print(txt[middle - 1 : middle +2 ])
print()
print("ZADANIE DRUGIE")
# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = input("Podaj pierwszy wyraz: ")
s2 = input("Podaj drugi wyraz: ")
mdl = len(s1) // 2
s3 = (s1[:mdl] + s2 + s1[mdl:])
print(s3)