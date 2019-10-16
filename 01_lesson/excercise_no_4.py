# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
title = input("Podaj tytuł książki: ")
name = input("Podaj nazwisko autora: ")
pages = input("Podaj liczbę stron: ")
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print("Czy tytuł składa się tylko z liter?")
print(title.isalpha())
print("Czy nazwisko składa się tylko z liter?")
print(name.isalpha())
print("Czy podane strony to wartość liczbowa?")
print(pages.isdecimal())
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print("Czy tytuł jest zapisany wielką literą?", title.isupper(), "\n powinno być: ", title.capitalize())
print("czy nazwisko jest zapisane wielką literą?", name.isupper(), "\n powinno być: ", name.capitalize())
print()
book = (title.capitalize() + " " + name.capitalize() + " " + pages)
print("Liczba wszystkich wprowadzonych znaków to: ", len(book))