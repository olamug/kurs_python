# W DOMU ROBIONE
def convert(miles):
    return 1.609 * miles
distance = int(input("podaj liczbę mil: "))
miles = convert(distance)
print(miles)

# silnia

def obliczsilnie(a):
    i = 1
    pytanie = input("napisz kot: ")
    silnia = 1
    while i < a:
        i += 1
        silnia = silnia * i
    return(silnia, pytanie)

wynik = obliczsilnie(4)
print(wynik)

#też działająca druga wersja obliczania pola powierzchni koła
def circle_field():
    pi = 3.14
    r = int(input("Podaj promień: "))
    return pi*r**2

print(circle_field())