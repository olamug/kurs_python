# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 
num_1 = int(input("Podaj pierwszą liczbę: "))
num_2 = int(input("Podaj drugą liczbę: "))
ratio = num_2 / num_1
print()
print("Dzielenie drugiej liczby przez pierwszą wynosi", ratio)
print()
print("Pierwsza liczba mieści się", num_2//num_1, "razy w drugiej.")
print()
print("Reszta z powyższego dzielenia wynosi", num_2%num_1)