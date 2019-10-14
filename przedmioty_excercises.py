# poproś użytkownika o podanie 3 przedmiotów oraz ocenę jaką z nich uzyskał.
p=1
while (p<=3):
    przedmiot = input("podaj przedmiot szkolny: ")
    grade = input("ocena w skali 1-6: ")
    print(przedmiot, "-", grade)
    print("Aktualny przedmiot", p)
    p=p+1
# p = zmienna sterująca/counter, licznik do ilu powtarza
przedmioty = input("Podaj przedmioty podzielone myślnikiem: ")
oceny = input("Podaj oceny podzielone myślnikiem")
przedmioty = przedmioty.split("-")
print(przedmioty)
